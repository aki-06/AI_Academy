# 引数のデフォルト値
"""
関数では引数を設定しなかった場合の引数を設定できる
"""

def func(a, b=5):
	print(a)
	print(b)

# bの引数を指定しないと、デフォルトの5が出力される
func(3) # 3と5が出力される

# bを指定すると指定した値が出力される
func(3, 10) # 3と10が出力される

def sample(arg):
	arg_list=[]
	arg_list.append(arg)
	print(arg_list)

sample('python')
sample('Python')


# 名前付き引数の指定
"""
引数を指定するときに、引数の名前を指定して関数を呼び出すことができる
キーワード引数ともいう
"""
def height_and_weight(height, weight):
	print('身長は' + str(height) + 'cmです')
	print('体重は' + str(weight) + 'kgです')

# 引数の名前を指定する
height_and_weight(height=170, weight=60)
# 身長は170cmです
# 体重は60kgです

