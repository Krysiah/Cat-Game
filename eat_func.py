import time
def eat(cat_attributes, catname):
    print("You and", catname, "ate some food.")
    time.sleep(2)
    print("[",catname,"'s Energy increased by +1]")
    time.sleep(1)
    print("[", catname,"'s weight increased by +2]")
    time.sleep(1)
    cat_attributes["Weight"] = cat_attributes.get("Weight")+2
    cat_attributes["Energy"]= cat_attributes.get("Energy")+1
    return cat_attributes