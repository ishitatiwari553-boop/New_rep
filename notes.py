set = {1,0,True,False,1,0,False,True}

print(set)

for i in set:
  if i == 1:
    print("yes")
  else:
    print("no")


set ={[1,2,3,4]}
print(set)

c1 = 2 + 4j
c2 = 3 + 5j
sum_complex= c1+c2
print("sum= ",sum_complex)
product_complex= c1*c2
print("product= ",product_complex)
print("imaginary_part = " , product_complex.imag)


a= 5
b= 7
(b,a)=(a,b)
print(a)
print(b)

a = 5
b = 7
c = a
a = b
b = c
print(a)