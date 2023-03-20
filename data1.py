# relational databases model data by storing rows and columns in tables
# database = contains many tables
# relation (or table) = contains tuples and attributes
# tuple (or row) = a set of fields that generally represents an "object" like a person
# attribute (also column or field) = one possible element of data corresponding to the object rep. by a row

# 3 major database management systems in wide use:
# oracle - large, commercial, enterprise-scale, very very tweakable
# mysql - simpler but very fast and scalable - commercial open source
# sqlserver - very nice - from microsoft (also Access)
# some differences in how each work, but core is the same

# sqlite is often included in many softwares

# SQL: Insert
# this inserts a row into a table
# INSERT INTO Users (name, email) VALUES ('Kristen', 'kf@umich.edu')

# SQL: Delete
# deletes a row in a table based on a selection criteria
# DELETE FROM Users WHERE email='ted@umich.edu'

# SQL: Update
# Allows the updating of a field with a where clause
# UPDATE Users SET name='Chuck' WHERE email='csev@umich.edu'
# without "WHERE" clauses, it would update every row

# SQL: Select
# the select statement retrieves a group of records - you can either retrieve all the records or a subset with WHERE
# SELECT * FROM Users
# SELECT * FROM Users WHERE email='csev@umich.edu'
# "*" in this case means "all"
# SELECT * FROM Users ORDER BY email
# SELECT * FROM Users ORDER BY name DESC
