# inheritance in python

# This is the parent class 
class Animal:

    def __init__(self):
        self.num_eyes = 2
    
    def present_eyes(self):
        print("Animal has eyes present")
    
    def eat(self):
        print("The animal can eat")

# This is the way an super class is defined in the subclass
class Fish(Animal):
    def __init__(self):
        # This calls the superclass constructor 
        super().__init__()
        self.gills_num = 2
    
    # This is function overloading
    def present_eyes(self):
        # Overloading the function by calling the same function as the same name as the super class and modifying it a bit. 
        super().present_eyes()
        print("The fish has two gills too")
    
    # This is an independent method of the fish class
    def swim(self):
        print("The fish can swim underwater !")

# Creating an object of the fish class 
fish = Fish()

# Test output for understanding the programs
print(f'fish eyes are {fish.num_eyes}')
fish.present_eyes()
