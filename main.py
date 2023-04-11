import SQLServer as sql
import employees as e
import addressGenerator as ag

server = "localhost\SQLExpress"
database = "eCommerce"

db = sql.SQLServer(server, database)

db.connect()

#generate a random row of data

for i in range(1,100):
    employeeGen = e.employees()
    employeeGen.createEmployee(db)

db.disconnect()