# Pythonの型
# リスト型

"""
リスト型は複数のデータを管理できる
格納する型の定義は必要ない
配列名 = ['x', 'y', Z]で定義する
変更可能
"""

list1 = [1, 2, 3]
print(list1) # [1, 2, 3]

list2 = ['I', 'love', 'python']
print(list2[2]) # python

list3 = [[1, 2], ['A', 'B']]
print(list3) # [[1, 2], ['A', 'B']]

print(list3[1][1]) # B

# 値を書き換える
list2[2] = 'PHP'
print(list2) # ['I', 'love', 'PHP']

list2[2] = 'python'
print(list2) # ['I', 'love', 'python']

print('python' in list2) # True

# 9までのリストを作成
print(list(range(10))) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 3から9までのリストを作成
print(list(range(3, 10))) # [3, 4, 5, 6, 7, 8, 9]

# 3から9まで2飛ばしのリストを作成
print(list(range(3, 10, 2))) # [3, 5, 7, 9]


"""
配列の長さを取得するlen(x)
オブジェクトのindexを取得するindex(x)
配列にオブジェクトを追加するappend(x)
配列からオブジェクトを削除するdel
"""

list1 = list(range(5))
print(list1)

print(len(list1)) # 5
print(list1.index(3)) # 3
list1.append(5)
print(list1) # [0, 1, 2, 3, 4, 5]
del list1[2]
print(list1) # [0, 1, 3, 4, 5]

"""
ネガティブインデックス
リストの逆からも参照できる
"""
li = [3, 10, 'Hello', 'Python']
print(li[-2]) # 'Hello'

s = 'abcdefg'
print(len(s)) # 7

# cの位置を探す
print(s.find('c')) # 2

print(s[2]) # c

# [start:end]でendのひとつ前まで出力
print(s[1:4]) # bcd

print(s[2:-1]) # cdef

"""
入れ子にすることも可能
"""
a = ['a', 'b', 'c']
b = ['d', 'e', 'f']
c = [a, b]

print(c) # [['a', 'b', 'c'], ['d', 'e', 'f']]
print(c[0][1]) # b
