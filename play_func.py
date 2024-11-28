import time


def play(cat_attributes, catname):
    print("Playing game!")
    time.sleep(1)
    print("You played chess with", catname)
    time.sleep(1)
    print("[",catname,"'s Intelligence increased by +1]")
    time.sleep(1)
    print("[", catname,"'s Energy decreased by -1]")
    time.sleep(1)
    cat_attributes["Intelligence"] = cat_attributes.get("Intelligence")+1
    cat_attributes["Energy"]= cat_attributes.get("Energy")-1
    return cat_attributes