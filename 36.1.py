from sys import exit

def living_room():
    print "You are greeted by a colorful display of lights cast on an elephant behind the television.\nThere is a pile of coats on the [couch] to the left of the rooms.\nThere is a stairway leading [down] and [up]\nThere also is an ominous looking [box spring] in the corner of the kitchen.\nWhat do you do?"
    choice =raw_input("> ")
    
    if "down" in choice:
        print "You walk downstairs, passing fredrick the spider"
        basement()
    
    elif "up" in choice:
        print "You head to the stairs upwards, 8, 2, 6."
        stair_way()
    
    elif "couch" in choice:
        dead("The coats on the couch start to stir.\nYou get wrapped up and sucked into a black void.\nSurrounded by tiny gnomes and the great Cthulhulu staring at you.\nYou go insane.\nAnd attempt to eat your own head.")
    
    elif "box" in choice:
        dead("You move to inspect the box spring, when suddenly it sprouts a giant dck and attempts to rape you in the eyes.\nYou narrowly escape back to the frozen suburban nightmare.")
    
    elif "smell" in choice:
        print "You smell a faint vanilla, upon further inspection you see a glade plug in half burnt out."
    
    else:
        living_room()

def stair_way():
    print "You arrive at a T hallway with 3 doors.\nThere are two doors to the [right] and one to the [left].\nThere is also a stair way leading [up]."
    key = False
    while True:
        choice = raw_input("> ")
        
        if choice == "right" and key:
            print "You turn to right, there are two doors one is open and contains a toilet and a ninja turtle shower, you go to open the door straight ahead."
            basement()
       
        elif choice == "left" and key:
            print "You go to the right an ominous squeeky sound is just past the door, you turn the handle..."
            basement()
        
        elif "up" in choice:
            print "You go upstairs "
        
        elif choice == "left" and not key:
            print "You approach the door but it is locked.\nYou get a slight waft of some kind of baked good"

        elif choice == "right" and not key:
            print "You approach the door but the sound of furious fapping scares you away"
        
        elif choice == "smell" and not key:
            print "You smell something sweet, you look up and there is a floating key in the center of a doughnut\nYou take the key and can continue"
            key = True
        
        else:
            print "Yo, you cray cray"
def basement():
    print "You walk down the stairs to a fairly open unfinished basement with a large black carpeted section to your left and a washer and dryer to your right.\nIt also looks like some kind of tiny human stores her junk down here.\nThere is also a [tiny] hole in the wall just big enough for your hand to fit in\nIf that scares you, you can always go back upstairs"
    choice = raw_input("> ")
    if "smell" in choice:
        print "You smell something musty, seems to be originating from the tiny hole"
    elif "tiny" in choice:
        dead("You feel somthing slimy, and realize that you just stuck your hand into a sleeping dragons nostril.\nHe wakes up and says \"Fucking millennials\" \nThen eats your face")
    elif "back" in choice:
        living_room()
    else:
        basement()

#def kitchen():

def alex_room():
    print "You look around the room, there is nothing of note here except a small frog statue with a stick in its mouth"
    choice = raw_input("> ")
    if "smell" in choice:
        print "Smells of faintly of patchuli"

    elif "leave" or "back" in choice:
        stair_way()
    
    elif "Look" in choice:
        print "Upon further inspection you see a riding harness and a small elephant in the corner"


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
        print "Sometimes in life, some things are beyond our comprehension, this is one of those things. Try again."
        start()

def dead(why):
    print why, "Congratulations!"
    exit(0)
start()