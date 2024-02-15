import uuid
import os
import json

from flask import Flask, render_template, request, jsonify

# Flask インスタンス作成 & 初期設定
webapp = Flask(__name__)

DB_FILE_NAME = './src/webapp.json'

if os.path.exists(DB_FILE_NAME):
    with open(DB_FILE_NAME, 'r+') as f:
        db = json.load(f)   #-> type: dict
else:
    db = {}


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

    if request.method == 'GET':
        resp = db

    elif request.method == 'POST':
        # POST 時には -H 'Content-Type: application/json' が必要
        payload = request.json
        if payload:
            b = {
                "id": str(uuid.uuid4()),
                "book_title": payload.get('book_title'),
            }

            books = db.get('data')  #-> type:list
            books.append(b)
            with open(DB_FILE_NAME, 'wt') as f:
                json.dump({"data": books}, f, indent=2)

            resp = {
                "result": "ok"
            }
        else:
            resp = {
                "result": "error"
            }

    return jsonify(resp)


# Read(Datail)
@webapp.route('/api/v1/book/<string:bookid>', methods=['GET'])
def get_book(bookid=None):
    resp = {}

    if db:
        resp = {
            "result": "not-found"
        }

        for b in db.get('data'):
            if b.get('id') == bookid:
                resp = b

    return jsonify(resp)
