from cassandra.cluster import Cluster

print("Cassandra DB Test Script")

primary_key_value = input("Please enter a unique PRIMARY KEY>>> ")

integer_value = input("Please enter an INTEGER VALUE>>> ")
integer_value = int(integer_value) # cast string as int

cluster = Cluster()
session = cluster.connect()

cql = "INSERT INTO hellocassandrakeyspace.foo_table (bar, baz) VALUES (%s, %s)"
values = (primary_key_value, integer_value)
session.execute(cql, values)

print("Data Inserted into Cassandra DB")
