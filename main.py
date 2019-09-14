from pathlib import Path
import csv
from pykakasi import kakasi
import mojimoji

kakasi = kakasi()

kakasi.setMode('H', 'a')
kakasi.setMode('K', 'a')
kakasi.setMode('J', 'a')

conv = kakasi.getConverter()


# CSVファイルを開く
csv_file = open("./japanese.csv", "r")

romaji_list = []
for row in csv.reader(csv_file):
            word = mojimoji.han_to_zen(row[1],ascii=False)
            romaji_list.append(conv.do(row[1])) 

# 最初の行を削除
del romaji_list[0]

# テキストに書き込み
text = ""
for word in reversed(romaji_list):
    text += word
    text += "\n"

#書き込む
a_file = open(Path("./romaji.txt"),"w")
a_file.writelines(text)
a_file.close()