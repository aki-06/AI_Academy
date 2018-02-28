# コメント

print("Hello world")

"""
コメント
"""

print(10)
print(10 + 5) # 足し算
print(10 - 5) # 引き算
print(10 * 5) # 掛け算
print(10 / 5) # 割り算
print(10 % 3) # 余り

print("10 + 5") # 文字列
print(10 + 5) # 数値

"""
変数とは、データを入れておく箱のようなもの
「変数名 = 値」で定義する。右辺を左辺に代入する
変数で使用できるのは、アルファベット、数字(先頭は不可)、「_」
"""
name = 'Tom'
age = 20

print(name) # Tom
print('name') # name


"""
変数は値を上書きすることができる
"""

x = 10
print(x) # 10

x = 20
print(x) # 20

"""
省略形でも書ける
"""
x = x + 5
x += 5


"""
文字列の連結
「+」で文字列を連結できる
"""
print("Hello " + "world")

name = "Tom"
print("My name is" + name)