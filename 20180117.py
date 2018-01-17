# 辞書型
"""
keyとvalueのペアを保持する型
順序が保証されない
{key1:value1, Key2:value2}
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

