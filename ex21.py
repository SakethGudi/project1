def add(a,b):
    print("Adding %d and %d" %(a,b))
	return a+b
def subtract(a,b):
    print("the difference of %d and %d is" %(a,b))
	return a-b
def product(a,b):
    print("the product of %d and %d is" %(a,b))
	return a*b
def divide(a,b):
    print("when we divide %d and %d we get" %(a,b))
	return a/b
print("Lets do some math")
age = add(30, 5)
height = subtract(78, 4)
weight = product(90, 2)
iq = divide(100, 2)
print("Age: %d, Height: %d, Weight: %d, iq: %d" %(age,height,weight,iq))
print("Heres a puzzle")
what = add(age, subtract(height, product(weight, divide(iq, 2))))
print("That becomes",what, "Can you do it by hand")


