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
