from cat import Cat
from dog import Dog

# factory method


def getPet(pet='dog'):
    pets = dict(dog=Dog('teddy'), cat=Cat('peace'))
    return pets[pet]


dog = getPet('dog')
print(dog.speak())

cat = getPet('cat')
print(cat.speak())
