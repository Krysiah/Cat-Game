import time
def Int_rank_up(cat_attributes, catname,cat_rank):

    if cat_rank["Intelligence_R"] == "Mindful":
        return
    if cat_attributes["Intelligence"] == 10:
        print("**********")
        time.sleep(1)
        print("RANK UP")
        time.sleep(1)
        print(catname,"'s Intelligence has increased to rank 1!")
        time.sleep(2)
        print(catname,"is now Mindful!")
        time.sleep(2)
        cat_rank["Intelligence_R"] = "Mindful"
        print("")
        print("**********")
        time.sleep(1)
        return cat_rank
    
    if cat_rank["Intelligence_R"] == "Mindful":
        return
    elif cat_attributes["Intelligence"] == 15:
        print("**********")
        time.sleep(1)
        print("RANK UP")
        time.sleep(1)
        print(catname,"'s Intelligence has increased to rank 2!")
        time.sleep(2)
        print(catname,"is now Wise!")
        time.sleep(2)
        cat_rank["Intelligence_R"] = "Wise"
        print("")
        print("**********")
        time.sleep(1)
        return cat_rank
    
    if cat_rank["Intelligence_R"] == "Erudite":
        return
    elif cat_attributes["Intelligence"] == 20:
        print("**********")
        time.sleep(1)
        print("RANK UP")
        time.sleep(1)
        print(catname,"'s Intelligence has increased to rank 3!")
        time.sleep(2)
        print(catname,"is now Erudite!")
        time.sleep(2)
        cat_rank["Intelligence_R"] = "Erudite"
        print("")
        print("**********")
        time.sleep(1)
        return cat_rank
    
    else:
        pass
        
        