# for loops

# name="abirami"
# for i in name:
#     print(i)

# for i in range(1,10):
#     print(i)

# nested for loop
# for i in range(3):
#     for j in range(2):
#         print(f"({i}-{j})")

# x = int(input())
# y = int(input())
# z = int(input())
# n = int(input())
# for i in range(x+1):
#        for j in range(y+1):
#           for k in range(z+1):
#               if i+j+k!=n:
#                 print(f"({i},{j},{k})")
            

# x = int(input())
# y = int(input())
# z = int(input())
# n = int(input())

# for i in range(x + 1):
#     for j in range(y + 1):
#         for k in range(z + 1):
#             if i + j + k != n:
#                 print(f"({i}, {j}, {k})")


# food=["idly","poori","pongal","dosai","vadai"]
# for item in food:
#     if item=="pongal":
#         continue
#     print(item)

# small_pizza=15
# medium_pizza=20
# large_pizza=25

# # ----------------
# add_pepper_small_pizza=2
# add_peper_large_or_medium_size=3
# add_cheese_any_size=2
# # -------------------

# size=input("what size do you want[s/m/l]")
# add_pepper=input("do you want pepper [y/n]")
# add_cheese=input(" do you cheese [y/n]")

# bill=0

# if size=="s":
#     bill+=small_pizza
# elif size=="m":
#     bill+=medium_pizza
# elif size=="l":
#     bill+=large_pizze
# else:
#     print("invalid input")

# if add_pepper=="y":
#     if size=="s":
#         bill+=add_pepper_small_pizza
#     else:
#         bill += add_pepper_large_or_medium_size
        

# if add_extra_chesse == "y":
#     bill+=add_cheese_any_size
# print(f"your final bill ${bill}")


# small_pizza = 15
# medium_pizza = 20
# large_pizza = 25

# # ----------------
# add_pepper_small_pizza = 2
# add_pepper_large_or_medium_size = 3
# add_cheese_any_size = 2
# # -------------------

# size = input("What size do you want [s/m/l]? ").lower()
# add_pepper = input("Do you want pepper [y/n]? ").lower()
# add_cheese = input("Do you want cheese [y/n]? ").lower()

# bill = 0

# if size == "s":
#     bill += small_pizza
# elif size == "m":
#     bill += medium_pizza
# elif size == "l":
#     bill += large_pizza  # corrected variable name
# else:
#     print("Invalid input")

# if add_pepper == "y":
#     if size == "s":
#         bill += add_pepper_small_pizza
#     else:
#         bill += add_pepper_large_or_medium_size

# if add_cheese == "y":  # corrected variable name
#     bill += add_cheese_any_size

# print(f"Your final bill is: ${bill}")


