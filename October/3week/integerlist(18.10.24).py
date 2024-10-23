intg_list1=[2,5,4,10]
intg_list2=[2,5,4,23]
intg=[]
Sum1=sum(intg_list1)
Sum2=sum(intg_list2)
Len1=len(intg_list1)
Len2=len(intg_list2)

if(len(intg_list1)==len(intg_list2)):
    print("Lengths are same",Len1,Len2)
else:
    print("Not same",Len1,Len2)

if(sum(intg_list1)==sum(intg_list2)):
    print("Sums are equal",Sum1,Sum2)
else:
    print("not equal",Sum1,Sum2)
    

common_values=set(intg_list1)&set(intg_list2)
if common_values:
    print("Common values:",common_values)
else:
    print("No common values")

