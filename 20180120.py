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


# 関数における引数の * と **
"""
仮引数（関数定義側）に*を使うと、可変個の位置引数をタプルにまとめる
**を使うと、キーワード引数が辞書にまとめる
*と**を併用する場合には*を先に書く
"""

def sample1(*args):
	print(args)

sample1(1, 2, 3, 'Python') # (1, 2, 3, 'Python')

# *で定義した仮引数よりも後ろはキーワード引数としてのみ使える

def concat(*args, sep='/'):
	return sep.join(args)

print(concat('a', 'b', 'c')) # a/b/c
print(concat('a', 'b', 'c', sep='|')) # a|b|c


def sample2(**args):
	print(args)

sample2(name='nemoto', age=27, job='engineer') # {'name': 'nemoto', 'age': 27, 'job': 'engineer'}


# グローバル(global)宣言
"""
ローカル変数（関数定義の内部で定義した変数）
グローバル変数（関数定義の外部で定義した変数）
"""
glb = 0

def func1():
	glb = 1

def func2():
	global glb
	glb = 5

print(glb) # 0
func1()
print(glb) # 0
func2()
print(glb) # 5
