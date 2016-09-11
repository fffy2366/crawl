# -*-coding:utf8-*-
from flask import Flask
from flask import render_template
from flask import request
from tutorial.tutorial.models.joke import Joke
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['BOOTSTRAP_SERVE_LOCAL'] = True
Bootstrap(app)

def my_render_template():
    return render_template()


@app.route('/')
def hello_world():
    # return 'Hello World!2'
    page = request.args.get('p', '1')
    cid = request.args.get('cid', '')

    if not page:
        page = 1
    limit = request.args.get('limit', '10')
    if not limit:
        limit = 10

    query = request.args.get('query', '')
    j = Joke()
    jokes, total = j.list(page, limit, cid)

    pager = {'total': int(total), 'limit':int(limit), 'page': int(page)}
    print pager
    return render_template('hello.html', jokes=jokes, query=query, p=pager)

@app.route('/list/')
@app.route('/list/<name>')
def list(name=None):
	# 分页链接会自动添加p这个参数，表示页码
    page = request.args.get('p', '1')
    cid = request.args.get('cid', '')
    if not page:
        page = 1
    limit = request.args.get('limit', '100')
    if not limit:
        limit = 100

    query = request.args.get('query', '')
    j = Joke()
    print "------------------"
    print "cid:{0}".format(cid)
    jokes, total = j.list(page, limit, cid)
    pager = {'total': int(total), 'limit':int(limit), 'curr_page': int(page)}
    # print jokes
    print pager
    return render_template('list.html', name=name, jokes=jokes, query=query, p=pager)
@app.route('/detail/<id>')
def detail(id=None):
    query = request.args.get('query', '')
    j = Joke()
    detail = j.findById(id)
    return render_template('detail.html', joke=detail[0])

@app.route('/baidu_verify_9cWPjuSrYu.html')
def baidu_verify(id=None):
    
    return render_template('baidu_verify_9cWPjuSrYu.html')
   
if __name__ == '__main__':
	app.debug = True
	# app.run(host='0.0.0.0')
	app.run(host='localhost')
