# クラスとオブジェクト
# オブジェクト
"""
データ（属性）とメソッドを持ったもの
Pythonの値は全てオブジェクト
オブジェクトには実行できる関数が定義されている
"""

# クラス
"""
データ構造を作る仕組み
クラスを使うと新しいデータ型を作ることができる
クラス名はCamlCase（キャメルケース）にする
インスタンス化...クラスからオブジェクトを作ること
クラスから作ったオブジェクトをインスタンスと呼ぶ
"""
# クラス名の最初の文字は大文字、複数単語の場合は単語の頭文字は大文字
class SampleClass:
	"sample class"

# インスタンス化
sample = SampleClass()
sample.name = 'A'

sample2 = SampleClass()
sample2.name = 'B'

print(sample.name) # A
print(sample2.name) # B

print(type(sample2)) # <class '__main__.SampleClass'>


# コンストラクタ
"""
インスタンスを作成するときに初期値を与える
インスタンスが作成されるときに一度だけ呼ばれる
"""
class User:
	def __init__(self, name):
		self.name = name
		print('コンストラクタが呼ばれました')

	def hello(self):
		print('Hello, ' + self.name)

user = User('sample user') # コンストラクタが呼ばれました
py = User('Python') # コンストラクタが呼ばれました

user.hello() # Hello, sample user
py.hello() # Hello, Python


# メソッドとプロパティ
"""
メソッド...クラスに定義した関数
プロパティ...属性に直接アクセスすることなく、何らかの処理を行い、属性にアクセスする仕組み。@propertyを使う
"""
class SampleClass2:
	def set_name(self, x):
		self.name = x

	def hello(self):
		print('Hello, {0}'.format(self.name))

sample2 = SampleClass2()
sample2.set_name('nemoto')
sample2.hello() # Hello, nemoto


# メソッドのオーバライド
"""
オーバーライド,,,独自の機能で上書きすること
"""
# 基底クラス
class Base:
	def sample(self):
		print('Base.sample()が呼ばれました')

	def test(self):
		print('Base.test()が呼ばれました')

# 派生クラス
class Derived:
	def test(self):
		print('Derived.test()が呼ばれました')

d = Derived()
d.test() # Derived.test()が呼ばれました


# 継承
"""
既存のクラスを元に新しいクラスを作る仕組み
"""
class User:
	def __init__(self, name):
		self.name = name

	def hello(self):
		print('Hello, ' + self.name)

class SuperUser(User):
	def __init__(self, name, age):
		# super()を使うと親クラスのメソッドを呼び出せる
		super().__init__(name)
		self.age = age

	# メソッドのオーバーライド
	def hello(self):
		print('Hello, SuperUser' + self.name)
		super().hello() # Hello, nemoto

a = SuperUser('nemoto', 27)
a.hello() # Hello, SuperUsernemoto


# 例外
"""
プログラムがある処理を実行している途中で、何らかの異常が発生した場合に、
現在の処理を中断し、別の処理を行うこと
"""
# 例外処理の構文
"""
try:
	バグがありそうなプログラム
except:
	バグが起きた時の処理
"""

# 例外オブジェクトを捕捉する
try:
	# バグ1
	i = input()
	input_num = int(i)
	result = 5 / input_num
	print(result)

	# バグ2
	a = 'a'
	b = 5
	print(a + b)

except(TypeError, ZeroDivisionError, KeyError) as e:
	print(type(e))


# else/finally
try:
	print('処理')
except KeyError as e:
	print('KeyError')
except ZeroDivisionError as e:
	print('ZeroDivisionError')
else:
	print('問題はありません')
finally:
	print('処理2')