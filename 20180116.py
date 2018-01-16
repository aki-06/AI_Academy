# リスタ内包表記
"""
ループと条件文を使って新しいリストを生成する
"""
li = [i for i in range(10) if i % 2 == 0]
print(li) # [0, 2, 4, 6, 8]

nums = [10, 99, 23, 55, 1]
# ソートする
nums.sort()
print(nums) # [1, 10, 23, 55, 99]

# 逆順
nums.reverse()
print(nums)

day = '2018/01/16'
print(day.split('/')) # ['2018', '01', '16']

a = ['a', 'b', 'c']
print('-'.join(a)) # a-b-c

li = ['A', 'B', 'C', 'D', 'E']
print(','.join(li)) # A,B,C,D,E

li2 = ['ABC', 'DEF', 'GHI']
sep = '*'
joined = sep.join(li2)
print(joined) # ABC*DEF*GHI

sep = joined.split(sep)
print(sep) # ['ABC', 'DEF', 'GHI']

lists = ['A', 'B', 'C', 'D', 'E']
lists.insert(1, 'Z')
print(lists) # ['A', 'Z', 'B', 'C', 'D', 'E']


# リストのコピーの種類
li1 = [1, 2, 3]
li2 = li1
print(li1) # [1, 2, 3]
print(li2) # [1, 2, 3]

li1[2] = 10
print(li1) # [1, 2, 10]
print(li2) # [1, 2, 10]

# deepcopy()メソッド

import copy
li1 = [1, 2, 3]
li2 = copy.deepcopy(li1)
print(li1) # [1, 2, 3]
print(li2) # [1, 2, 3]

li1[2] = 10
print(li1) # [1, 2, 10]
print(li2) # [1, 2, 3]


# タプル
"""
イミュータブル(不変)
格納する値は自由
初めから変更しない値を入れる
リストより高速
"""

ai_a = ('ai', 'academy', 2018)
print(ai_a) # ('ai', 'academy', 2018)

t = (2, 5, 8)
print(len(t)) # 3
print(t * 3) # (2, 5, 8, 2, 5, 8, 2, 5, 8)

# タプルとリストの変更
a = (1, 2, 3)
b = list(a)
print(b) # [1, 2, 3]
c = tuple(b)
print(c) # (1, 2, 3)


# セット集合型
"""
setは順序は保持せず、ユニークなオブジェクトのグループを保持する
格納するオブジェクトは問わないが、リストは追加できない
"""

# セットの操作
x = {1, 2, 'ab'}
x.add(3)
print(x) # {1, 2, 3, 'ab'}
# removeは指定されたオブジェクトがあればsetから取り除く。なければエラー。
x.remove(3)
print(x) # {1, 2, 'ab'}
# discardは要素があった場合だけ取り除く。
x.discard(2)
print(x) # {1, 'ab'}
x.discard('python')
print(x) # {1, 'ab'}