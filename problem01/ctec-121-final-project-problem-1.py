# CTEC 121 Final Project
# Problem No. 1
# YOUR NAME

'''
PROGRAM OVERVIEW:
===============================


IPO
===============================
INPUTS:


PROCESSES


OUTPUTS:



'''


class Employee:
    def __init__(self,person):
        self.__record_id = person[0]
        self.__employee_id = person[1]
        self.__first_name = person[2]
        self.__last_name = person[3]
        self.__department_name = person[4]
        self.__salary = float(person[5])
        self.__marital_status = person[6]

    def setRaise(self,raiseAmount):
        self.__salary = self.__salary * raiseAmount
        return self.__salary

    def getSalary(self):
        return self.__salary

    def getAllData(self):
        return [self.__record_id, self.__employee_id, self.__first_name, self.__last_name, self.__department_name, self.__salary, self.__marital_status]


def giveRaises(staff,raiseAmount):
    for person in staff:
        person.setRaise(raiseAmount)


def displayStaff(fileHeader,staff,message):
    print(2 * '\n')
    print(message)
    print(2 * '\n')

    print("{0:<12} {1:<12} {2:<12} {3:<30} ${4:<12} {5}".format('Employee ID','First Name','Last Name','Department','Salary','Marital Status'))

    print(90 * '=')

    for person in staff:
        employee = person.getAllData()
        print("{0:<7} {1:<12} {2:<12} {3:<12} {4:<30} ${5:0.2f} {6}".format(employee[0],employee[1],employee[2],employee[3],employee[4],employee[5],employee[6]))


def writeFileWithRaises(fileHeader, employeeRaisesFile,staff):
    employeeRaisesFile.write(fileHeader[0] + ',' + fileHeader[1] + ',' + fileHeader[2] + ',' + fileHeader[3] + ',' + fileHeader[4] + ',' + fileHeader[5] + ',' + fileHeader[6] + '\n')

    for person in staff:
        data = person.getAllData()
        employeeRaisesFile.write(data[0] + ',' + data[1] + ',' + data[2] + ',' + data[3] + ',' + data[4] + ',' + str(data[5]) + ',' + data[6] + '\n')

def main():

    staff = []

    employeeFile = open('employees.csv','r')
    employeeRaisesFile = open('employee_raises.csv','w')

    fileHeader = employeeFile.readline().rstrip().split(',')

    for line in employeeFile:
        person = line.rstrip().split(',')
        staff.append(Employee(person))

    print('Display the Staff List...')    
    displayStaff(fileHeader,staff,'Staff List')

    print('Applying Annual 5% Raises...')
    giveRaises(staff,.05)

    print('Displaying Salaries After Raises Applied...')
    displayStaff(fileHeader,staff,'Staff List After Raises')

    print('Writing the data to employee_raises.csv...')
    writeFileWithRaises(fileHeader,employeeRaisesFile,staff)

    employeeFile.close()
    employeeRaisesFile.close()

main()