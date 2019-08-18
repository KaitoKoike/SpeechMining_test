# これはクライアントの挙動が正しいのかを判定するプログラム
# マイクを用いてはいないが，実際はマイクから得られた結果を用いる
# 構文解析に多少のラグがあるので非同期での通信を想定
# マイクから構文解析のサーバーにひたすら送るクライアント(マイク側)
# 構文解析からの結果をひたすら受け取るクライアント(生徒の意見集約側)
# ２つができる
# 
# しかし，今回は１つの中でしか行っていない．．．#

import requests
import json

def main():
    base_server_url = "http://0.0.0.0:8000/"

    #イニシャライズは一回だけ
    res = requests.post(base_server_url+"init",data="please")
    print(json.loads(res.text))


    data = {"speaker":1,"text":"地球温暖化は二酸化炭素が原因だよ"}
    res = requests.post(base_server_url+"appendText",json=data)
    print(json.loads(res.text))

    data = {"speaker":1,"text":"二酸化炭素を減らすにはどうすればいいかな？"}
    res = requests.post(base_server_url+"appendText",json=data)
    print(json.loads(res.text))


    while(True):
        res = requests.post(base_server_url+"getResult",data="True")
        contents = json.loads(res.text)["ResultSet"]

        if contents["status"] == True:
            print(contents["text"])
        else:
            print("queにtextがないよ")
            break
if __name__ == "__main__":
    main()