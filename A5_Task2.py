a=[1,2,3,4,5,6,7,8,9,10]
b=a[0:5]
print("Original List:",a)
print("Extracted First five Elements",b)
c=b.copy()
c.reverse()
print("Reversed Extracted elements:",c)
