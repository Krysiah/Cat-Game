import time
def Str_rank_up(cat_attributes, catname,cat_rank):
    if cat_rank["Strength_R"] == "Stable":
        return 
    if cat_attributes["Strength"] == 5:
        print("**********")
        time.sleep(1)
        print("RANK UP")
        time.sleep(1)
        print("[",catname,"'s Strength has increased to rank 1!]")
        time.sleep(2)
        print(catname,"is now Stable!")
        time.sleep(2)
        print("You've grown a bit too!")
        time.sleep(2)
        print("You are now Capable!")
        time.sleep(2)
        cat_rank["Strength_R"] = "Stable"
        print("")
        print("**********")
        time.sleep(1)
        return cat_rank
    
    if cat_rank["Strength_R"] == "Sturdy":
        return    
    elif cat_attributes["Strength"] == 10:
        print("**********")
        time.sleep(1)
        print("RANK UP")
        time.sleep(1)
        print("[",catname,"'s Strength has increased to rank 2!]")
        time.sleep(2)
        print(catname,"is now Sturdy!")
        time.sleep(2)
        print("You've grown a bit too!")
        time.sleep(2)
        print("You are now Powerful!")
        time.sleep(2)
        cat_rank["Strength_R"] = "Sturdy"
        print("")
        print("**********")
        time.sleep(1)
        return cat_rank
    
    if cat_rank["Strength_R"] == "Vigorous":
        return
    elif cat_attributes["Strength"] == 15:
        print("**********")
        time.sleep(1)
        print("RANK UP")
        time.sleep(1)
        print("[",catname,"'s Strength has increased to rank 3!]")
        time.sleep(2)
        print(catname,"is now Vigorous!")
        time.sleep(2)
        print("You've grown a bit too!")
        time.sleep(2)
        print("You are now The Strongest!")
        time.sleep(2)
        cat_rank["Strength_R"] = "Vigorous"
        print("")
        print("**********")
        time.sleep(1)
        return cat_rank
    
    else:
        pass
        
        