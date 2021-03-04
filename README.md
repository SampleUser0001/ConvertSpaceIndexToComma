# ConvertSpaceIndexToComma
スペースのインデックスをカンマに変換する

## 使用方法

docker-compose.ymlファイルを用意し、volumesとenvironmentを指定する。

``` yml
version: '3'
services:
  node:
    image: ittimfn/convert_space_index_to_comma:latest
    container_name: converter
    volumes:
      - ./files:/files                 # 入力/出力ファイルのファイルパス
    environment: 
      - input_file=/files/input.txt    # 入力ファイルのパス(コンテナ内のパスを指定する。)
      - output_file=/files/output.txt  # 出力ファイルのパス(コンテナ内のパスを指定する。)
```

### 実行

```
docker-compose up -d
```

## 開発用コマンド

### 実行

```
docker-compose -f docker-compose_develop.yml up
```
