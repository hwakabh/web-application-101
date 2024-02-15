# Lab-25

```text
今までの Lab を踏まえて、最後に「UUID な阿部寛のホームページ」をローカルで作ってみましょう！
簡略化した阿部寛のホームページを自作して、動的コンテンツを扱える自作サイトにしてみましょう。
```

- Lab-25 は最後のハンズオンになります
  - 今までのラボ内容を踏まえて、いよいよ Flask という Python フレームワークを利用して、動的コンテンツを扱える Web サイトを作成します

- URL 設計

| Path | Method | Access | Descriptions |
| --- | --- | --- | --- |
| / | GET | ブラウザ | ルートパス。サイトマップを表示する。 |
| /book | GET | ブラウザ | 阿部寛の出版物に関する情報を静的な HTML コンテンツで表示する。 |
| /movie | GET | ブラウザ | 阿部寛の出演映画に関する情報を静的な HTML コンテンツで表示する。 |
| /api/v1/book | GET / POST | REST-API | 阿部寛の出版物に関する情報を一覧(Read)、追加(Create)する REST-API エンドポイント。 |
| /api/v1/book/${id} | GET | REST-API | 阿部寛の出版物に関する情報を個別参照(Read)する REST-API エンドポイント。 |

```bash
# 実際に各 URL にアクセスしたイメージ
2021/10/03_02:39:41 ~ % curl -X GET localhost:5000/
<!DOCTYPE html>
<html>
  <head>
    <title>HOME</title>
  </head>
  <body>
    <h1>怖くないウェブアプリケーション開発</h1>
    <a href="/">HOME</a>
    <a href="/movie">MOVIE</a>
    <a href="/book">BOOK</a>
  </body>
</html>

2021/10/03_02:39:51 ~ % curl -X GET localhost:5000/book
<!DOCTYPE html>
<html>
  <head>
    <title>BOOK</title>
  </head>
  <body>
    <h1>出版物の情報</h1>
    <a href="/">HOME</a>
    <a href="/movie">MOVIE</a>
    <a href="/book">BOOK</a>
  </body>
</html>2021/10/03_02:40:34 ~ % 

2021/10/03_02:40:35 ~ % curl -X GET localhost:5000/movie
<!DOCTYPE html>
<html>
  <head>
    <title>MOVIE</title>
  </head>
  <body>
    <h1>映画情報</h1>
    <a href="/">HOME</a>
    <a href="/movie">MOVIE</a>
    <a href="/book">BOOK</a>
  </body>
</html>

2021/10/03_02:40:53 ~ % curl -X GET localhost:5000/api/v1/book |jq .
{
  "data": [
    {
      "book_title": "hoge",
      "id": "cba05efe-9185-48ee-8e71-58faa5ca43b3"
    },
    {
      "book_title": "fuga",
      "id": "947fe703-1e2a-40d7-86b7-7a8728a4b12e"
    },
    {
      "book_title": "piyo",
      "id": "8ad0ee49-f27e-4a57-a0d2-2a3683272bd7"
    }
  ]
}
2021/10/03_02:40:56 ~ % curl -X GET localhost:5000/api/v1/book/cba05efe-9185-48ee-8e71-58faa5ca43b3 |jq .
{
  "book_title": "hoge",
  "id": "cba05efe-9185-48ee-8e71-58faa5ca43b3"
}
```

- モデル設計
  - 最もシンプルに、ユーザの POST リクエストとして `阿部寛の出版物に関するタイトル(book_title)` を受け付けて、それに対して動的に UUID を付与する
  - UUID を生成、付与するロジックは、Flask の View（ファイルとしては、`./src/app.py`） 内で記述します

| Field | Data Type | Description |
| --- | --- | --- |
| id | string | 出版物に関する情報に割り当てられる一意の UUID |
| book_title | string | 出版物のタイトル |

