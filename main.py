import SQLServer as sql
import employees as e
import addressGenerator as ag
import Customer_generator as cg
import ItemGen as ig

server = "localhost\SQLExpress"
database = "eCommerce"

db = sql.SQLServer(server, database)

db.connect()

itemGenerator = ig.ItemGen()

# Create item data
itemData = itemGenerator.CreateItemData()

# Print out the item data
print(itemData)
for x in range(10000):
    itemData = itemGenerator.CreateItemData()
    db.send_data('items', itemData, columns=["itemName", "decription", "price"])

'''
headerArray = ['fName', 'lName', 'paymentInfo',  'customerJoinDate', 'phoneNo', 'DoB' ]
inputArray = []

for i in range(10000):
    first_name, last_name = cg.generate_random_name()
    number = cg.generate_random_number()
    date = cg.generate_random_date()
    birthdate = cg.generate_random_birthdate()
    phone_number = cg.generate_random_phone_number()

    inputArray.append((first_name, last_name,number,date, phone_number ,birthdate ))

db.send_data('customer', inputArray , columns= headerArray )
'''
#generate a random row of data

#for i in range(1,100):
    #employeeGen = e.employees()
    #employeeGen.createEmployee(db)

db.disconnect()