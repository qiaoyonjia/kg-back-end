# app.py

from flask import Flask, request
from flask_cors import CORS  # 支持跨域
from api.er_post import get_er_res
from api.relation_view import get_er
from api.question_answering import get_ques_res
from api.chat_glm import get_chat_res


app = Flask(__name__)

CORS(app)

@app.route('/er_post', methods=['GET'])
def er_post():
    # 获取前端传过来的参数
    text = request.args.get('text')
    return get_er_res(text)

@app.route('/search_entity', methods=['GET'])
def search_relation():
    # 获取前端传过来的参数
    text = request.args.get('text')
    return get_er(text)

@app.route('/question_answering', methods=['GET'])
def question_answering():
    # 获取前端传过来的参数
    text = request.args.get('text')
    return get_ques_res(text)


@app.route('/chatglm_answering', methods=['GET'])
def chatglm_answering():
    # 获取前端传过来的参数
    text = request.args.get('text')
    return get_chat_res(text)


if __name__ == '__main__':
    app.run(debug=True)
