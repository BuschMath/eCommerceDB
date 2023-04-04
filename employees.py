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

    def createEmployee(self):
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

    def sendEmployee(self, db):
        dataEmployee = {"fName": self.fName, "lName": self.lName, "DoB": self.DoB, "SSN": self.ssn,
                "phoneNo":self.phoneNo}
        db.insert_data("employee", dataEmployee)
        employeeRow = db.execute_query(f"SELECT employeeID FROM employee WHERE SSN={self.ssn}")

        dataAddress = {"houseNo": self.houseNo, "streetName": self.streetName, "city": self.city,
                       "stateProvidence": self.stateProvidence, "country": self.country}
