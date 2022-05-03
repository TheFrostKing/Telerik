my_dict = {
2000:"Dragon",		
2001:"Snake",		
2002:"Horse",		
2003:"Sheep",	
2004:"Monkey",		
2005:"Rooster",
2006:"Dog",
2007:"Pig",
2008:"Rat",
2009:"Ox",
2010:"Tiger",
2011:"Hare"
}

key_list = list(my_dict.keys())

year = int(input())

if year < max(key_list):
    while year not in my_dict:
        year+=12
        
else:
    while year not in my_dict:
        year-=12

print(my_dict[year])