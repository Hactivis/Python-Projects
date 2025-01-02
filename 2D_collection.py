# fruits =     ["apple", "banana", "orange","grapes"]
# vegetables = ["carrot", "potato","beans"]
# snacks =     ["Doritos", "jim jam","too yum"]
#
# groceries = [["apple", "banana", "orange","grapes"],
#              ["carrot", "potato","beans"],
#              ["Doritos", "jim jam","too yum"]]
#
# for collection in groceries:
#     for food in collection:
#         print(food, end=" ")
#     print()

num_pad = ((1,2,3),
           (4,5,6),
           (7,8,9),
           ("*", 0, "#"))

for row in num_pad:
    for num in row:
        print(num,end=" ")
    print()