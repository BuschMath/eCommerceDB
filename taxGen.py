import random as r
import SQLServer as sql

class taxGen:
    def createTaxTableByAddress(self, db):
        addressData = db.execute_query(f"SELECT addressID FROM address")

        for address in addressData:
            federal = r.random() / 5
            statetax = r.random() / 5
            county = r.random() / 5
            city = r.random() / 5

            data = [(address[0], federal, statetax, county, city)]
            columnRef = ["addressID", "federal", "statetax", "county", "city"]
            db.send_data("taxes", data, columns=columnRef)