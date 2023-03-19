num_set={"res"}
product=0
for a in range(2,101):
    for b in range(2,101):
        product=a**b
        num_set.add(product)
print(len(num_set)-1)       