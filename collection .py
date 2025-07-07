# list
# ipl=["csk","rcb","kkr","mi"]
# print(2)
# print(ipl[-3:-1])
# ipl[-1]="dc"
# print(ipl)
# ipl[1:2]="gt","gh"
# print(ipl)
# ipl[2:3]="tt"
# print(ipl)


# extend
# x=["a","b","c"]
# y="bnt"
# x.extend(y)
# print(x)

# remove list item
"""
1.remove
2.pop
3.del
4.clear
"""
# n=[2,3,4,6,7]
# print(type(n))
# n.pop(3)
# # n.pop()
# print(n)

# ipl=["csk","mi","rcb","kkr","srh"]
# ipl.pop("mi")
# print(ipl)


# del
# ipl=["csk","mi","rcb","kkr","srh","dc"]
# del ipl

# ipl=["csk","mi","rcb","kkr","srh"]
# n=[]
# for item in ipl:
#     if "k" in item:
#         n.append(item)
# print(n)

# n="abi"
# list1=list(n)
# print(list1)

# x="once upon a time there lived a ghost"
# sentence=x.split()
# largest=[item for item in sentence if len(item)>4]
# print(largest)

# tuple

# a=["apple","banana"]
# b=["cherry","mango"]
# group=a+b
# print(group)

# a=["apple","banana"]
# c=a*2
# print(c)

# a=["apple","banana"]
# print("apple" in a)

# players="dhoni","koli","rohit"
# csk,rcb,mi=players
# print(csk)
# print(rcb)
# print(mi)

# Set

# duplicccate not allow



# add values
# move={"goat","vettaiyan","amaran"}
# move.add("brother")
# print(move)

# remove
"""
remove()
pop()
discard
clear

"""

# ipl={"csk","rcb","mi","kkr"}
# ipl.remove("rcb")
# print(ipl)

# ipl={"csk","rcb","mi","kkr"}
# ipl.pop()
# print(ipl)


# ipl={"csk","rcb","mi","kkr"}
# ipl.discard("rcb")
# print(ipl)

# a={10,20,30}
# b={40,20,60}
# c=a-b
# print(c)

# products={"jam":120,"apple":100,"bread":200}
# products["mazza"]=60
# print(products)
# products["jam"]=50
# a=products.get("appple")
# print(a)
# products.pop("jam")
# print(products)
# products.popitem()
# print(products)


# products={"jam":120,"apple":100,"bread":200}
# print(products.items())

product1={"bread":10}
product2={"jam":20}
product3={"apple":30}
products={
    "p1":product1,
    "p2":product2,
    "p3":product3,
    }
print(products["p1"])