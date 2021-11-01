
##　Connect to the Database コード　1　理解
import sqlite3

import click
from flask import current_app, g
    ①gとは、異なる関数によって何度も呼び出される同じデータを記憶するためのオブジェクト
    呼び出されるたびに何度もデータベースとのコネクションを生成するのは効率が悪いため、gオブジェクトが記憶する。
    ②current_appは、db.pyでFlaskクラスのappインスタンスを生成しなくてもappにアクセスできるようになるためのオブジェクトらしい = 要勉強
from flask.cli import with_appcontext


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()