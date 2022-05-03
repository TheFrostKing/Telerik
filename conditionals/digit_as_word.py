my_dict = {0:"zero",
    1:"one",
    2:"two",
    3:"three",
    4:"four",
    5:"five",
    6:"six",
    7:"seven",
    8:"eight",
    9:"nine"}

digit = input()

try:
    digit = int(digit)
    if digit >= 0:
         print(my_dict[int(digit)])
    else:
        print("not a digit")
except:
    print("not a digit")
