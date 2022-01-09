from dog import Dog
# concrete factory flass


class DogFactory:
    def getPet(self):
        return Dog()

    def getFood(self):
        return 'Dog food'
