class Employee:
    language = "Py" # This is a class attribute
    salary = 1200000

meen = Employee()
meen.language = "Javascript" # This is an instance attribute
print(meen.language, meen.salary)

