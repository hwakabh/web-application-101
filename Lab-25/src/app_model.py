import uuid

from flask import Flask, render_template, request, jsonify
from .database import init_db, webdb
from .models.books import Books

# Flask インスタンス作成 & 初期設定
webapp = Flask(__name__)
webapp.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///webapp.db'
webapp.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
init_db(app=webapp)


# ----- Browser Access
@webapp.route('/', methods=['GET'])
def index_page():
    return render_template('index.html')


@webapp.route('/movie', methods=['GET'])
def movie_page():
    return render_template('movie.html')


@webapp.route('/book', methods=['GET'])
def book_page():
    return render_template('book.html')



# ---- REST-API
# Create/Read(List)
@webapp.route('/api/v1/book', methods=['GET', 'POST'])
def book():
    resp = {}

    # Flask の request(ラボで扱った requests とは別物) を利用して、HTTP メソッドを判定
    if request.method == 'GET':
        # レスポンスボディを組み立てる
        resp = {
          "data": [b.to_dict() for b in Books.query.all()]
        }

    elif request.method == 'POST':
        # POST 時には -H 'Content-Type: application/json' が必要
        # ユーザのリクエストボディを json で受け取り、payload という変数に格納
        payload = request.json

        if payload:
            # UUID を自動生成するロジック
            book_id = str(uuid.uuid4())
            # ユーザのリクエストボディで book_title の Key で指定されたデータを取得
            book_title = payload.get('book_title')

            # 自分で定義した ./src/models/books.py 内の Book という Model をインスタンス化する
            # インスタンス化する際に、上記で定義した book_id, book_title を与えることで、データを更新する
            b = Books(book_id, book_title)
            webdb.session.add(b)
            webdb.session.commit()

            # 成功時のレスポンスボディ
            resp = {
                "result": "ok"
            }

        else:
            # ユーザのリクエストボディを取れなかったケースのレスポンスボディ
            # (Content-Type: application/json が含まれない場合、など)
            resp = {
                "result": "error"
            }

    # リクエストボディをユーザ側に返す(REST-API なので JSON 形式で返す)
    return jsonify(resp)


# Read(Datail)
@webapp.route('/api/v1/book/<string:book_id>', methods=['GET'])
def get_book(book_id=None):
    resp = {
        "result": "not-found"
    }

    # Model から検索(id がない場合には、null が戻る)
    book = Books.query.filter_by(id=book_id).first()
    if book:
        resp = book.to_dict()

    return jsonify(resp)
