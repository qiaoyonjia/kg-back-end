# app.py

from flask import Flask, request
from flask_cors import CORS  # 支持跨域
from api.er_post import get_er_res

app = Flask(__name__)

CORS(app)


@app.route('/er_post', methods=['GET'])
def er_post():
    # 获取前端传过来的参数
    text = request.args.get('text')
    return get_er_res(text)


if __name__ == '__main__':
    app.run(debug=True)
