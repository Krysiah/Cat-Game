#Imports
import time
import play_func
import train_func
import eat_func
import nap_func
import stats_func
import status_check
import game_over
import intel_rank
import strength_rank


cat_attributes = {
    "Intelligence":9,
    "Energy": 5,
    "Weight": 10,
    "Strength":4,
}

cat_rank = {
    "Intelligence_R": "Sentient",
    "Strength_R": "Weak",
}
#naming cat
catname = input("What is the name of your cat?:")
catname = catname.title()
catcolour = input("What colour is the cat?:")
print("You have officially adopted the", catcolour, "cat:", catname,"!")
time.sleep(3)

#Selection code 
while cat_attributes["Energy"] != 0:
    #warnings for poor health
    st_check = status_check.status_check(cat_attributes=cat_attributes, catname=catname)

    #rank up check
    i_rank = intel_rank.Int_rank_up(cat_attributes=cat_attributes, catname=catname, cat_rank=cat_rank)
    s_rank = strength_rank.Str_rank_up(cat_attributes=cat_attributes, catname=catname, cat_rank=cat_rank)

    #selection
    print("What should we do with", catname, "today?")
    time.sleep(2)
    print("""1. Play
2. Train
3. Eat
4. Nap
5. Stats
          """)
    choice = input("===>")
    u_input = choice.upper()

    #choice 1 = play
    if u_input == "PLAY":
        play = play_func.play(cat_attributes=cat_attributes, catname=catname)

    #choice 2 = train
    elif u_input == "TRAIN":
        train = train_func.train(cat_attributes=cat_attributes, catname=catname)

    #choice 3 = eat
    elif u_input == "EAT":
        eat = eat_func.eat(cat_attributes=cat_attributes, catname=catname)

    #choice 4 = sleep
    elif u_input == "NAP":
        nap = nap_func.nap(cat_attributes=cat_attributes, catname=catname)

    #choice 5 = see stats
    elif u_input == "STATS":
        stats = stats_func.stats(cat_attributes=cat_attributes, cat_rank=cat_rank)
   
    #Game Overs:
    game_ovr = game_over.gm_ovr(cat_attributes=cat_attributes ,catname=catname)