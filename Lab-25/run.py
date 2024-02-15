# # --- Model の代わりに JSON ファイルを用いる場合
# # シェルで export FLASK_APP='src/app_json.py' を実行してから flask run
# from src.app_json import webapp

# --- Model を用いる場合
# シェルで export FLASK_APP='src/app_model.py' を実行してから flask run
from src.app_model import webapp


if __name__ == "__main__":
    # Flask インスタンスを起動
    webapp.run()
