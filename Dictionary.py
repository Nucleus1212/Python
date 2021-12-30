#Python Dictionary


thislist={
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x=thislist.get("brand")
y=thislist["model"]
z=thislist["year"]
print(x)
print(y)
print(z)

thislist["year"]=2020
print(thislist)

for x in thislist:
    print(thislist[x])

if "model" in thislist:
    print("Yes, there is model in the list")
else:
    print("NO")

print(len(thislist))

thislist["color"]="red"
print(thislist)

thislist.clear()
