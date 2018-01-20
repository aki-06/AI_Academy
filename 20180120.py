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