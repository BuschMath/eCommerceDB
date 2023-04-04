import SQLServer as sql

server = "localhost\SQLExpress"
database = "eCommerce"

db = sql.SQLServer(server, database)

db.connect()

#generate a random row of data
data = {"fName": "Carter", "lName": "Doe"} #place data in dict
db.insert_data("customer", data) #Send to db
