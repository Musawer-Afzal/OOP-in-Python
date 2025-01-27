#                              CLASS and OBJECTS

# "Everything is a Object in Python"
# You can make your own datatype using OOP

# Syntax to create an Object
# object_name = class_name()
# example: L = list(), s = str()

# Class
class Atm:
    # Constructor, Variable in a class are always made inside a constructor
    def __init__(self): # It is a Constructor
        # print(id(self)) # It will print the address of the object        
        self.pin = ""
        self.balance = 0
        self.menu()
    def menu(self):
       user_input = input("""
        Hi, How can i help you?
              1. Press 1 to create pin
              2. Press 2 to change pin
              3. Press 3 to check balance
              4. Press 4 to withdraw
              5. Anything else to exist         
            """)
       
       if user_input == "1":
           self.create_pin()
       elif user_input == "2":
            self.change_pin()
       elif user_input == "3":
            self.check_balance()
       elif user_input == "4":
            self.withdraw()
       else:
            exit()
    
    def create_pin(self):
        self.pin = input("Enter your pin: ")
        print("Pin has been created")

        self.balance = int(input("Enter your balance: "))
        print("Balance has been created")
        self.menu()

    def change_pin(self):
        old_pin = input("Enter your old pin: ")
        if old_pin == self.pin:
            self.pin = input("Enter your new pin: ")
            print("Pin has been changed")
            self.menu()
        else:
            print("Wrong Pin")
            self.menu()

    def check_balance(self):
        pin = input("Enter your pin: ")
        if pin == self.pin:
            print("Your balance is: ", self.balance)
            self.menu()
        else:
            print("Wrong Pin")
            self.menu()
    
    def withdraw(self):
        pin = input("Enter your pin: ")
        if pin == self.pin:
            amount = int(input("Enter the amount to Withdraw: "))
            if amount <= self.balance:
                self.balance -= amount
                print("Withdraw successful, Remaining balance is:", self.balance)
            else:
                print("Insufficient balance")
        else:
            print("Wrong Pin")
            self.menu()

obj = Atm()
# Both self and obj are pointing at the same place
# Meaning self = obj
print(id(obj))




# Magic Methods/ Dunder Methods
# Magic Methods are special Methods that have a special super power
# Example
# __init__ - Constructor, Unlike other functions it is directly called when a object is created

# What is the benefit of Constructor Function being initialised by itself when 
# object is created??
# Ans: Some data access is not allowed to be given to user.
# Constructor is used to write configuration related code
# Example: Connecting to Database or Connecting to Network/Internet

#                       SELF Keyword

# self is a reference to the current instance of the class
# Golden rule of OOP
# Who can access Class Members?
# Only the Object of that class
# Example: If Balance Functiom wants to access Withdraw Function, it is not allowed
# Now this is where "self" comes into picture



#                        CREATING OUR OWN DATATYPE
print(3/4*1/2) # 0.375, I donot want this


class Fraction:
    def __init__(self, x, y): # Parameterized Constructor
        self.num = x
        self.den = y
    
    def __str__(self):
        return f"{self.num}/{self.den}"

    def __add__(self, other):
        new_num = self.num * other.den + self.den * other.num
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def __sub__(self, other):
        new_num = self.num * other.den - self.den * other.num
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def __mul__(self, other):
        new_num = self.num * other.num
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def __truediv__(self, other):
        new_num = self.num * other.den
        new_den = self.den * other.num
        return Fraction(new_num, new_den)

    def convert_to_decimal(self):
        return self.num/self.den


fr1 = Fraction(3,4)
print(type(fr1))
print(fr1) # <__main__.Fraction object at 0x000001898F565CD0>, Interpreter doesnot know what it looks like
# After using __str__ it will print the Parameters
fr2 = Fraction(1,2)
print("Addition: ",fr1 + fr2) # When + Operator is added between them, Interperator will enter __add__ and return whats inside
print("Substraction: ",fr1 - fr2)
print("Multiplication: ",fr1 * fr2)
print("Division: ",fr1 / fr2)
print("Decimal: ",fr1.convert_to_decimal())

# The Functions above are called Magic Methods, __add__, __sub__, __mul__, __truediv__
# Whereas convert_to_decimal is not a Magic Method