import os

from flask import Flask, request, render_template, redirect

app = Flask(__name__)


@app.route('/gallery', methods=['POST', 'GET'])
def galery():
    title = 'Красная планета'
    pictures = os.listdir('static/img')
    if request.method == 'GET':
        return render_template('gallery.html', pictures=pictures, title=title, lnp=len(pictures))
    elif request.method == 'POST':
        f = request.files['file']
        with open(f'static/img/{len(pictures) + 1}.jpg', 'wb') as file:
            file.write(f.read())
        return redirect('/gallery')


@app.route('/')
def index():
    return redirect('/gallery')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
