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

