from english import English
from french import French
from adapter import Adapter

objects = []
fr = French()
eng = English()

objects.append(Adapter(fr, speak=fr.speakFrench))
objects.append(Adapter(eng, speak=eng.speakEnglish))

for language in objects:
    print("{} says '{}' \n".format(language.name, language.speak()))
