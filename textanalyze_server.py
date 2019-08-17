from flask import Flask, request, jsonify, url_for
from pyknp import KNP
import json
from collections import deque

app = Flask(__name__)

# 構文解析，形態素解析のツールを初期化
@app.route("/init",methods=["POST"])
def init():
    r = request
    print(r.data)
    global knp 
    knp = KNP()
    global queue
    queue = deque()

    result = {"text":"init done"}
    return jsonify(ResultSet=result)

@app.route("/appendText",methods=["POST"])
def appendText():
    r = request
    print(r.data)
    content = json.loads(r.data)
    queue.appendleft(content)
    print(queue)
    result = {"text":"successfuly got text"}
    return jsonify(ResultSet=result)

@app.route("/getResult",methods=["POST"])
def analyze():
    r = request
    flag = r.data
    #何か文字列があれば実施
    if flag:
        content = queue.pop()
        speaker = content["speaker"]
        text = content["text"]
        #*
        # この辺でゴチャゴチャする予定
        # 
        # 
        # 
        # 
        # *#
        result = {"speaker":speaker,"data":"君が好き"}
        print(result)
        return jsonify(ResultSet=result)

if __name__ == '__main__':
    print("start server")
    app.run(host="0.0.0.0", port=8000, debug=True)