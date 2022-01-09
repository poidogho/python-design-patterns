from component import Component


class Child(Component):
    def __init__(self, *args, **kwargs):
        Component.__init__(self, *args, **kwargs)
        self.name = args[0]

    def componentFunc(self):
        '''just prints the name of the child item'''
        print("{}".format(self.name))
