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


# インデックスのアクセス
d = {'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}
print(d['k1']) # v1
print('k1' in d) # True
print('k4' in d) # False


# 辞書型のイテレーションアクセス
d = {'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}
for i in d:
	print(i)

# k1
# k2
# k3


# キーと値はdel文で削除可能
"""
delは値を返さない
popは値を返す
"""
d = {'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}
d['k4'] = 'v4'
print(d) # {'k1': 'v1', 'k2': 'v2', 'k3': 'v3', 'k4': 'v4'}

d = [1, 2, 3, 4, 5]
del d[1]
print(d) # [1, 3, 4, 5]
deleted = d.pop(2)
print(deleted) # 4
print(d) # [1, 3, 5]
del d[0:2]
print(d) # [5]
