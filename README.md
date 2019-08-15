# SpeechMining_test
スピーチからマイニングする方法を検討

# 設定
環境変数を登録
(gcpにてプロジェクトの作成 -> speech to text のapi連携認証 -> 認証keyのjsonファイルをダウンロード)  
さらに，音声ファイルの置き場所を作る

```bash
export GOOGLE_APPLICATION_CREDENTIALS=[keyとなるjsonのファイル名].json
mkdir resources
```

# テスト
resource以下に音声ファイルを置いておく  
configとして言語や音声ファイルのエンコード方法を設定せねばならない  
speech_test.pyを実行

```bash
python speech_test.py
```
結果が標準出力されているはず

# 参考
[公式ドキュメント](https://cloud.google.com/speech-to-text/docs/)
