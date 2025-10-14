class Employee:
    language = "Py" # This is a class attribute
    salary = 1200000

meen = Employee()
meen.name = "Meen" # This is an instance attribute
print(meen.name, meen.language, meen.salary)

mohan = Employee()
mohan.name = "Mohan"
print(mohan.name, mohan.salary, mohan.language)

# Here name is an instance attribute and salary and 
# language are class attributes as they directly belong to the class
