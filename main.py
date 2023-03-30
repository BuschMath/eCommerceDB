import SQLServer as sql

server = "localhost\SQLExpress"
database = "eCommerce"

db = sql.SQLServer(server, database)

db.connect()
