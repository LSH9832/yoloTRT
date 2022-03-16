from flask import Flask, request
import json

app = Flask(__name__)


@app.route("/detect_result", methods=["POST"])
def receive_detect_result():
    params = request.data.decode()
    p = json.loads(params)["outputs"]
    count = {}
    for obj in p:
        if not obj['label'] in count:
            count[obj['label']] = 1
        else:
            count[obj['label']] += 1

    print("total:", len(p), count)
    return ""


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=12345)