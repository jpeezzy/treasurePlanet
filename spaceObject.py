# Made by Justin Lee 
# Free use
# IEEE space project

#class planet
#Parameters: string name, float radius, long weight, string color (hexadecimal), the default 
#   x and y values when starting the solar system simulation
#for its position x and y, we have to assume that the sun is the center of the universe
import json
class spaceObject: 
    def __init__(self, name, radius, mass, color, positionX, positionY):
        self.name = name
        self.radius = radius
        self.mass = mass
        self.color = color
        self.x = positionX
        self.y = positionY
#converts the planet clsas to a json structure and appends it to
#a text file
    def spaceObjToJson(self):
        dictionary = {"name" : self.name, "radius" : self.radius, "mass": self.mass, "color": self.color, "x": self.x, "y":self.y}
        print(json.dumps(dictionary))
        f=open('planets.json','a+')
        json.dump(json.dumps(dictionary), f)
        return json.dumps(dictionary)
            

