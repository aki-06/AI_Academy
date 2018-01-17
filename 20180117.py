# 辞書型
"""
keyとvalueのペアを保持する型
順序が保証されない
{key1:value1, Key2:value2}
存在しないキーを参照するとエラーになる
"""
dic = {}
dic = {'a':1, 'b':2, 'c':3}

print(dic) # {'a': 1, 'b': 2, 'c': 3}

# 値を追加
dic['d'] = 4
dic['e'] = 5
dic['f'] = 6

print(dic) # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}

# 値を上書き
dic['a'] = 0

print(dic) # {'a': 0, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}


# 辞書の操作
dic = {'nemoto': 27, 'aiacadmy': 1}
print(dic) # {'nemoto': 27, 'aiacadmy': 1}

# valueを取得する
# 辞書型[key]
print(dic['nemoto']) # 27

# 値の追加(更新)
dic['nemoto'] = 28
print(dic['nemoto']) # 28

# 値の削除
del dic['nemoto']
print(dic) # {'aiacadmy': 1}

# setdefault
d = {}
print(d.setdefault('name', 'nanashi')) # nanashi
print(d) # {'name': 'nanashi'}
d = {'name': 'nemoto'}
print(d.setdefault('name', 'nanashi')) # nemoto

# getメソッド
# 指定されたキーの値を取得
dic = {'nemoto': 27, 'tanaka': 29, 'yamada': 30}
print(dic.get('nemoto')) # 27
print(dic.get('sato', 19)) # 19

# 元の辞書に影響はない
print(dic) # {'nemoto': 27, 'tanaka': 29, 'yamada': 30}
