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


# 関数 変数のスコープ
var1 = 'グローバル変数'

def sample3():
	var2 = 'ローカル変数'
	return (var1, var2)

print(sample3()) # ('グローバル変数', 'ローカル変数')


var1 = 'グローバル'

def sample4():
	global var1
	var1 = 'ローカル'
	var2 = 'ローカル'
	return(var1, var2)

print(sample4()) # ('ローカル', 'ローカル')


# よく利用される標準関数
"""
zip()
引数に渡したそれぞれのリストは、要素をタブルでまとめたリストで返される
"""

a = [1, 2, 3]
b = [4, 5, 6]
z = zip(a, b)
print(z) # <zip object at 0x104515348>
print(list(z)) # [(1, 4), (2, 5), (3, 6)]

questions = ['name', 'favorite food']
answers = ['nemoto', 'sushi']

for q, a in zip(questions, answers):
	print('what is your {0}? it is {1}'.format(q, a))
	# what is your name? it is nemoto
	# what is your favorite food? it is sushi

"""
map()
リストの要素に演算を適用する
"""
def square(x):
	return x * x

li = list(map(square, range(1, 10)))
print(li) # [1, 4, 9, 16, 25, 36, 49, 64, 81]

"""
filter()
リストの要素を抽出する
"""
def is_mod(x):
	return x % 3 == 1

li = list(filter(is_mod, range(1, 10)))
print(li) # [1, 4, 7]


# 再帰関数
"""
自分自身を呼び出す関数
"""
def count_down(i):
	print(i)
	if i > 0:
		count_down(i-1)
	else:
		return

count_down(10)


def factrial(i):
	if i == 0:
		return 1
	else:
		return i * factrial(i - 1)

print(factrial(4))


# 無名関数
"""
名前のない関数
lambdaを使う
変数 = lambda 引数1,引数2:式
"""
# iを2倍にする無名関数
sample = lambda i: i * 2
print(sample(10)) # 20
print(sample(100)) # 200


def sample5(func):
	return func(10)

print(sample5(lambda i:i * 2)) # 20
