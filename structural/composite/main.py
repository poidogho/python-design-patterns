from component import Component
from child import Child
from composite import Composite

# create a composite that will have children
subMenu1 = Composite('sub menu1')

# creat and add children to composite
child1 = Child('sub menu1 child 1')
child2 = Child('sub menu1 child 2')

subMenu1.addChild(child1)
subMenu1.addChild(child2)

# create a composite that will be the main menu
mainMenu = Composite('main menu')

# create a child that will have no children
subMenu2 = Child('sub menu 2')

mainMenu.addChild(subMenu1)
mainMenu.addChild(subMenu2)

mainMenu.componentFunc()
