#!user/bin/env python3

from flask import Flask, render_template, jsonify, request, make_response

app = Flask(__name__)


# Global variables

ip_list = list()
ip = str()

def restart():
    global app
    app = Flask(__name__, template_folder="templates" )


@app.route('/')
def index():
    title = "Bienvenu sur ryben network"
    if request.remote_addr not in ip_list:
        ip_list.append(request.remote_addr)
    ip = str(request.remote_addr)

    # sets cookies to remember user
    resp = make_response(render_template('index.html', index_title = title))
    resp.set_cookie( 'user' , ip )
    return resp
    #return render_template('index.html', index_title = title)

@app.route('/stats')
def stats():
    title = "Bienvenu sur ryben network statistiques"
    return render_template('stats.html', page_title = title)

@app.route('/test')
def test():
    return 'ceci est un test'

@app.route('/show')
def show():
    dict = {'phy': 50, 'che': 60, 'maths': 70}
    print(dict)
    return render_template('show.html', result=dict)

@app.route('/cookie/')
def get_cookie():
    return jsonify(username = request.cookies.get('user')), 200



if __name__ == '__main__':
    app.run(debug = True)
    app.config['TEMPLATES_AUTO_RELOAD'] = True

