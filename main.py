from flask import Flask, render_template, request
import requests

app = Flask(__name__)
# @app.route('/test/')
# def text():
#     return render_template('test.html')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/test/<int:num>/')
def fun1(num):
    return render_template('{}.html'.format(num), num=num)


@app.route('/test/<int:num>y/')
def fun２(num):
    print(num)
    return render_template('{}y.html'.format(num), num=num)


@app.route('/test/about/')
def about():
    return render_template('about.html')
    

@app.route('/test/others/')
def fun_others():
    return app.send_static_file(filename='others.html')


@app.route('/test/test/', methods=['POST', 'GET'])
def test():
    code = None
    if request.method == 'POST':
        code = request.form['code']  # 提取代码
        result = fun(code)  # 计算结果
        return render_template('test.html', result=result, code1=code)
    else:
        if code is None:
            code = '#!/usr/bin/python\nprint("Hello, World!")'
        return render_template('test.html', code1=code)


def fun(code):
    url = 'https://api.toolnb.com/RunCode/Api/sendRunCode.html'
    headers = {
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://www.toolnb.com',
        'referer': 'https://www.toolnb.com/dev/runCode.html',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
         AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
    }
    data = {
        'code_type': 'python:3',
        'code': code,
        'name': ''

    }
    response = requests.post(url, data=data, headers=headers)
    # print(response)
    # print(response.json())
    data = response.json()['data']['result']
    return data


if __name__ == '__main__':
    app.run(port=8002)