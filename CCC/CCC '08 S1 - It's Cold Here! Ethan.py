cold_city = ""
cold_temp = 0

flag = True
while flag:
    city = input()
    temp = city.split()
    if temp[0] == "Waterloo":
        if int(temp[1]) < int(cold_temp):
            cold_temp = temp[1]
            cold_city = temp[0]
        flag = False
    else:
        if int(temp[1]) < int(cold_temp):
            cold_temp = temp[1]
            cold_city = temp[0]

print(cold_city)