wine_rows = []
counter = 0
def sanitize(input_string):
    if type(input_string) != str:
        return None
    else:
        return input_string.replace("(","").replace(")","").replace(",","").replace("*","").replace("&","").replace("'","").replace('"',"").replace("%","").replace("$","").replace("#","").replace("@","").replace("!","").replace("?","").strip()



for row in wine_rows:
    if row.css(f"span#mainContent_gvInventory_lblProduct_{counter}::text").get() == None:
        continue
    pass
    counter +=1
counter = 0
