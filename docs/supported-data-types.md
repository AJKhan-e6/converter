---
description: This document contains the datatypes supported by e6data
---

# Supported Data Types

* [ARRAY](supported-data-types.md#array)
* [BOOLEAN](supported-data-types.md#boolean)
* [DATE](supported-data-types.md#date)
* [DECIMAL](supported-data-types.md#decimal)
* [DOUBLE](supported-data-types.md#doable)
* [FLOAT](supported-data-types.md#float)
* [INT32](supported-data-types.md#int32)
* [INT64](supported-data-types.md#int64)
* [JSON](supported-data-types.md#json) _(as a string)_
* [STRING](supported-data-types.md#string)
* [STRUCT](supported-data-types.md#struct)

### ARRAY

An array of the given component type.

Examples:

* `ARRAY[1, 2, 3]`
* `select array[1,2,3,4]`

### BOOLEAN

Represents boolean values TRUE and FALSE

### DATE

Represents values having values of fields year, month, and day.

### DECIMAL

Represents the numbers with precision and a scale factor of x.

### DOUBLE

Represents x-byte single/variable-precision floating point numbers.

### FLOAT

Represents x-byte single/variable-precision floating point numbers.

### INT32

Represents a 32-bit signed two’s complement integer with a minimum value of $$-2^{31}$$ and a maximum value of $$2^{31}-1$$.

### INT64

Represents a 64-bit signed two’s complement integer with a minimum value of $$-2^{63}$$ and a maximum value of $$2^{63} - 1$$.

### JSON

JSON querying is supported when the JSON data is saved in the form of a string.

### STRING

Represents character string values.

### STRUCT

Represents values with the structure described by a sequence of fields.

Example:

* `struct({value:prod,dpid:51})`
* `select tablename.columnname.structfield1.structfield2 from tablename`
