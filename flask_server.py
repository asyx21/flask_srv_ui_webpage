#!user/bin/env python3

from flask import Flask, render_template

app = Flask(__name__)

#def restart():
#    global app
#    app = Flask(__name__, template_folder="templates" )

@app.route('/')
def index():
    title = "Bienvenu sur ryben network"
    return render_template('index.html', index_title = title)


@app.route('/test')
def test():
    return 'ceci est un test'


@app.route('/show')
def show():
    dict = {'phy': 50, 'che': 60, 'maths': 70}
    print(dict)
    return render_template('show.html', result=dict)

if __name__ == '__main__':
   app.run(debug = True)
