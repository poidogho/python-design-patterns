from dog_factory import DogFactory
from pet_store import PetStore

factory = DogFactory()
shop = PetStore(factory)

shop.showPet()
