price = float(input())
paid = float(input())
change = paid-price

result = []
total = {}
values = {
    1.0:"1 lev",
    0.5:"50 stotinki",
    0.2:"20 stotinki",
    0.10: "10 stotinki",
    0.05: "5 stotinki",
    0.02:"2 stotinki",
    0.01: "1 stotinka"
}
key_list = list(values.keys())
position = 0
while change > 0:

    if change >= key_list[position]:
        change = round(change - key_list[position],2)
        result.append(key_list[position])
        continue
    position += 1

for x in result:
    if x not in total:  
        total[x] = result.count(x)
sorted_total = sorted(total, reverse=True)

for r in sorted_total:
    print(f"{total[r]} x {values[r]}")


