import SQLServer as sql
import employees as e

server = "localhost\SQLExpress"
database = "eCommerce"

db = sql.SQLServer(server, database)

db.connect()

#generate a random row of data
employeeGen = e.employees()
employeeGen.createEmployee(db)

db.disconnect()