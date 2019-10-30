from cassandra.cluster import Cluster

print("Cassandra DB Query Test")

cluster = Cluster()
session = cluster.connect()

rows = session.execute('SELECT bar, baz FROM hellocassandrakeyspace.foo_table')
for row in rows:
    foo = row[0]
    bar = row[1]
    print("foo: " + foo)
    print("bar: " + str(bar))
