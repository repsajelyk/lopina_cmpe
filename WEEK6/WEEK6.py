# TOPICS: SET, LIST, TUPLE, DICTIONARY

fruitsA = ["apple", "apple", "orange", "banana", "grapes"]
print(fruitsA)
print(fruitsA)
print(fruitsA)
print(fruitsA[2])
print(fruitsA.index("orange"))
isThere = "orange" in fruitsA
print(isThere)

fruitsA.append("guava")
print(fruitsA)
fruitsA.append("watermelon")
print(fruitsA)

fruitsA.insert(2, "cacao")
print(fruitsA)

len(fruitsA)
print (len(fruitsA))

print(fruitsA.count("grapes"))

fruitsA.remove("apple")
print(fruitsA)
fruitsA.remove("apple")
print(fruitsA)
print(fruitsA.index("orange"))
fruitsA[1] = "tomato"
print(fruitsA)

fruitsA = ["apple", "apple", "orange", "banana", "grapes"]
fruitsB = ["watermelon", "cacao", "pineapple", "tomato", "lychee"]
fruitsC = ["mango", "cottonfruit", "melon", "pomelo", "apricot"]

fruitBasket_list = [fruitsA, fruitsB, fruitsC]
print(fruitBasket_list)
print(fruitBasket_list[2])
print(fruitBasket_list[1][3])

fruitBasket_plus = fruitsA + fruitsB + fruitsC
print(fruitBasket_plus)

(fruitsA.extend(fruitsB))
(fruitsB.extend(fruitsC))
print(fruitsA)
print(fruitsB)

fruitsA = {"apple", "apple", "orange", "banana", "grapes", "cacao"}
fruitsB = {"watermelon", "cacao", "pineapple", "tomato", "lychee", "banana"}
print(fruitsA)

fruitsA.add("lychee")
print(fruitsA)

fruitsUnion = fruitsA.union(fruitsB)
print(fruitsUnion)

fruitsIntersection = fruitsA.intersection(fruitsB)
print(fruitsIntersection)

fruitDifference = fruitsA.difference(fruitsB)
print(fruitDifference)

fruitbasketlisofset = [fruitsA, fruitsB]
print(fruitbasketlisofset)

fruitsA = ("apple", "apple", "orange", "banana", "grapes", "cacao")
print(fruitsA)

fruitbasket = (fruitsA, fruitsB)
print(fruitbasket)

superlist = [ {1, 2, 3}, True, fruitbasket, ["a"], [True, False], 13107]
print(superlist)

mytuple = (
(1, 2, 3, "A"),
(4, 5, 6, "B"),
(7, 8, 9, "C"),
)

print(mytuple[2][2])

myInfo =  {"Name": "Jasper",
           "Age": 18,
           "Height": 1.65,
           "Address": "Pasay" }
print(myInfo)
print(myInfo["Age"])
print(myInfo["Height"])
print(myInfo["Address"])
print(myInfo.get("Address"))

myInfo["Name"] = "Kyle"
print(myInfo)

print(myInfo["Name"])

myInfo.update({"Section" : 4})
print(myInfo)
print(myInfo["Section"])

myInfo.update({"Name": "Rona"})
print(myInfo)



myInfo ={"Name" : {"Fist Name" : "Jasper", "Last Name" : "Lopina"},
                  "Age" : 18, "Height": 1.65,
                  "Address": "Pasay",
                  "Hobbies" : ("Playing Video Games" ,
                               "Movies") }
print(myInfo)

print(myInfo["Name"]["Last Name"])
print(myInfo["Hobbies"])

simpleATMDatabase = {
    "Name": {
        "Fist Name": "Jasper",
        "Last Name": "Lopina"
    },
    "AccountNumber" : 13107,
    "PIN" : 2007,
    "Control Number" : 4321,
    "Balance" : 1000,}

myName = input("Enter your name: ")
myAccountNumber = input("Enter your account number: ")
myPIN = input("Enter your PIN: ")

print(f"Balance: {simpleATMDatabase['Balance']}")
