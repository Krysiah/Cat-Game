import time
def status_check(cat_attributes, catname):
    if cat_attributes["Energy"] <= 3:
        print(catname,"is low on energy. Please, allow them to rest.")
        time.sleep(2)
    elif cat_attributes["Weight"] >=13:
        print(catname,"is gaining unhealthy weight. Try to get rid of it.")
        time.sleep(2)
    elif cat_attributes["Weight"] <=7:
        print(catname,"is looking frail. Are you feeding it enough?.")
        time.sleep(2)