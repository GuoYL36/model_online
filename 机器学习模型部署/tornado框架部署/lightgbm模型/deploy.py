'''
此代码利用tornado框架来部署lightgbm模型pkl文件
'''


# ==============================================================
## 利用tornado框架部署
## 部署模型文件代码
'''
运行deploy.py后，此时已经加载模型，会一直监听localhost:9999，页面输入http://localhost:9999/，会显示"Hello, 666666"
如果要通过post请求调用模型，可以使用postman发送post请求
'''
import tornado.ioloop
import tornado.web
import json
import joblib
import numpy as np


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, 666666")

    def post(self):
        data = self.request.body.decode("utf-8")
        data = json.loads(data)

        # # ==== 单条数据测试
        # data = np.array(data["data"]).reshape(1, 4)  # 单条数据测试
        # predict_lbl = clf.predict(data)[0]
        #
        # msg = {"label": int(predict_lbl), "code": 200}
        # self.write(json.dumps(msg))
        # # ====================

        # ==== 多条数据测试
        data = np.array(data["data"]).reshape(-1,4)
        predict_lbl = clf.predict(data)
        msg = {"label": predict_lbl.tolist(), "code": 200}
        self.write(json.dumps(msg))
        # =================



if __name__ == "__main__":
    application = tornado.web.Application([(r"/", MainHandler), ])  # 路由映射到类
    clf = joblib.load("./model.pkl")
    application.listen(9999)  # 监听端口
    tornado.ioloop.IOLoop.instance().start() # 启动IOLoop,该函数一直运行且不退出，用于处理完所有客户端的访问请求
