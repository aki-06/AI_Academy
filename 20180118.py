# Python制御構文
# 制御構造

# プログラム処理の流れ
"""
プログラムの処理の流れは上から下へ
"""

# 条件分岐
"""
ある条件に当てはまるかによって処理を分ける
if (条件A):
	条件AがTrueが実行
elif (条件B):
	条件AがFalseかつ条件BがTrueなら実行
else:
	条件Aも条件BもFalseなら実行
"""
score = 80

if score > 70:
	print('合格')

# 条件式の作り方
"""
>...右辺より左辺が大きい
<...右辺より左辺が小さい
>=...左辺が右辺以上
<=...右辺が左辺以上
==...右辺と左辺が等しい
!=...右辺と左辺が等しくない
"""

score = 80

if score > 78:
	print('合格')
else:
	print('不合格')


score = 100

if score == 100:
	print('満点')
elif score >= 80:
	print('合格')
else:
	print('不合格')


# ループ
# for文
"""
for ループ内変数 in リスト名:
	処理
"""
for i in ['apple', 'banana', 'melon']:
	print(i)

# apple
# banana
# melon

"""
forで一定回数の処理をするには、range()関数を使う
range(x)...0からx-1回
range(x, y)...xからy-1回
"""
for i in range(10):
	print(i)

data = [10, 20, 30, 40]
for d in data:
	print(d)

sum_d = 0
for d in data:
	sum_d += d

print(sum_d)

"""
elseを使うとループが終了したら処理が実行される
"""
sum_d = 0
for d in data:
	sum_d += d
else:
	print(sum_d)

# continue...一回スキップ
for i in range(10):
	if i == 3:
		continue
	print(i) # 3がスキップされる

# break...処理が終了
for i in range(10):
	if i == 3:
		break
	print(i) # 2までしか表示されない


f = [1, 2, 3, 4, 5]
for i in f:
	if i == 4:
		print('found')
		break
else:
	print('not found')


for s in 'Hello':
	print(s)

"""
インデックス番号も欲しい時はenumerate()を使う
"""
for index, name in enumerate(['apple', 'banana', 'melon']):
	print(index, name)

# while文
"""
特定条件を満たすまで繰り返す
"""
n = 0
while n < 10:
	print(n)
	n += 1

# フィボナッチ級数を実装してみよう
n = 100
a, b = 0, 1
while a < n:
	print(a, end=' ')
	a, b = b, a + b
print()

# リスト内包表記
"""
既存のリストやジェネレータから新しいリストを作成
"""
result = [x**2 for x in range(1, 11)]
print(result) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# その他内包表記
s = {x**2 for x in range(1, 11)}
print(s) # {64, 1, 4, 36, 100, 9, 16, 49, 81, 25}

d = {x*2: x**2 for x in range(1, 11)}
print(d) # {2: 1, 4: 4, 6: 9, 8: 16, 10: 25, 12: 36, 14: 49, 16: 64, 18: 81, 20: 100}

# 標準入力
print('名前を入力してください')
name = input()
print(name + 'さんですね。')