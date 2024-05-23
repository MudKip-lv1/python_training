# #数値型(Numeric): intger, float, complex

# #int(integer, 整数) -3, -2, -1, 0, 1, 2, 3, 100
# print(type(-100))

# # float(浮動小数点) 3.14, 0.0, -2.5
# print(type(3.14))

# #complex(複素数) 1+2j, 1-2j
# #複素数とは、実数部と虚数部を持つ数のこと
# print(type(1+2j))

#numeric operation(数値演算)
#四則演算
#加算
a = (1+2)
print(a)

b = (2 * 4)
print(b)

result = (1 + 1.0)
print(result, type(result))

#floor division(切り捨て除算)
result2 = (7 // 5)
print(result2)

#modulus(剰余)
result3 = (7 % 5)
print(result3, type(result3))

#exponentiation(累乗)
result4 = (2 ** 3)
print(result4)

hit_point = 100
damage = 20
hit_point = hit_point - damage
print(f"rest hit point is {hit_point}.")

#augmented assignment(複合代入)
hit_point = 100
damage = 20
hit_point -= damage
print(f"rest hit point is {hit_point}.")