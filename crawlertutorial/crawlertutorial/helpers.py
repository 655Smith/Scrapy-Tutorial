from types import NoneType

def sanitize(input_string):
    if type(input_string) == NoneType:
        return ""
    else:
        return input_string.replace("(","").replace(")","").replace(",","").replace("*","").replace("&","").replace("'","").replace('"',"").replace("%","").replace("$","").replace("#","").replace("@","").replace("!","").replace("?","").strip()

def bottle_response(row,counter):
    bottle = { "Wine Name":"", "Year":0, "Varietal":"", "Country":"", "Region":"", "Sub-Region":"", "Type":"", "Size":"","Availability":0, "Price": 0.0, "Sale Price": None, "CT Link":""}
    bottle["Wine Name"] = sanitize(row.css(f"span#mainContent_gvInventory_lblProduct_{counter}::text").get())
    bottle["Year"] = sanitize(row.css(f"span#mainContent_gvInventory_lblVintage_{counter}::text").get())
    bottle["Varietal"] = sanitize(row.css(f"span#mainContent_gvInventory_lblVarietal_{counter} strong::text").get())
    bottle["Country"] = sanitize(row.css(f"span#mainContent_gvInventory_lblCountry_{counter} strong::text").get())
    bottle["Region"] = sanitize(row.css(f"span#mainContent_gvInventory_lblRegion_{counter} strong::text").get())
    bottle["Sub-Region"] = sanitize(row.css("td.tdItem_desc>p>strong::text").get())
    bottle["Type"] = sanitize(row.css(f"span#mainContent_gvInventory_lblType_{counter} strong::text").get())
    bottle["Size"] = sanitize(row.css(f"span#mainContent_gvInventory_lblSize_{counter}::text").get())
    row_query = bottle["Wine Name"].replace(" ", "+")+"+"+bottle["Year"].replace(" ", "+")
    bottle["CT Link"] = f'=HYPERLINK(\"https://www.google.com/search?q=Cellartracker+{row_query}\")'
    if row.css(f"span#mainContent_gvInventory_lblTotal_{counter}::text").get():
        bottle["Availability"] = sanitize(row.css(f"span#mainContent_gvInventory_lblTotal_{counter}::text").get())
    else:
        bottle["Availability"] = "In Stock"
    if "Regular" in row.css("td.tdItem_order::text").get():
        bottle["Price"] = float(row.css("td.tdItem_order del::text").get().strip("$").replace(",",""))
        bottle["Sale Price"] = float(row.css("td.tdItem_order font::text").get().strip("Sale Price:").strip().strip("$").replace(",",""))
    elif "Price" in row.css("td.tdItem_order::text").get():
        bottle["Price"] = float(row.css("td.tdItem_order::text").get().strip().strip("Price:").strip().strip("$").replace(",",""))
    return bottle