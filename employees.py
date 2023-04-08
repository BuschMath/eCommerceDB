import nameGenerator as ng
import dateGenerator as dg
import ssnGenerator as sg
import phoneNoGenerator as pg
import addressGenerator as ag
import SQLServer as sql

class employees:

    def __init__(self) -> None:
        pass

    def createDepartment():
        pass

    def createEmployee(self, db):
        self.fName = ng.nameGenerator.generate_random_name()
        self.lName = ng.nameGenerator.generate_random_name()
        self.DoB = dg.dateGenerator.generate_random_date()
        self.ssn = sg.ssnGenerator.generate_random_ssn()
        self.phoneNo = pg.phoneNoGenerator.generate_random_phone_number()

        self.houseNo = ag.addressGenerator.generate_random_house_number()
        self.streetName = ag.addressGenerator.generate_random_streetCityStateCountry_name()
        self.city = ag.addressGenerator.generate_random_streetCityStateCountry_name()
        self.stateProvidence = ag.addressGenerator.generate_random_streetCityStateCountry_name()
        self.country = ag.addressGenerator.generate_random_streetCityStateCountry_name()

        self.sendEmployee(db)

    def sendEmployee(self, db):
        dataEmployee = [(self.fName, self.lName, self.DoB, self.ssn, self.phoneNo)]
        columnsEmployee = ["fName","lName","DoB","SSN", "phoneNo"]
        db.send_data("employee", dataEmployee, columns=columnsEmployee)
        employeeRow = db.execute_query(f"SELECT employeeID FROM employee WHERE SSN='{self.ssn}'")

        dataAddress = [(self.houseNo, self.streetName, self.city, self.stateProvidence, self.country)]
        columnsAddress = ["houseNo","streetName","city","stateProvidence","country"]
        db.send_data("address", dataAddress, columns=columnsAddress)
        addressRow = db.execute_query(f"SELECT addressID FROM address WHERE houseNO='{self.houseNo}' AND streetName='{self.streetName}'")

        dataRef = [(employeeRow[0][0], addressRow[0][0])]
        columnRef = ["employeeID", "addressID"]
        db.send_data("employeeAddressRef", dataRef, columns=columnRef)
