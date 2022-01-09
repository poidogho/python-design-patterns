from component import Component
from child import Child


class Composite(Component):
    '''concrete class that maintains tree relationship'''

    def __init__(self, *args, **kwargs):
        Component.__init__(self,  args, kwargs)
        self.name = args[0]
        self.children = []

    def addChild(self, child):
        self.children.append(child)

    def removeChild(self, child):
        self.children.remove(child)

    def componentFunc(self):
      #   print name of composite obj
        print("{}".format(self.name))

        for child in self.children:
            child.componentFunc()
