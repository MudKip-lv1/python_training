#論理演算子：(logical operator)
# and, or, not
# and: 両方がTrueの場合にTrue
# or: どちらかがTrueの場合にTrue
# not: TrueとFalseを反転させる

a = 1
b = 1
c = 10
d = 100
print(a is b) #True

print(a == b and c > d)
print (a == b or c > d)

age = 10
height = 120
print(age >= 10 and height >= 110)

phd = True
exp_year = 5
print(phd or exp_year >= 5)