# Made by Justin Lee 
# Free use
# IEEE space project

#class planet
#Parameters: string name, float radius, long weight, string color (hexadecimal), the default 
#   x and y values when starting the solar system simulation
from spaceObject import spaceObject

class Planet(spaceObject):
    pass
    def __init__(self, name, radius, mass, color, positionX, positionY):
        super().__init__(name, radius, mass, color, positionX, positionY)

