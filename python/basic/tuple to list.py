mytuple=('p','q','r')
mylist=list(mytuple)
mylist[0]='x'
print(mylist)
mytuple=tuple(mylist)
print(mytuple)
