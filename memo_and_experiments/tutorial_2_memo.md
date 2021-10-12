# The Application Factory

Tutorial 2：The Application Factory<br>
Flaskクラスのappインスタンスの生成方法<br>
※ 作業ディレクトリ：flaskr/__init__.py<br>


## __init__.pyファイルの役割
__init_,pyファイルの役割は主に2つ。<br>
1つ目は、application factoryコードが書かれており、これによってflaskのインスタンスを生成することができる。<br>
2つ目は、__init__.pyによって、flaskrディレクトリがパッケージの役割を果たすことができる。<br>
ちなみに、<br>
スクリプトファイルがモジュールで、スクリプトファイルが格納されているディレクトリがパッケージ<br>
パッケージ用のディレクトリに__init__.pyをおくのが標準的で、そのようなパッケージを正規パッケージという。<br>


## コード

import os
from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app


## コードの理解/説明

def create_app(test_config = None):
        ① 関数内でappインスタンスを生成して、返り値としてappインスタンスを返している関数。

    app = Flask(__name__, instance_relative_config=True)

        ① 関数内でFlaskのインスタンスを生成している。
        __name__は現在のモジュール、今後の設定ファイルで設定をしていく上で、インスタンス生成のファイルがどのモジュールであるのかをわかっていなければいけない場合があるから、このように__name__と明記する。

        ② Flask 0.8から新たにinstance folderという新しい概念が導入された。
        instance folderには機密性の高いパスワードなどが書かれているため、誤ってgit pushなどしたら大変。
        だから、そもそもアプリ開発のためのflaskrディレクトリ配下におかず、flaskrの外にinstance folderとして保管する。
        そしてinstance folderは.gitignoreに入れる。
        しかし、そのinstance folderまでのパスがわからないとパスワードを使いたい時など困ってしまう。
        (仮説)
        instace folderに対するconfigurationファイルのパスをアプリケーションに伝える上で、そのパスが相対パスなのか絶対パスなのかをはっきりさせる必要がある。
        そして、instance_relative_config = Trueならば、おそらくconfigファイルとinstance folderのパスを相対パスにするということを示しているのではなかろうか。
    


    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )
        ① app.config.from_mappingで、今後開発に必要な設定を行なっている。
        "app.config.from_mapping() sets some default configuration that the app will use:"

        ② SECRE_KEY変数に格納することで、機密性の高いものをカモフラージュすることができる。
        例えば、SECRET_KEYは開発に使えるが、デプロイした時にこの値がランダムな値になるように設定できる。

        ③ DATABASE変数では、SQLiteのデータベースファイルが置かれているパスが格納されている。
        app.instance_pathには、flaskr.sqliteファイルが実際に置いてあるディレクトリまでのパスが格納されている。
        os.path.joinで、flaskr.sqliteファイルとそこに行き着くまでのパスapp.instance_pathを結合させている。
        つまり、flaskr.sqliteファイルまでのパスということ。
        (osライブラリの実戦については、tutorial_2_os_library参照)


    if test_config is None:
        app.config.from_pyfile('config.py', silent = True)
    else:
        app.config.from_mapping(test_config)
    
        ① app.config.from_pyfileで、instance folder内のcofig.pyから、機密性の高い本物のパスワードを実際に持ってくる設定をしている。
        "app.config.from_pyfile() overrides the default configuration with values taken from the config.py file in the instance folder if it exists. For example, when deploying, this can be used to set a real SECRET_KEY."

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

        ① app.instance_pathを指定して、仮にinstance folderが存在しなかった場合に、instance folderを生成する。

    @app.route('/hello')
    def hello():
        return 'Hello, World!'
        ①@app.route('/hello')でルーティングしている。

    return app

        ① appインスタンスを返している。




