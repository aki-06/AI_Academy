# 変数
# データを保存する箱
lang = 'Python' # langという変数に文字列'Python'を代入
x = 5 # xという変数に5という数値を代入

# 大文字と小文字は区別される
var = 'var'
Var = 'Var'

print(var)
print(Var)

# 二単語繋げる場合は「_」で繋げる
hello_world = 'Hello World'
print(hello_world)


# 定数
"""
定数は値が変えられない変数
Pythonに定数はないため、定数のような意図を持って定義する場合には、すべて大文字で変数名を定義する
"""


# 予約後
"""
関数名や変数名に使用できない単語
予約語を用いるとSyntax Errorになる
"""
print(__import__('keyword').kwlist) # 予約語一覧を出力
# ['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']


# 変数と型
"""
Pythonの変数には型宣言がないため、変数にどのような型でも入れることができる
"""
x = 5
print(x) # 5
x = 'Python'
print(x) # Python