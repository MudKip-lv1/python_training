#is演算子：同じオブジェクトかどうかを判定する
# ==演算子：同じ値かどうかを判定する
a = 1
b = 1
print(a is b) #True

a = [1, 2, 3]
b = [1]
print(a is b) #False
print(id(a),id(b)) #id()でオブジェクトのアドレスを取得できる

hello = "hello"
hello2 = "h" + "e" + "l" + "l" + "o"
print(hello is hello2) #True

#Noneかどうかを判定する
nothing = None
print(nothing is None) #True
print(nothing is not None) #False