import time
def nap(cat_attributes, catname):
    print(catname, "decided to take a nap.")
    time.sleep(1)
    print("[",catname,"'s Energy increased by +2]")
    time.sleep(1)
    cat_attributes["Energy"]= cat_attributes.get("Energy")+2
    return cat_attributes