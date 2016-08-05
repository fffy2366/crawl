# -*-coding:utf8-*-
from flask import Flask
from flask import render_template
from flask import request
from tutorial.tutorial.models.joke import Joke

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!2'

@app.route('/list/')
@app.route('/list/<name>')
def list(name=None):
	# 分页链接会自动添加p这个参数，表示页码
    page = request.args.get('p', '1')
    if not page:
        page = 1
    limit = request.args.get('limit', '10')
    if not limit:
        limit = 10

    query = request.args.get('query', '')
    j = Joke()
    jokes, total = j.list(page, limit, query)

    pager = {'total': int(total), 'limit':int(limit), 'curr_page': int(page)}
    print pager
    return render_template('list.html', name=name, jokes=jokes, query=query, p=pager)

if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0')
