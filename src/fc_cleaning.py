import re
#function to get city names where offices are located
def getCity(row):
    of=row.offices
    if type(of) == dict:
        if "city" in of:
            if of["city"]:
                return of["city"]
            else:
                return "NoCity"
        else:
            return None
    else:
        return "NoOffice"

# transform office object into GeoPoint for office
def officeToGeoPoint(row):
    office = row.offices
    if type(office) == dict:
        if 'latitude' in office and 'longitude' in office:
            if office["latitude"] and office["longitude"]:
                return ({
                    "type":"Point",
                    "coordinates":[float(office["longitude"]),float(office["latitude"])]
                },"success")
            else:
                return(None,"Invalid lat and long")
        else:
            return (None,"No lat and long keys in office dict")
    return (None,"No office")

# function to group total_money_raised values by currency and units (only to see how many different values we have)
def getTypeMoney(value):
    if re.search(r"\d+\.*\d*",value):
        return "".join(value.split((re.search(r"\d+\.*\d*",value)).group()))

# function to transform total_money_raised values into $ an k units
# all total_money_raised values in ¥ come from japanese companies
def getMoney(row):
    dic_money = {r"^C\$\d+":["C$",0.71],r"^\$\d+":["$",1],r"^\£\d+":["£",1.25],r"^\€\d+":["€",1.09],r"^kr\d+":["kr",0.1],
                r"^\¥\d+":["¥",0.0093]}
    dic_unit = {"k":1,"M":1000,"B":1000000}
    
    value = row["total_money_raised"]
    if value:
        for key in dic_money.keys():
            if re.search(key,value):
                value = value.split(dic_money[key][0])[1]
                break
        for unit in dic_unit.keys():
            if unit in value:
                return (round(float(value.split(unit)[0])*(dic_money[key][1])*dic_unit[unit],4),"success")
        return (round(float(value)*(dic_money[key][1])/1000,4),"success")
    else:
        return (None, "fail")

# function to get latitude and longitude values from GeoPoint location
def easyLatLng(row):
    loc = row.location
    if type(loc)==dict:
        return {
        "latitude":float(loc["coordinates"][1]),
        "longitude":float(loc["coordinates"][0])
        }
    else:
        return("Invalid lat long")