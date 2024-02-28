# SQL Limitations

## Statements

The following statements are currently not supported:

| CREATE TABLE    |
| --------------- |
| INSERT INTO     |
| UPDATE          |
| DELETE          |
| CREATE TABLE AS |

## Data Types

Querying complex data types, as listed below, is not currently supported:

| MAP    |
| ------ |
| ARRAY  |
| STRUCT |

## Materialized Views

e6data currently does not support the creation of materialized views for complex data types such as:

| MAP    |
| ------ |
| ARRAY  |
| STRUCT |

## Functions/Procedures

e6data currently does not support the creation of functions/procedures.

## Others

* Correlated Subqueries are currently not supported.
