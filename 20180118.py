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
