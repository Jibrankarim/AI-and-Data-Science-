
#task 1 bank account 
class bankaccount :
    def __init__(self,account_number,balance):
        self.__account_number = account_number
        self.__balance = balance

    def deposit (self, amount):
        self.__balance += amount 
        print("RS" , amount , "was deposit")
        print("Total balance is :", self.get_balance () )

    def withdraw (self, amount):
        self.__balance -+ amount 
        print("RS", amount, "was withdraw")

    def get_balance(self):
        return self.__balance 
    

acc1 = bankaccount (37037 , 20000 )
acc1.deposit (200)
acc1.get_balance 


#Task 2 student Marks Validation 

class Student:
    def __init__(self, name, roll_no, marks):
        self.__name = name
        self.__roll_no = roll_no
        self.__marks = marks 

    def set_marks (self, marks):
        if 0 <= marks <= 100:
           self.__marks = marks
        else:
             print("Enter between 0 and 100.")
    
    def get_name (self):
        return self.__name
    
    def get_roll_no(self):
        return self.__roll_no

    def get_marks(self):
        return self.__marks

student1 = Student( "jibran", 37 , 95)

print("name", student1.get_name())
print("roll_no", student1.get_roll_no())
print("marks", student1.get_marks())

student1.set_marks(76)
print("Updated makrs: ", student1.get_marks)

# task 3: password manager 

class passwordmanager: 
    def __init__(self, username, password):
        self.username = username
        self.__password = password 

    def __check_username (self, name):
        return self.username == name
    
    def __check_password(self, input_password):
        return self.__password == input_password
    

    def set_password (self,old_password , new_password):
        if self.__check_password(old_password):
            self.__password = new_password 
            print("password updated successfully")

        else:
            print("password is incoorect")


user1 = passwordmanager("jibran", "abc123")


user1.set_password("abc123", "cba123")

#Task 4 : Employee protection

class employee :
    def __init__(self, name , salary):
        self.__name = name
        self.__salary = salary 

    def get_name(self):
        return  self.__name
    
    def set_salary (self , salary ):
        if  salary > 0:
             self.__salary = salary
        else:
            print("invalid salary")

    def show_details(self,):
        print(f"Employee_name: { self.__name }")
        print(f"Employee salary: {self.__salary}")





emp1 = employee( "jibran" ,2209)

emp1.show_details()

# Task 5: Shopping Cart 

class shoppingcart:
    def __init__(self):
        self.__items = []

    def add_items(self,item):
        if item not in self.__items :
            self.__items.append(item)

        else:
            print("item already in cart!")
    def remove_item(self, item):
        if item in self.__items:
            self.__items.remove(item)
        else:
            print("item nor found!")

    def view_card(self):
        return self.__items
    


cart = shoppingcart()

cart.add_items("APPLE")
cart.add_items("BANANA")
cart.add_items("MANGO")
cart.add_items("KIVI")

print(cart.view_card())

cart.remove_item("KIVI")
print(cart.view_card())


 #part 2 inheritance practice tasks
# task 1: single level Animal 

class Animal :
    def make_sound(self):
        print("Animal makes a sound")

class Dog (Animal): 
    def make_sound(self):
        print("Dog barks")

a = Animal()
print(a.make_sound())
d = Dog()

print(d.make_sound())

#Task 2: single level vehicle

class vehicle :
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
class car (vehicle):
    def __init__(self, brand , model , seats):
        self.seats = seats
        vehicle.__init__(self, brand, model)


check = car ("Honda", "civic",5)

print("brand:", check.brand)
print("model:", check.model)
print("seats:", check.seats)

#Task 3: multi level family tree

class grandparent:
    def family_name(self):
        print("family name: sukoo")

class parent(grandparent):
    def occupation(self):
        print("occupation: Engineering")

class child(parent):
    def hobby (self):
        print("hobby: Playing Football")

family = child()

family.family_name()
family.occupation()
family.hobby()        

# task 4 multiple inheritance skills

class Father:
    def skills(self):
        return "Scientist"

class Mother:
    def skills(self):
        return "Freelancer"   


class Child(Father, Mother):
    def skills(self):
         return Father.skills(self) + " and " + Mother.skills(self) 
    


check1 = Child()

print("child skills ", check1.skills())