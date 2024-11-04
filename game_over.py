import time
def gm_ovr(cat_attributes, catname):

    #Energy used up
    if cat_attributes["Energy"] == 0:
        print("""


        """)
        print(catname, "has ran out of energy and passed out!")
        time.sleep(3)
        print("[ You can no longer play with", catname,"]")
        time.sleep(2)
        print("Leave at once you bad cat owner!")
        time.sleep(2)
        print("[GAME OVER]")
        quit()

    #Fat cat
    elif cat_attributes["Weight"] >= 15:
        print("""


        """)
        print(catname, "has become too plump! their veins has been filled with unecessary blockage!")
        time.sleep(5)
        print(catname, "had a severe heart attack!")
        time.sleep(3)
        print("[ You can no longer play with", catname,"]")
        time.sleep(3)
        print("No hospital can save them now! Shoo off at once! Shoo!")
        time.sleep(3)
        print("[GAME OVER]")
        quit()
    
    #Hunger loss
    elif cat_attributes["Weight"] <= 5:
        print("""


        """)
        print(catname, "has not been fed for too long! They can't lift a single bone!")
        time.sleep(3)
        print(catname, "died AGONIZINGLY due to hunger loss!")
        time.sleep(3)
        print("[ You can no longer play with", catname,"]")
        time.sleep(3)
        print("Can't even feed a cat food properly!? PATHETIC!")
        time.sleep(3)
        print("[GAME OVER]")
        quit()