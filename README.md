# 鬼畜ロbot

Python (`discord.py`) で作った、鬼畜ロbotのコラ画像生成器です。  
ちっこすぎてリポジトリにするまでもない。参考用資料として。

このリポジトリには、著作権的な問題がありそうなので  
画像素材となるファイルは用意していません。ご自身でどうぞ。

## 下準備

実行するには、以下の手順に従ってください。

1. 仮想環境を作成し移動する（任意）
1. `requirements.txt` 内のパッケージをインストールする（例: `pip install -r requirements.txt`）
1. `.env-template`を`.env`にコピーし、`TOKEN`を設定する
1. 任意の画像素材を`image.png`として用意する
1. `main.py`の14行目を用意した画像にあわせて調整する
1. `main.py`を実行する（例: `python main.py`）

## フォント

生成に用いるフォントとして、Noto Sans JP Regularを用いています。  
必要に応じて`font.ttf`を置き換えてください。
