from planet import Planet
from spaceObject import spaceObject
import json #to encode data to html
def main():
    #initialize all the planets
    # to make life easy we should make a vector with al the planets,
    # so we can modularize the system to add more things on top
    solarSystemObjects = []
#initializing the solar system
    sun = spaceObject("sun", 695700, 1.989e30, "#ffd014", 0, 0)
    mercury = Planet("mercury", 2.440e3, 3.285e23, "#868c86", 0.5, 10)
    venus = Planet("venus", 6052, 4.867e24, "#868c86", 0.5, 10)
    earth = Planet("earth", 6371, 5.972e24, "#4286f4", 0.5, 10)
    mars = Planet("mars", 3390, 6.39e25, "#c1440e", 15, 15)
    jupiter = Planet("jupiter", 69911, 1.838e27, "#d8ca9d", 15, 15)
    solarSystemObjects.append(sun)
    solarSystemObjects.append(mercury)
    solarSystemObjects.append(venus)
    solarSystemObjects.append(earth)
    solarSystemObjects.append(mars)
    solarSystemObjects.append(jupiter) 
    #print(json.dumps(solarSystemObjects[0]))
    sun.spaceObjToJson()
    print(solarSystemObjects[0].name)

if __name__ == "__main__":
    main()