```bash
# 実際の SQLite3 データベースの中では以下のようにデータが格納される
$ sqlite3 webapp.db 
SQLite version 3.32.3 2020-06-18 14:16:19
Enter ".help" for usage hints.
sqlite> 
# テーブル一覧
sqlite> .tables
abe_hiroshi_books  alembic_version  
sqlite> 

sqlite> .header on
sqlite> SELECT * FROM abe_hiroshi_books;
id|book_title
cba05efe-9185-48ee-8e71-58faa5ca43b3|hoge|
947fe703-1e2a-40d7-86b7-7a8728a4b12e|fuga|
8ad0ee49-f27e-4a57-a0d2-2a3683272bd7|piyo|
sqlite> .exit

# POST する際のコマンド例
# (Content-Type ヘッダを付与しないと正常に Flask 側でリクエストボディを扱うことができません)
$ curl -X POST localhost:5000/api/v1/book -H "Content-Type: application/json" -d '{"book_title": "abe_hiroshi_jiden"}'
{"result":"ok"}

# 正常に登録できると、データベース内では以下のようにリクエストデータに応じて、UUID が付与され、REST-API で参照できるようになる
sqlite> SELECT * FROM abe_hiroshi_books;
id|book_title
cba05efe-9185-48ee-8e71-58faa5ca43b3|hoge|
947fe703-1e2a-40d7-86b7-7a8728a4b12e|fuga|
8ad0ee49-f27e-4a57-a0d2-2a3683272bd7|piyo|
ee13f9a2-8a5a-4ef4-b12b-52183ce734a0|abe_hiroshi_jiden|

$ curl -X GET localhost:5000/api/v1/book/ee13f9a2-8a5a-4ef4-b12b-52183ce734a0 |jq .
{
  "book_title": "abe_hiroshi_jiden",
  "id": "ee13f9a2-8a5a-4ef4-b12b-52183ce734a0"
}
```

***

## Hello Flask: 最もシンプルな View を作る

- まずは Python の Web Application Framework である Flask を動かせるようにしましょう
  - Flask パッケージのインストール
  - Flask で起動したアプリケーションにアクセスしてみて、"Hello World" という文字列を返すことができればこのセクションは OK です

```bash
# Flask パッケージのインストール
# (SQLite3 のデータベースを扱うための関連パッケージも含んでいます)
$ pip install flask Flask-SQLAlchemy Flask-Migrate

# アプリケーションを構成するディレクトリと、アプリケーションの起動に最小限必要なファイルを作成
# (フレームワークを利用した開発では、プログラムの目的に応じてファイルが多数必要になるので、ディレクトリにまとめられることが大半です)
$ mkdir ./src
# Flask アプリケーションを起動するために必要なプログラム
$ touch ./run.py
# 実際の処理内容が書かれる Flask アプリケーションのプログラム
$ touch ./src/app.py
$ touch ./src/__init__.py
```

- アプリケーション起動用のプログラム: `./run.py`
  - Flask では複数のアプリケーションを扱うこともできるため、どのアプリケーションをどのように起動するのか、という起動用のプログラムを作成することが多いです
    - 必須ではないですが、ソースコードのどこかで `アプリケーションを起動する` ロジックは含める必要がある

```python
# ./src/app.py から webapp というアプリケーションを import
from src.app import webapp

if __name__ == "__main__":
    # import したアプリケーションを起動する
    webapp.run()
```

- アプリケーションプログラム: `./src/app.py`

```python
from flask import Flask


# Flask を利用して自分のアプリケーションをインスタンス化する
# (webapp という名前は自由に命名可能)
webapp = Flask(__name__)

# アノテーション(@) を利用してアプリケーションのルートパス(/) に GET された場合の処理を記述する
@webapp.route('/', methods=['GET'])
def hello():
    return 'Hello World’
```

- アプリケーションの起動と、アクセス

```bash
# 起動するための環境変数を設定
$ export FLASK_APP='src/app.py'

# Flask パッケージをインストールすると、flask コマンドが使えるようになるので、これを利用してアプリケーションを起動する
# (デフォルトでは、localhost:5000 でアプリケーションが起動されます)
$ flask run
```

