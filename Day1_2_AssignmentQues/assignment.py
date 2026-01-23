from enum import Enum

class Department(Enum):
    HR = "Human Resources"
    DEV = "Development"
    DATA = "Data Science"
    MANAGEMENT = "Manager"

# Employee class with basic attributes (name, id, department). 
class Employee:
    def __init__(self, name, emp_id, department):
        self.emp_id = emp_id
        self.name = name
        self.department = department
    
    # using dunder methods
    def __repr__(self):
        return f"Employee({self.emp_id}, {self.name}, {self.department})"
    
    def __eq__(self, other):
        return isinstance(other, Employee) and self.emp_id == other.emp_id
    
# Manager class that inherits from Employee
class Manager(Employee):
    def __init__(self, emp_id, name, department, team_size=0):
        super().__init__(emp_id, name, department)
        self.team_size = team_size
    
    def __repr__(self):
        return f"Manager: {self.emp_id}, {self.name}, {self.department}, team_size={self.team_size}"

# Developer class that inherits from Employee. 
class Developer(Employee):
    def __init__(self, emp_id, name, department, programming_languages=None):
        super().__init__(emp_id, name, department)
        self.programming_languages = programming_languages if programming_languages else []
    
    def __repr__(self):
        return f"Developer: {self.emp_id}, {self.name}, {self.department}, {self.programming_languages}"

# specialized classes like HRManager, PythonDeveloper, and DataScientist. 
class HRManager(Manager):
    def __init__(self, emp_id, name, team_size=0):
        super().__init__(emp_id, name, Department.HR, team_size)

class PythonDeveloper(Developer):
    def __init__(self, emp_id, name, programming_languages=None):
        languages = programming_languages if programming_languages else ["Python"]
        super().__init__(emp_id, name, Department.DEV, languages)

class DataScientist(Developer):
    def __init__(self, emp_id, name, programming_languages=None):
        languages = programming_languages if programming_languages else ["Python", "R", "SQL"]
        super().__init__(emp_id, name, Department.DATA, languages)

employees = [
    HRManager(101, "Alok", team_size=5),
    PythonDeveloper(102, "Akshit"),
    DataScientist(103, "Pulkit"),
    Manager(104, "Pawan", Department.MANAGEMENT, team_size=10)
]

# Display employees
for emp in employees:
    print(emp)