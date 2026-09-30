# calculate the product by multiplying all the elements of a given tuple
tuple1=(1,2,4,6,8,9,8,8)
i=1
for x in tuple1:
    i*=x
    print("intermediate values",i)
    print("the final product value",i)