```bash
# 別のシェルを開いて、アプリケーションにアクセスしてみる
$ curl -X GET localhost:5000/
Hello World
```

***

## Template を使ってみる

- 静的な HTML コンテンツをユーザが見れるようにするためには、ロジックとして、ユーザのリクエスト内容に応じて、どの HTML をユーザに返すのか？という処理を記述する必要があります
  - Flask では `render_template()` という関数を利用して、Template と View との対応を紐付けます

```bash
# HTML が格納されるフォルダを作成
# (templates という名前で作成することで、Flask が自動的にこのフォルダ内を検索するようになります)
$ mkdir -p ./src/templates
$ touch ./src/templates/index.html

# index.html を好きに作る
$ echo '<h1>Hello Index Page</h1>' > ./src/templates/index.html
```

```python
# import するパッケージを追加
from flask import Flask, render_template, request, jsonify

webapp = Flask(__name__)

# 先程の Hello World を記載した src/app.py を書き換えてみましょう
@webapp.route('/', methods=['GET'])
def index_page():
    # localhost:5000/ に GET アクセスがされた場合、./src/templates/index.html の内容がユーザに返される、ということ
    return render_template('index.html')
```

- 今回のラボで紹介しきれなかった Templates の機能
  - テンプレートの継承: `extends`
    - 実際の Web アプリケーションではユーザのリクエストごとに動的な HTML が生成されていますが、それらをすべてコーディングするのは現実的ではありません
      - 実際にみなさんが Web サイトをみている時に、ページ遷移される回数を想像すれば想像に容易いかと思います
    - Flask はじめ多くのフレームワークでは、ベースとなる HTML を作り、可変部分だけをファイルとして別途作成しておき、それらを紐づけることで作成すべき HTML を最小限にする仕組みがあります

  - テンプレートとのデータのやりとり
    - ユーザからのデータを受け取り、それに応じて何かの処理が(View により)行われ、その結果がユーザ側に返る、というケースも実際のアプリケーションでは多数見られます
      - View 側でユーザのリクエストボディを受け取り、View で記載した Python の処理結果を、Template 側に返し、HTML としてそれらを表示する、という形になります
    - Flask では、`render_template()` 関数で処理結果を一緒に Template 側に渡し、Template 側では jinja2 というテンプレートエンジンの文法に応じて HTML を書くことで処理結果を表示することができます

***

## Model を構成する

- 今回のラボでは、データベースとして SQLite3 を利用しますが、簡易的なデータベースとして、JSON ファイルを利用するパターンの例も用意しています
  - Model を利用する（SQLite3 を Python から操作する）パターン
    - アプリケーションファイル: `./src/app_model.py` を参考に
    - データベースファイル: `./src/webapp.db`
  - JSON ファイルを利用するパターン
    - アプリケーションファイル: `./src/app_json.py` を参考に
    - データベースファイル: `./src/webapp.json`

- ここでは、Model を利用するパターンについて、以下のポイントを記載します
  - データベースを利用可能にする
  - データベース内に実際に作成されるテーブルやフィールドを Python で定義する
  - View 側で Model と連動させる

```bash
# database を扱うプログラムを作成
$ touch ./src/database.py
# モデルに関するプログラムをまとめるディレクトリを作る
$ mkdir -p ./src/models
$ touch ./src/models/books.py
```

- `database.py` は、Python からデータベースを扱うための処理や、初期化処理などを含める

```python
# ./src/database.py
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# SQLAlchemy で、データベースをインスタンス化する
# この時点では何も設定が入っていない
webdb = SQLAlchemy()

# View 側から Flask アプリケーションそのものを引数として受け取り、データベースの初期化を行う
def init_db(app):
    webdb.init_app(app)
    # Flask-Migrate パッケージでマイグレーション処理を行うことができるように、追加
    Migrate(app, webdb)
```

