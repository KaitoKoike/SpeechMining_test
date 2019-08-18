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
    if queue.__len__()>0:
        content = queue.pop()
        speaker = content["speaker"]
        text = content["text"]
        #*
        # この辺でゴチャゴチャする予定
        knp_result = knp.parse(text)
        out = ""
        for bnst in knp_result.bnst_list(): # 各文節へのアクセス
            out += "\tID:%d, 見出し:%s, 係り受けタイプ:%s, 親文節ID:%d, 素性:%s" \
                    % (bnst.bnst_id, "".join(mrph.midasi for mrph in bnst.mrph_list()), bnst.dpndtype, bnst.parent_id, bnst.fstring)
            out += "\n"
        # 
        # 
        # 
        # #
        result = {"speaker":speaker,"text":out,"status":True}
        print(result)
        return jsonify(ResultSet=result)
    
    else:
        result = {"speaker":None,"data":None,"status":False}
        return jsonify(ResultSet=result)

if __name__ == '__main__':
    print("start server")
    app.run(host="0.0.0.0", port=8000, debug=True)