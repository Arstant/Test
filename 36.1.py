from sys import exit

def living_room():
    print "You are greeted by a colorful display of lights cast on an elephant behind the television.\nThere is a pile of coats on the [couch] to the left of the rooms.\nThere is a stairway leading [down] and [up]\nThere also is an ominous looking [box spring] in the corner of the kitchen.\nWhat do you do?"
    choice =raw_input("> ")
    if "down" in choice:
        print "You walk downstairs, passing fredrick the spider"
        basment()
    elif "up" in choice:
        print "You head to the stairs upwards, 8, 2, 6."
        stair_way()
    elif "couch" in choice:
        dead("The coats on the couch start to stir.\nYou get wrapped up and sucked into a black void.\nSurrounded by tiny gnomes.")
    elif "box" in choice:
        dead("You move to inspect the box spring, when suddenly it sprouts a giant dck and attempts to rape you in the eyes.\nYou narrowly escape back to the frozen suburban nightmare.")
    elif "smell" in choice:
        print "You smell a faint vanilla, upon further inspection you see a glade plug in half burnt out."
    else:
        living_room()

def stair_way():
    print "You arrive at a T hallway with 3 doors.\nThere are two doors to the [right] and one to the [left].\nThere is also a stair way leading [up]."
    choice = raw_input("> ")
    if "right" in choice:
        print "You turn to right, there are two doors one is open and contains a toilet and a ninja turtle shower, you go to open the door straight ahead."
        dan_room()
    elif "left"in choice:
        print "You go to the right an ominous squeeky sound is just past the door, you turn the handle..."
        alex_room()
    elif "up" in choice:
        print "You go upstairs "
#def basement():

#def kitchen():

#def alex_room():

#def dan_room():

#def stair_way2():

#def dan_closet():

#def my_room():

#def my_closet():

#def under_bed():

#def pony_land():

#def under_world():

#def narnia():

#def over_world():

#def win_room():

#def secret_room():

def start():
    print "You see a door with a large 5 next to it, a sterile prefab environment is behind you.\nYou can either [open door] or [head] back into your suburban nightmare\n[Also you can [Smell]]"
    choice = raw_input("> ")
    if "open door" in choice:
        living_room()
    elif "smell" in choice:
        print "You smell the freshly cut grass, and troubles of middle class"
    else:
        dead("Your suburban nightmare awaits!")

def dead(why):
    print why, "Beware of dragons!"
    exit(0)
start()