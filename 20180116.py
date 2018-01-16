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
