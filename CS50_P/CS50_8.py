# Lecture 8 - Object-Oriented Programming

def main():
    # this returns type tuple we can write it as following:
    # name, house = get_student()
    # print(f"{name} from {house}") 
    student = get_student() 
    '''
    since the studnet is type tuple it does not allow us to change the values isnide it like this:
        if student[0] == "Padma":
            student[1] = "Ravenclaw
    Thus we should make it a list as in the lines 27-(...)
    '''
    print(f"{student[0]} from {student[1]}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    # this line return only one value, which is a tuple
    return name, house

if __name__ == "__main__":
    main()



# now the get_student returns list 
def main():
    student = get_student() 
    if student[0] == "Padma":
            student[1] = "Ravenclaw"
    print(f"{student[0]} from {student[1]}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return [name, house]

if __name__ == "__main__":
    main()



# now get_student returns dictionary
def main():
    student = get_student() 
    if student["name"] == "Padma":
            student["house"] = "Ravenclaw"
    # we use single quotes inside the paranthesis since we have double quotes outside 
    print(f"{student['name']} from {student['house']}")

def get_student():
    ''' 
    student = {}
    student["name"] = input("Name: ")
    student["house"] = input("House: ")
    return student
    '''
    name = input("Name: ")
    house = input("House: ")
    return {"name": name, "house": house}

if __name__ == "__main__":
    main()



# class - blueprint for pices of data/objects, allows us to define our own data types
class Student:
    # to store the variables in the current object, we use another variables (commonly written as 'self')
    # this can be nambed differently but it should always be the first attribute of the object
    # intilization method
    # if we want to have defualt values def __init__(self, name=None, house=None):
    def __init__(self, name, house):
        if not name:
            # to create our own exceptions, we use the 'raise' keyword
            raise ValueError("Missing name")
        if house not in ["Gyriffindor", "Hufflepuf", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        # instance variables
        self.name = name
        self.house = house

def main():
    student = get_student() 
    print(f"{student.name} from {student.house}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)

if __name__ == "__main__":
    main()



class Student:
    def __init__(self, name, house, patronus=None):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gyriffindor", "Hufflepuf", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house
        self.patronus = patronus
    
    # if we don't define a __str__ function and try to print the object directly it does not write our intention 
    # java'daki String function'u gibi düşün
    def __str__(self):
        return f"{self.name} from {self.house}"

    def charm(self):
        match self.patronus:
            case "Stag":
                return "s"
            case "Otter":
                return "o"
            case "Jack Russel terrier":
                return "r"
            case _:
                return ""
        """
            if self.patronus == "Stag":
                return "s"
            elif self.patronus == "Otter":
                return "o"
            elif self.patronus == "Jack Russel terrier":
                return "r"
            else:
                return "" 
        """
            
def main():
    student = get_student() 
    print(student.charm())

def get_student():
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ")
    return Student(name, house, patronus)

if __name__ == "__main__":
    main()




# to program defensively (we can change the value of house after the user input by typing student.house = "smth")
# that is by using properties - @property (getter/setter methods) - encapsulation
class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house
    
    def __str__(self):
        return f"{self.name} from {self.house}"
    
    # Getter - to indicate a getter we add @property
    @property
    def house(self):
        return self._house

    # Setter - to indicate a setter we add @self.setter 
    @house.setter
    def house(self, house):
        if house not in ["Gyriffindor", "Hufflepuf", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house
    
    @property
    def name(self):
        return self._name

    # if we have an instance variable called name, we cannot have a function called name
    # so we put an underscore in front of the instance variables name in the setter method
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name
            
def main():
    student = get_student() 
    # if we try to type "student.house = 'smth'", the compiler will automatically call the house setter method and raise an error
    # however if we type "student._house = 'smth'", the value of house will change
    # python da java'da olduğu gibi public/private mevzusu yok
    # pyton'da variable'ların başındaki "_", onun 'private' olduğunu belirmek içindir 
    # _ = dokunma, __ = hiç dokunma
    print(student)

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)

if __name__ == "__main__":
    main()



"""
python'da int bir class, constructor call:
    class int(x, base=10)

python'da str bir class, constructor call:
    class str(object='')
str.strip([chars]) ya da str.lower() string class içinde bulunan methodlar 

python'da list bir class, constructor call:
    class list([iterable])
list.append() list class içinde bulunan bir method

python'da dict bir class

print(type(50)) -> <class 'int'>
print(type("hello")) -> <class 'str'>
print(type([])) -> <class 'list'>
print(type(list())) -> <class 'list'>
print(type({})) -> <class 'dict'>
print(type(dict())) -> <class 'dict'>
"""

# @classmethod -  this method is not an instance method that has access to self, 
# # it is an object method that knows what class it is inside
import random

class Hat:
    # class variable - self is no longer relevant
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    # first argument is not self, it is cls
    # we don't want multiple Hat objects, there is only one Hat - Hat class
    @classmethod
    def sort(cls, name):
        # houses is now not an istance variable accessible by self.houses, it is a class variable accessiable by 'class'.houses  
        print(name, "is in", random.choice(cls.houses))

Hat.sort("Harry")
# örnek: java'da Math.random() vardı 




class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house
    
    def __str__(self):
        return f"{self.name} from {self.house}"
    
    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        # create an object of the current class 
        return cls(name, house)
            
def main():
    student = Student.get() 
    print(student)

"""
it would be weird to create a student object to get a student object in a funciton
# so instead of the code below we created the classmethod in lines 254-258
def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)
"""

if __name__ == "__main__":
    main()




# inheritance
class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")
        self.name = name

    ...

# Student is a Wizard
class Sutdent(Wizard):
    def __init__(self, name, house):
        # acess the super class and aceess the __init__ method of the super class and pass the Student's name to Wizard
        super().__init__(name)
        self.house = house

    ...

# Professor is a Wizard
class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject 

    ...

wizard = Wizard("Albus")
student = Student("Harry", "Gyriffindor")
professor = Professor("Severus", "Defense Against Dark Arts")




# operatpr overloading
class Vault:
    def __init__(self, galleons=0, sickles=0, knuts=0):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts
    
    def __str__(self):
        return f"{self.galleons} Galleons, {self.sickles} Sickles, {self.knuts} Knuts"

potter = Vault(100, 50, 25)
print(potter)

weasley = Vault(25, 50, 100)
print(weasley)

"""
galleons = potter.galleons + weasley.galleons
sickles = potter.sickles + weasley.sickles
knuts = potter.knuts + weasley.knuts

total = Vault(galleons, sickles, knuts)
print(total)
"""