class Employee:
    language = "Python" # This is a class attribute
    salary = 1200000

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good morning")
        
meen = Employee()
meen.language = "Javascript" # This is an instance attribute
meen.getInfo()
meen.greet()
# Employee.getInfo(meen)
