
## tutorialに出てくるさまざまなosライブラリの関数・メソッドの練習

import os

dir_path = '/Users/home/workspace/kota_training/projects/flask_tutorial/drafts'
new_dir_absolute_path = '/Users/home/workspace/kota_training/projects/flask_tutorial/drafts/test_os/test_os.py'
new_dir_retative_path = '../../drafts/test_os'
new_file_path = '/Users/home/workspace/kota_training/projects/flask_tutorial/drafts/test_os/test_os.py'


print(os.getcwd())
print(os.listdir(dir_path))
print(os.listdir('.'))

# 新しいディレクトリの名前を合わせてパスを指定する。これはディレクトリ作成であって、ファイル作成ではない。
os.mkdir(new_dir_absolute_path)
os.rmdir(new_dir_absolute_path)
# 1つ上に上がってmemo_and_experimentsディレクトリへ、もう1つ上がってdraftsディレクトリにいって
# そこでtest_osディレクトリが作成される。
os.mkdir(new_dir_retative_path)

# 親パスと作業ディレクトリに分割してくれる。作業ディレクトリがflask_tutorialの場合、
# ('/Users/home/workspace/kota_training/projects', 'flask_tutorial')と分ける。
print(os.path.split(os.getcwd()))
('/Users/home/workspace/kota_training/projects/flask_tutorial/drafts', 'test_os')
print(os.path.split(new_dir_absolute_path))


print(os.path.splitext(new_file_path))

# os.path.split()とは逆で、パスとファイル名をつないで返してくれます。
# os.path.join(パス、ファイル名)
print(os.path.join(new_dir_absolute_path, 'test_os.py'))