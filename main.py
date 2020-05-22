from flask import Flask, render_template, request

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
    

if __name__ == '__main__':
    app.run(port=8002)