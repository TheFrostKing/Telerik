specials = {
"A":14,
"J": 11,
"Q":12,
"K": 13}
def determine_num(n):
   
    if n in specials:
        return specials[n]
    return int(n)
        
card_type = 4
new_dict = dict([(value, key) for key, value in specials.items()])
n = str(input())

x = 1

while x < determine_num(n):
    x+=1
    if x in new_dict:
        print(f"{new_dict[x]} of spades, {new_dict[x]} of clubs, {new_dict[x]} of hearts, {new_dict[x]} of diamonds")
    else:
        print(f"{x} of spades, {x} of clubs, {x} of hearts, {x} of diamonds")

      