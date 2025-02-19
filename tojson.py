import os
import re
import json
import glob
import argparse

def split_into_sentences(text):
    """
    正規表現を用いて、文章を文末の句点(. ! ?)で分割
    """
    sentences = re.split(r'(?<=[.!?])\s+', text)
    # 空文字列になってしまう部分を除去
    return [s.strip() for s in sentences if s.strip()]

def process_files(directory, label):
    """
    指定ディレクトリ内の全てのテキストファイルを処理して各文章に指定されたラベルを付与してリストにまとめる
    """
    data = []
    # 指定ディレクトリ内の .txt ファイルを全て取得
    txt_files = glob.glob(os.path.join(directory, '*.txt'))
    
    for file_path in txt_files:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            sentences = split_into_sentences(content)
            for sentence in sentences:
                data.append({
                    "text": sentence,
                    "label": label
                })
    return data

def main():
    parser = argparse.ArgumentParser(
        usage="tojson.py [DIRECTORY_PATH] [--label LABEL] [--output OUTPUT_FILE_PATH]"
    )
    parser.add_argument("DIRECTORY_PATH", help="ICNALE_data")
    parser.add_argument("--label", type=int, default=0, help=0) # 0: non-native, 1: native
    parser.add_argument("--output", default="output.json", help="output.json")
    args = parser.parse_args()
    
    # 全テキストファイルの文章を取得
    data = process_files(args.directory, args.label)
    
    # JSON ファイルとして保存
    with open(args.output, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    
    print(f"{len(data)} sentences successfully saved in json format")

if __name__ == "__main__":
    main()

