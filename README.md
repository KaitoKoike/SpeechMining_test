# SpeechMining_test
スピーチからマイニングする方法を検討

# 環境
macOS Mojave (10.14.6)  
python 3.6.x  


# 設定
## ライブラリの追加


```bash
pip install --upgrade google-cloud-speech
pip install pyaudio
```


## 環境変数の登録とフォルダ作成
(gcpにてプロジェクトの作成 -> speech to text のapi連携認証 -> 認証keyのjsonファイルをダウンロード)  
さらに，音声ファイルの置き場所を作る

```bash
export GOOGLE_APPLICATION_CREDENTIALS=[keyとなるjsonのファイル名].json
mkdir resources
```

# テスト

## 音声ファイルからの音声認識
resource以下に音声ファイルを置いておく  
configとして言語や音声ファイルのエンコード方法を設定せねばならない  
test/speech_test.pyを実行

```bash
python file_test.py
```

結果が標準出力される

## マイクからの音声認識
test/mic_test.pyを実行

```bash
python mic_test.py
```

# 参考
[公式ドキュメント](https://cloud.google.com/speech-to-text/docs/)
