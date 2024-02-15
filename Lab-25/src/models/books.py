from src.database import webdb


class Books(webdb.Model):
    __tablename__ = 'abe_hiroshi_books'

    id = webdb.Column(webdb.String(50), primary_key=True)
    book_title = webdb.Column(webdb.String(50))

    def __init__(self, id=None, title=None):
        self.id = id
        self.book_title = title

    # Model からのクエリ結果は、iterable だがそのまま jsonify に渡せないため
    def to_dict(self):
        return {
            'id': self.id,
            'book_title': self.book_title
        }
