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