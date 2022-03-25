import datetime
import re
import random
from flask import Flask, render_template, request
from markupsafe import Markup

g_app = Flask(__name__)
g_hist = []


def make_history_text(h_list):
    history_html = ''
    for h in h_list:
        history_html = history_html + h[0] + \
            '\n(USER)' + h[1] + '\n(PC)' + h[2] + '\n'
    return history_html


@g_app.route('/', methods=['GET'])
def index():
    pc = Markup('<b>こんにちは！私の名前はサンプル君です。</b><br/>'
                '質問文を入力して、実行ボタンを押してください。')
    return render_template('sample01.html', sound='normal', face='normal', pc_message=pc, history='', debug_text='開発中')


@g_app.route('/', methods=['POST'])
def output():
    global g_hist
    dt = datetime.datetime.now()
    user = request.form['user_message'].strip()
    pc = Markup('「' + user + '」と入力されました。')
    ft = random.choice(['normal', 'happy', 'sad'])
    g_hist.append(
        (dt.strftime('%Y/%m/%d %H:%M:%S'), user, pc))
    return render_template('sample01.html', sound=ft, face=ft, pc_message=pc, history=make_history_text(g_hist), debug_text=output.__name__)


if __name__ == '__main__':
    g_app.run(host='0.0.0.0', port=5000, debug=True)
