# Other Limitations

## File Formats

e6data currently does not support the following file formats:

| Orc                                                                                                |
| -------------------------------------------------------------------------------------------------- |
| Avro                                                                                               |
| CSV                                                                                                |
| JSON _(however, JSON data which is stored in Parquet files can be queried when saved as a string)_ |

## Compression Codecs

e6data currently does not support the following compression codecs:

| Parquet files compressed using LZO codec    |
| ------------------------------------------- |
| Parquet files compressed using BROTLI codec |
