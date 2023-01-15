#object-oriented programming practice
#a method is a fn associated with class

class Employee:
    #use 'pass' to put an empty class
    emp_num=0
    raise_amt=1.04
    def __init__(self, first, last, pay):
        self.first=first  #instance variable
        self.last=last  #instance variable
        self.pay=pay  #instance variable
        self.email=first+'.'+last+'@company.com' #instance variable

        Employee.emp_num+=1
    
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay=int(self.pay*self.raise_amt)

    @classmethod 
    def set_raise_amt(cls, amount):
        cls.raise_amt=amount

    @classmethod #alternative constructor
    def from_string(cls, emp_str):
        first, last, pay=emp_str.split('-')
        return cls(first, last, pay)
    
    @staticmethod 
    def is_workday(day):
        if day.weekday()==5 or day.weekday()==6:
            return False
        return True

emp_1=Employee('Anna', 'Baker', 20000)
emp_2=Employee('Hara', 'Suno', 30000)

print(emp_1.fullname())
print(emp_2.first, emp_2.last)

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

print(Employee.emp_num) #everytime an instance is created it iterates through the init fn and increments value of emp_num

Employee.set_raise_amt(1.05)

print(Employee.raise_amt, emp_1.raise_amt, emp_2.raise_amt)

emp_1_new=Employee.from_string('Avery-Miller-30000')
emp_2_new=Employee.from_string('Jacob-Williams-30000')
emp_3_new=Employee.from_string('Donnie-Darko-30000')
print(emp_1_new.fullname())
print(Employee.emp_num)
import datetime as dt

my_date=dt.date(2022, 4, 12)
print(Employee.is_workday(my_date))
