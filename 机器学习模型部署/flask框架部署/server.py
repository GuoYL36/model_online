'''
利用flask框架来部署深度学习模型——部署代码
'''

from flask import Flask,request,jsonify
import tensorflow as tf
import numpy as np
app = Flask(__name__)

# 预加载模型

def load_model():
    path="./my-model/"
    sess = tf.Session()
    saver = tf.train.import_meta_graph("./my-model/my-model.meta")  # 加载计算图
    saver.restore(sess, tf.train.latest_checkpoint(path))
    # var_lists = tf.global_variables()   # 获取变量名称
    graph = tf.get_default_graph()   # 获取计算图中
    return sess, graph

# sess, var_lists, graph = load_model()
# print(sess)
# print(var_lists)
# print(graph)
# inputs = graph.get_tensor_by_name("input:0")
# pred = graph.get_tensor_by_name("output:0")
# # print(graph.get_tensor_by_name("input:0"))
# x = np.random.random((1,6))
# print(x)
# print(sess.run(pred, feed_dict={inputs:x}))

# 加载model
sess, graph = load_model()

# 进行预测
@app.route("/predict", methods=["POST"])
def predict():
    # initialize the data dictionary that will be returned from the
    # view
    data = {"success": False}
    print(data)

    # ensure an image was properly uploaded to our endpoint
    if request.method == "POST":
        print("Hello")
        if request.form.get("input"):
            print("world")

            # 获取url中的表单内容
            x = request.form.get("input",type=str,default="")
            print("x: ",x, x.split(","))
            arr = np.array([[float(i) for i in x.split(",")]])

            # 加载graph
            inputs = graph.get_tensor_by_name("input:0")
            pred = graph.get_tensor_by_name("output:0")

            pred_score = sess.run(pred, feed_dict={inputs: arr})[0]

            data["predictions"] = int(pred_score)
            # data["predictions"].append(pred_score)

            # indicate that the request was a success
            data["success"] = True
            print(data)

    # return the data dictionary as a JSON response
    return jsonify(data)


if __name__ == "__main__":
    app.config["JSON_AS_ASCII"]=False
    app.run(host="127.0.0.1", port=8000)



