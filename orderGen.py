import random as r
import SQLServer as sql
import dateGenerator as dg

class orderGen:
    def createOrder(self, db):
        customerID = r.randint(1020, 11019)
        addressID = db.execute_query(f"SELECT addressID FROM customerAddressRef WHERE customerID='{customerID}'")
        taxID = db.execute_query(f"SELECT taxID FROM taxes WHERE addressID='{addressID[0][0]}'")
        orderDate = dg.dateGenerator.generate_random_date()
        orderData = [(customerID, orderDate, taxID[0][0])]
        columnRef = ["customerID", "orderDate", "taxID"]
        db.send_data("orders", orderData, columns=columnRef)

        orderID = db.execute_query(f"SELECT orderID FROM orders WHERE customerID='{customerID}' AND orderDate='{orderDate}'")

        numItems = r.randint(1,20)
        itemList = []
        look = True
        for i in range(1,numItems):
            while look:
                itemID = r.randint(2000, 11999)
                if itemID not in itemList:
                    itemList.append(itemID)
                    break

            itemCount = r.randint(1,20)
            itemData = [(orderID[0][0], itemID, itemCount)]
            columnItemRef = ["orderID", "itemID", "itemAmount"]
            db.send_data("ordersItemsRef", itemData, columns=columnItemRef)
            