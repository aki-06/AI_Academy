# Pythonの型
## 数値型

"""
・整数(int)
・少数、実数(float)
・複素数
"""

i = 0
i += 1
print(i) # 1

"""
以下は同じ
i = i + 1
i += 1
"""

print(10 - 2) # 8
print(10 * 2) # 20
print(10 // 3) # 3
print(10 % 3) # 1
print(10 ** 3) # 1000

"""
/...小数点が返ってくる
//...切り捨て
"""
print(5 // 2) # 2
print(5 / 2) # 2.5


## 文字列
print('I love ' + 'Python') # I love Python
print('Hello' * 3) # HelloHelloHello
print('I say ' + ('hello' * 3)) # I say hellohellohello

x = 'I'
y = 'love'
z = 'Python'
print(x + y + z) # IlovePython
