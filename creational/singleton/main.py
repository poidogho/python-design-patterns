from singleton import Singleton

# lets add the founder
founder = Singleton(Founder="Odafe Idogho")
print(founder)

cofounder1 = Singleton(CoFounder="Jesse Okeya")
print(cofounder1)
# printing cofounder1 will retain the informartion of the dictionary of employees and only add to it
