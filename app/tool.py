# -*- coding: utf-8 -*-
import sys

args = sys.argv
args_index = 1

input_file = args[args_index]  ; args_index = args_index + 1 ;

# 入力ファイル読み込み
with open(input_file, mode='r', encoding='utf-8') as reader:
    for item in reader.read().splitlines():
        while '  ' in item:
            item = item.replace('  ', ' ')
        item = item.strip().replace(' ',',')
        print(item)
