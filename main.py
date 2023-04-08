import SQLServer as sql

server = "localhost\SQLExpress"
database = "eCommerce"

db = sql.SQLServer(server, database)

db.connect()

#generate a random row of data
data = [("Carter", "Doe")]
columns = ["fName", "lName"]
db.send_data("customer", data, columns=columns) #Send to db
print(f"SELECT customerID FROM customer WHERE fName='{data[0][0]}'")
row = db.execute_query(f"SELECT customerID FROM customer WHERE fName='{data[0][0]}'")
print(row)

db.disconnect()