profit=[5,		10,		15,		7,		8,		9,		4]
weight=[1,		3,		5,		4,		1,		3,		2]
items=len(weight)
p_by_w=[(profit[i]/weight[i],i) for i in range(items)]
print(p_by_w)
x=[0]*items
#x=[0,0,0,0,0,0]
max=0
price=0
p_by_w.sort(reverse=True, key=lambda x: x[0])
for key,i in p_by_w:
    if max+weight[i]<=15:
        price+=profit[i]
        x[i]=1
        max+=weight[i]
sorted_p_by_w = [key for key, i in p_by_w]
print(sorted_p_by_w)
print(x)
print(price)