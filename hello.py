# -*-coding:utf8-*-
from flask import Flask
from flask import render_template
from flask import request
from flask import make_response
from tutorial.tutorial.models.category import Category
from tutorial.tutorial.models.joke import Joke
from flask_bootstrap import Bootstrap
from datetime import datetime
from datetime import timedelta

from config.config import Config
# app = Flask(__name__)
app = Flask(__name__, static_folder='static', static_url_path='')
app.config['static_folder'] = 'static'
app.config['static_url_path'] = ''
app.config['BOOTSTRAP_SERVE_LOCAL'] = True
conf = Config()
if(Config.ENV=="dev"):
    app.config.from_object('config.config.DevelopmentConfig')
elif(Config.ENV=="testing"):
    app.config.from_object('config.config.TestingConfig')
elif(Config.ENV=="prod"):
    app.config.from_object('config.config.ProductionConfig')


Bootstrap(app)

def my_render_template(template_name_or_list, **context):
    context["test"] = "test"
    context["host"] = app.config["HOST"]
    # print context
    #获取分类
    cate = Category()
    category = cate.findAll()
    context['category'] = category

    return render_template(template_name_or_list, **context)

def home(cid=''):
    if(request.path=="/hot"):
        menu = "hot"
    else:
        menu = "latest"
    page = request.args.get('p', '1')
    # cid = request.args.get('cid', '')

    if not page:
        page = 1
    limit = request.args.get('limit', '10')
    if not limit:
        limit = 10

    query = request.args.get('query', '')
    j = Joke()
    jokes, total = j.list(page, limit, cid,menu)
    cate = None
    if(cid):
        c = Category()
        cate = c.findById(cid)

    pager = {'total': int(total), 'limit':int(limit), 'page': int(page)}
    # print pager
    app.logger.debug(request.path)
    app.logger.debug("host:"+request.host)
    ass = []
    for a in request.args:
        if(a=="p"):
            continue
        ass.append(a+"="+request.args.get(a))
        app.logger.debug(a)
        app.logger.debug(request.args.get(a))
    args = "&".join(ass)
    args = "?"+args if args else ""
    return my_render_template('hello.html', jokes=jokes, query=query,path=request.path,args=args, p=pager,menu=menu,cate=cate)
@app.route('/')
@app.route('/home')
def hello_world():
    return home()

@app.route('/hot')
def hot():
    return home()

# 分类
@app.route('/category/<cid>')
def category(cid=None):
    return home(cid)

@app.route('/detail/<id>.html')
def detail(id=None):
    # query = request.args.get('query', '')
    j = Joke()
    detail = j.findById(id)
    #阅读量加1
    j.addViewCount(id)
    #上一篇 下一篇
    prev_date = j.prev_next("prev",detail[0],"date")
    next_date = j.prev_next("next",detail[0],"date")
    prev_cate = j.prev_next("prev",detail[0],"cate")
    next_cate = j.prev_next("next",detail[0],"cate")

    relation = {"prev_date":prev_date,"next_date":next_date,"prev_cate":prev_cate,"next_cate":next_cate}
    return my_render_template('detail.html', joke=detail[0],relation=relation)

@app.route('/baidu_verify_9cWPjuSrYu.html')
def baidu_verify(id=None):
    
    return render_template('baidu_verify_9cWPjuSrYu.html')

# [Generating a sitemap.xml](http://flask.pocoo.org/snippets/108/)
@app.route('/sitemap.xml', methods=['GET'])
def sitemap():
    """Generate sitemap.xml. Makes a list of urls and date modified."""
    pages=[]
    # ten_days_ago=datetime.now() - timedelta(days=10).date().isoformat()
    # category
    cate = Category()
    category = cate.findAll()
    for c in category:
        pages.append(
                ["http://"+request.host+"/category/"+c['category_id'],"2016-09-26"]
            )

    sitemap_xml = render_template('sitemap.xml', pages=pages)
    response= make_response(sitemap_xml)
    response.headers["Content-Type"] = "application/xml"    

    return response

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404



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
    return my_render_template('list.html', name=name, jokes=jokes, query=query, p=pager)

if __name__ == '__main__':
	app.debug = True
	# app.run(host='0.0.0.0')
	app.run(host='localhost')
