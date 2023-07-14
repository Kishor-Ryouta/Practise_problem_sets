file = input("Filename: ").lower().strip()
x = file.split(".",-1)

list1 = ["jpeg", "gif", "png"]
list2 = ["pdf", "zip"]
list3 = ["txt"]


if x[1] in list1 and x[1]!= "jpg" and len(x[1])!= 0:
    print("image/",x[1], sep="")

elif x[1] == "jpg":
    print("image/jpeg")

elif x[1] in list2:
    print("application/",x[1], sep="")

elif x[1] in list3:
    print("text/plain")

else:
    print("application/octet-stream")