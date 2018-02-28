# スライス
"""
リストからサブリストを得るためのシンタックスで、サブリストはリストの開始位置と終了位置までの要素のリスト
"""

li = [3, 5, 10.0, 'a', 'b']

print(li[0:2]) # [3, 5]
print(li[0:-2]) # [3, 5, 10.0]
print(li[-3:-1]) # [10.0, 'a']

# スライスの指定がマッチしなかった場合はからの配列が返る
print(li[-7:-6]) # []

"""
[:]は先頭から末尾までのシーケンス全体を抽出
[start:]は先頭から末尾まで
[:end]は先頭から末尾-1まで
[start:end]はstartからend-1まで
[start:end:step]はstepごとに、startからend-1まで
"""

print(li[1:]) # [5, 10.0, 'a', 'b']
print(li[:-1]) # [3, 5, 10.0, 'a']
print(li[:]) # [3, 5, 10.0, 'a', 'b']


# リストの更新
li = []
li = ['Python']
print(li) # ['Python']
li.append('PHP')
print(li) # ['Python', 'PHP']
li.remove('Python')
print(li) # ['PHP']
del li[0]
print(li) # []

li = [1, 2, 3, 4 ,5]
li[1:4] = ['Python']
print(li) # [1, 'Python', 5]