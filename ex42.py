class Animal(object):
    pass
class dog(Animal):
    def _init_(self,name):
	    self.name=name
class cat(Animal):
    def _init_(self,name):
	    self.name=name
class person(object):
    def _init_(self,name):
	    self.name=name
		self.pet=None
class employee(person):
    def _init_(self,name,salary):
	    super(employee,self)._init_(name)
	    self.salary = salary
class Fish(object):
    pass
class Salmon(Fish):
    pass
class Halibut(Fish):
    pass
rover = dog("Rover")
satan = cat("Satan")
mary = person("Mary")
mary.pet = satan
frank = employee("Frank", 120000)
frank.pet = rover
flipper = Fish()
crouse = Salmon()
harry = Halibut()

		
    