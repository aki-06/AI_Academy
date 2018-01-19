# 関数
# 関数とは
"""
あるデータを受け取り、関数に定義されている処理を実行し、その結果を返すもの
独自関数、標準関数（組み込み関数）がある
"""

# 関数の定義
"""
def 関数名():
	処理
"""

# 関数の定義
def hello():
	print('hello')

# 関数の呼び出し
hello() # hello


# 関数名
"""
小文字で定義する
単語二文字以上で関数名を定義する時は「_」でつなぐ
予約語、組み込み関数と名前が被らないようにする
"""
def lowercase_underscore():
	print('lowercase_underscore')


# 引数
"""
関数を呼び出すときに関数に与える値
仮引数...関数の定義側で受け取る値
実引数...関数の呼び出し側で与える値
"""

def test():
	print('test')

test() # test


# pass
"""
関数を定義するが処理は何もしない
"""
def test():
	pass


# 引数とリターン
"""
returnを実行すると、関数を終了し、呼び出し元に戻る
def 関数名(引数):
	処理
	return 返り値
"""
def add(a, b):
	return a + b

print(add(2, 4))