week={
    "day1":"monday",
    "day2":"tuesday",
    "day3":"wednesday",
    "day4":"friday",
    "month":{
        "1st":"january",
        "2nd":"feb",
        "year":{
            "year1":"2025",
            "year2":"2024"
        }
    }
}


# print(week["day5"]) # this will give us error ehen there is no value 
# print(week.get("day5"))

# week["day5"]="Saturday"
# print(week)

for day in week:
    print(day)
    print(day,week[day])
    
# for key,value in week.items():
    # print(key,value)

# if "day6" in week:
    # print("day6 exists in week")
    
# print(len(week))

# week.pop("day2")
# week.popitem()
# print(week["month"]["year"]["year1"])

# new_dictionary={x:x**2 for x in range(6)}
# print(new_dictionary)
# new_dictionary.clear()
# print(new_dictionary)

# keys=["1","2","3"]
# default_valu="numbers"
# newdict=dict.fromkeys(keys,default_valu)
# print(newdict)

