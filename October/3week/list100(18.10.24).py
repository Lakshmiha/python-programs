lst=[12,120,102,166,52,49]
print(lst)
for a in range(len(lst)):
    if lst[a]>100:
        lst[a]="over"
print("Updated list:",lst)
