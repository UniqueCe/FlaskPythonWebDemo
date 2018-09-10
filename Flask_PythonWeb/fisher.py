from flask import Flask
from config import DEBUG
from helper import is_isbn_or_key
from yushu_book import YuShuBook

'''
def Flask_Web():
    return "这只是一个开始！！！\n [1. /hello]"

@app.route('/hello/')
def hello():
    return "Hello Flask Web!"
app.add_url_rule('/', view_func=Flask_Web)
'''

app = Flask(__name__)
'''
豆瓣API
https://api.douban.com/v2/book

鱼书 -- 搜索API
鱼书：http://www.yushu.im
关键字搜索API：http://t.yushu.im/v2/book/search?={}&start={}&count={}
sibn搜索API：http://t.yushu.im/v2/book/isbn/{}
'''


@app.route('/book/search/<q>/<page>')
def search(q, page):
    isbn_or_key = is_isbn_or_key(q)
    if isbn_or_key:
        YuShuBook.search_by_isbn(q)




if __name__ == '__main__':
    print("OK")
    app.run(host='0.0.0.0', debug=DEBUG)