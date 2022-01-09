# Pet store houses the abstract factories
class PetStore:

    def __init__(self, petFactory=None):
        self._petFactory = petFactory

    def showPet(self):
        pet = self._petFactory.getPet()
        petFood = self._petFactory.getFood()

        print(pet, petFood)
        print('------------')

        print("Our pet is '{}'!".format(pet))
        print("Our pet says hello by '{}'!" .format(pet.speak()))
        print("its food is '{}' !" .format(petFood))
