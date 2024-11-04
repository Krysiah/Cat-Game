import time
def train(cat_attributes, catname):
    print("You hit the gym with", catname,".")
    time.sleep(2)
    print("[",catname,"'s Strength inecreased by +1]")
    time.sleep(1)
    print("[",catname,"'s Energy decreased by -1]")
    time.sleep(1)
    print("[", catname,"'s weight decreased by -1]")
    time.sleep(1)
    print("[Your own strength increased by +1 too!]")
    time.sleep(2)
    cat_attributes["Strength"] = cat_attributes.get("Strength")+1
    cat_attributes["Weight"] = cat_attributes.get("Weight")-1
    cat_attributes["Energy"]= cat_attributes.get("Energy")-1
    return cat_attributes