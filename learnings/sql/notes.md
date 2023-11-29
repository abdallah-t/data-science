# SQL

SQL is short for Structured Query Language and is a standard language for dealing with relational databases.

A raw is called a record.
A column is called a field.

the number of rows is called cardinality, and the number of columns is called degree.
the number of rows can be changed by adding or removing records, but the number of columns is fixed.

## naming

### tables

- table names are plural or collective nouns
- be lowercase
- no spaces, use underscores

### fields

- be lowercase
- no spaces, use underscores
- be descriptive
- be singular
- be different from table name
- be different from other field names in the same table


## data types

- `VARCHAR` - variable length string
- `CHAR` - fixed length string
- `INT` - integer
- `FLOAT` - floating point number
- `NUMERIC` - fixed point number

## keywords

- `SELECT` - select data from a database
- `FROM` - specify the table to select or delete data from

example: `SELECT * FROM table_name;`

### aliases

- `AS` - specify an alias for a table or a column
example: `SELECT column_name AS alias_name FROM table_name;`
- `DISTINCT` - return only distinct (different) values
example: `SELECT DISTINCT column_name FROM table_name;`

### views

- `CREATE VIEW` - create a view
example: `CREATE VIEW view_name AS SELECT column_name FROM table_name WHERE condition;`f