- `database.py` により Python でデータベースを扱うことができるようになったので、これを View 側で Flask アプリケーションと紐づけていく
  - SQLite3 のデータベースファイル名や、定義した初期化処理の実行など

```python
# ./src/app.py
# import するパッケージとして、これから作成する Model 関連のファイルを指定する
from .database import init_db, webdb
from .models.books import Books

# database.py で作成したデータベースに設定を入れ込む
webapp.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///webapp.db'
webapp.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
init_db(app=webapp)
```

- モデルに関する定義
  - Flask や Django では、Python のクラスを利用してデータベース定義を抽象化します
  - クラスに関連して、オブジェクト指向に関しては今回詳細は割愛します

```python
# Python で扱えるようになったデータベースのオブジェクトを import
from src.database import webdb

class Books(webdb.Model):
    # データベース内で作成されるテーブル名を指定(任意)
    __tablename__ = 'abe_hiroshi_books'

    # データベース内でのフィールドを定義
    id = webdb.Column(webdb.String(50), primary_key=True)
    book_title = webdb.Column(webdb.String(50))

    # クラスがインスタンスとして作成された時の初期化処理
    def __init__(self, id=None, title=None):
        self.id = id
        self.book_title = title

    # Model からのクエリ結果は、iterable だがそのまま jsonify に渡せないため
    def to_dict(self):
        return {
            'id': self.id,
            'book_title': self.book_title
        }
```

- マイグレーションの実行
  - 定義した Model を実際に自分の環境の SQLite3 として構成する
  - モデルの定義を変更した際（=`./src/models/books.py` の内容を変更した際）には、実際のデータベース内の定義と、アプリケーションが想定するデータベースの定義とで乖離が生じるため、都度マイグレーション処理を行う必要があります

```bash
# データベース初期化
# (これにより、./migrations というフォルダが自動的に作られる)
$ flask db init
  Creating directory /Users/hwakabh/git/web-application-development/Lab-25/migrations ...  done
  Creating directory /Users/hwakabh/git/web-application-development/Lab-25/migrations/versions ...  done
  Generating /Users/hwakabh/git/web-application-development/Lab-25/migrations/script.py.mako ...  done
  Generating /Users/hwakabh/git/web-application-development/Lab-25/migrations/env.py ...  done
  Generating /Users/hwakabh/git/web-application-development/Lab-25/migrations/README ...  done
  Generating /Users/hwakabh/git/web-application-development/Lab-25/migrations/alembic.ini ...  done
  Please edit configuration/connection/logging settings in '/Users/hwakabh/git/web-application-development/Lab-25/migrations/alembic.ini' before proceeding.

# migration ファイルを作成する
# migration ファイルは、実際にデータベースに対して投げられる処理などが記載されたファイルで、この時点ではまだデータベースへの処理は適用されない
# ./migrations/versions/ 配下にファイルが作成される(バージョン管理のため)
$ flask db migrate
INFO  [alembic.runtime.migration] Context impl SQLiteImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
INFO  [alembic.autogenerate.compare] Detected added table 'abe_hiroshi_books'
  Generating /Users/hwakabh/git/web-application-development/Lab-25/migrations/versions/b872216924e4_.py ...  done

# migration を実行する == migration ファイルを適用する
# これにより、./src/webapp.db が自動的に作成され、内部に ./src/models/books.py で定義した内容が設定される
$ flask db upgrade
INFO  [alembic.runtime.migration] Context impl SQLiteImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
INFO  [alembic.runtime.migration] Running upgrade  -> b872216924e4, empty message
```

- ここまでできれば、あとは自由に View や Template を書き換えていき、アプリケーションを組み立てていくだけです！
  - 理論的には、Python でできることはアプリケーションとして実装していくことが可能です
  - `./src/app_model.py` や `./src/app_json.py` のサンプルロジックを参考にして、はじめての Flask アプリケーションをつくっていってみましょう！
