# Import the openai library and os module to set the API key
import openai
import os
from llama_index.llms import OpenAI
from llama_index import (
    GPTVectorStoreIndex,
    SimpleDirectoryReader,
    ServiceContext,
    StorageContext, load_index_from_storage, set_global_service_context
)
from llama_index.storage.docstore import SimpleDocumentStore
from llama_index.storage.index_store import SimpleIndexStore
from llama_index.vector_stores import SimpleVectorStore
from llama_index.embeddings.openai import OpenAIEmbedding
import streamlit as st

# Setting up the prompts
#setting up assistant prompt
os.getcwd()
gen_assistant_prompt_file=open('gen_assistant_prompt_spec_line.txt','r')
gen_assistant_prompt=gen_assistant_prompt_file.read()
gen_prompt_file=open('gen_prompt.txt')
gen_prompt=gen_prompt_file.read()


# setting up the documentation paths
document_path = "./docs/equivalent-functions-and-operators.md"
# document_path = '/home/abdul/Downloads/text-to-sql/Talk with documentation/docs/e6-documentation-main'

# Setting up persistent directory paths
persistent_path = "./stores/equivalent-functions"
# persistent_path = '/home/abdul/Downloads/text-to-sql/Talk with documentation/stores'

# Initialising streamlit page
st.set_page_config(page_title="Query Converter", layout="centered", initial_sidebar_state="auto", menu_items=None)
# OPENAI_API_KEY=
# openai.api_key=
st.title("Convert Queries")

if "messages" not in st.session_state.keys(): # Initialize the chat messages history
    st.session_state.messages = [
        {"role": "assistant", "content": "..."}
    ]

service_context = ServiceContext.from_defaults(llm=OpenAI(temperature=0, model="gpt-4-turbo-preview",api_key="", system_prompt=gen_assistant_prompt), embed_model=OpenAIEmbedding(model="text-embedding-3-large"), chunk_size=4100)
set_global_service_context(service_context=service_context)


@st.cache_resource(show_spinner=False)

def load_data(persistent=True):
     
    
    index = None
    

    if persistent:
        print("started the loading document process...")
        print("Fetching indexed document...")
        storage_context = StorageContext.from_defaults(
            docstore=SimpleDocumentStore.from_persist_dir(persist_dir=persistent_path),
            vector_store=SimpleVectorStore.from_persist_dir(
                persist_dir=persistent_path
            ),
            index_store=SimpleIndexStore.from_persist_dir(persist_dir=persistent_path),
        )
        print("Fetched index process...")
        index = load_index_from_storage(storage_context)
        print("Loading Context ...")
    else:
        print("started the loading document process...")
        documents = SimpleDirectoryReader(input_files={document_path}).load_data()
        print("started the indexing process...")
        index = GPTVectorStoreIndex.from_documents(documents, service_context=service_context)
        # print("Persisting the index ...")
        # index.storage_context.persist(persist_dir=persistent_path)

        # # Check if 'default__vector_store.json' exists in the folder
        # default_vector_store_path = os.path.join(persistent_path, 'default__vector_store.json')
        # vector_store_path = os.path.join(persistent_path, 'vector_store.json')

        # if os.path.exists(default_vector_store_path):
        #     # Check if 'vector_store.json' exists
        #     if os.path.exists(vector_store_path):
        #         # Delete 'vector_store.json' if it exists
        #         os.remove(vector_store_path)

        #     # Rename 'default__vector_store.json' to 'vector_store.json'
        #     os.rename(default_vector_store_path, os.path.join(persistent_path, 'vector_store.json'))

	
    return index


index = load_data(False)


if "chat_engine" not in st.session_state.keys(): # Initialize the assistant
        # st.session_state.chat_engine = index.as_query_engine(response_mode="compact", verbose=True, similarity_top_k=6)
        st.session_state.chat_engine = index.as_query_engine(verbose=True, similarity_top_k=2)



if prompt := st.chat_input("Your question"): # Prompt for user input and save to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

for message in st.session_state.messages: # Display the prior chat messages
    with st.chat_message(message["role"]):
        st.write(message["content"])

# If last message is not from assistant, generate a new response
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = st.session_state.chat_engine.query(prompt)
            st.write(response.response)
            message = {"role": "assistant", "content": response.response}
            st.session_state.messages.append(message) # Add response to message history