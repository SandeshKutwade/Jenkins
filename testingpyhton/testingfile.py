from FirstPython import addition

checking = [
    (1,3,4),
    (0,0,1),
    (-1,0,-1),
    (10,80,90),
]

for i, (a,b, expetections) in enumerate(checking):
    result = addition(a,b)
    if result == expetections:
        print("all good")
    else:
        print("wrong")


