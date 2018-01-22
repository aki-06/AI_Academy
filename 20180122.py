# テキストファイルの読み書き
# ファイル読み書きの決まりごと
"""
fileを開く...open()
ファイルを読む...read()
ファイルに書き込む...write()
ファイルを閉じる...close()

r...読み込みモード
w...書き込みモード
a...追加書き込みモード

readline()...一行読み込み
readlines()...すべての行をリストとして読み込み
"""

f = open('test.txt', 'w')
f.write('hello')
f.close()


# ファイルを読み込んで見よう
fileobj = open('test.txt', 'r')
print(fileobj.read())
fileobj.close()


# 例外処理と合わせて使う
sample_file = open('sample.txt', 'a')
try:
	sample_file.write('sample01\n')
	sample_file.write('sample02')
finally:
	sample_file.close()