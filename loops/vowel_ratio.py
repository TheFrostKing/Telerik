lines = int(input())
store_food = {}
food_lst = []
lst_from_dict = []
temp = 0


def calc_ratio(food_lst):
    for food in food_lst:
        sum_vowels = sum(food.count(x) for x in 'aeiou')
        if sum_vowels <= 0:
            break
        word_len = len(food)
        ratio = sum_vowels / word_len
        store_food[food] = ratio

def occur_in_dict():
    occur = list(store_food.values())
    a = (list(set([i for i in occur if occur.count(i) > 1])))
    povtarqshti_vowels = []
    biggest_lett = 0
    most_vowels = 0
    best_word = ''

    for x in a:
        povtarqshti_vowels = [key for key in store_food if store_food[key] == x]
    for x in povtarqshti_vowels:
        sum_vowels = sum(povtarqshti_vowels.count(x) for x in 'aeiou')
        if most_vowels < sum_vowels:
            povtarqshti_vowels.append(x)
            most_vowels = sum_vowels
    
    if len(povtarqshti_vowels) > 1:
        for x in povtarqshti_vowels:
            if len(x) > biggest_lett:
                best_word = x
                biggest_lett = len(x)  

        summed = sum(best_word.count(x) for x in 'aeiou')
        return print(f"{best_word} {summed}/{len(best_word)}")
    else:
        print(f"{povtarqshti_vowels} {most_vowels}/{len(povtarqshti_vowels)}")
    
'''MAIN LOOP'''
for x in range(lines):  
    food = str(input())
    food_lst.append(food)
    
    calc_ratio(food_lst)
    lst_from_dict = list(store_food.values())


if lst_from_dict == []:
    word = max(food_lst)
    summed = sum(word.count(x) for x in 'aeiou')
    print(f"{word} {summed}/{len(word)}")

else:
    get_min = min(store_food.values())
    if lst_from_dict.count(get_min) > 1: # look for multiple occurances
            occur_in_dict()

    else: 
        res = [key for key in store_food if store_food[key] == get_min] # print min value
        word = res[0]
        summed = sum(word.count(x) for x in 'aeiou')
        print(f"{word} {summed}/{len(word)}")



        

lines_of_input = int(input())

best_ratio = 1.1
best_vowels = 0
best_length = 0
best_food = ''
for x in range(lines_of_input):
    food = input()
    vowels = 0
    length = len(food)
    for letter in food:
        if letter in 'aoeui':
            vowels += 1

    ratio = vowels / length
    if ((ratio < best_ratio)
        or (ratio == best_ratio and vowels > best_vowels)
            or (ratio == best_ratio and vowels == best_vowels and length > best_length)):
        best_ratio = ratio
        best_vowels = vowels
        best_length = length
        best_food = food


print(f'{best_food} {best_vowels}/{best_length}')