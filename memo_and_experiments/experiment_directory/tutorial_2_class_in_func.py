
"""
tutorial 2：the application factoryでは、
Flaskインスタンスをcreate_app関数内で実行している。これにより様々な設定が関数内で一気に行える。
create_app関数は、appインスタンスを返している。

今までインスタンスを関数内で生成し、[return インスタンス]のようにインスタンスを返すような関数を作ったことがなかったので、実践してみる。
"""


# まずはクラスを作成する

class Mid_twenties():
    def __init__(self, name, age, ismarry = True):
        self.name = name
        self.ag4e = age
        self.ismarry = ismarry

    def greeding(self):
        print('私の名前は'+ self.name + 'です。よろしく')

    def propose(self):
        if self.ismarry is True:
            print('はい、結婚します。')
        else:
            print('今のところは結婚する気はありません。')

# 方法1
# def create_mid_twenties():
#     man = Mid_twenties('スニーズ', 29, True)
#     return man 

#方法2 クロージャー
def create_mid_twenties():
    man = Mid_twenties('スニーズ', 29, True)
    def call_method():
        return man.propose()
    return call_method


if __name__ == '__main__':

    # 方法1
    # create_mid_twenties().greeding()
    # create_mid_twenties().propose()

    #方法2
    create = create_mid_twenties()
    create()