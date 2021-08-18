l1=[3,2,4,1]
l2=sorted(l1)
l3=["a","b","c","d"]

sorted_l1=[]
sorted_l3=[]
j=0

for i in l2:
    print(l1.index(l2[j]))
    x=(l1.index(l2[j]))
    sorted_l1.append(l1[x])
    sorted_l3.append(l3[x])
    j=j+1
    
print(l2)
print(sorted_l1)
print(sorted_l3)
