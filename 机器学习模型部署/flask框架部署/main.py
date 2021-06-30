import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets.samples_generator import make_classification
import tensorflow as tf

class model:
    def __init__(self, learning_rate, batch_size, training_epochs):
        self.learning_rate = learning_rate
        self.batch_size = batch_size
        self.training_epochs = training_epochs

    def build_graph(self):
        self.add_placeholder()
        self.forward()
        self.losses()
        self.optimizer_op()
        self.init_op()

    def add_placeholder(self):
        self.x = tf.placeholder(tf.float32, [None, 6], name="input")
        self.y = tf.placeholder(tf.float32, [None, 3])

    def forward(self):
        w = tf.Variable(tf.zeros([6, 3],tf.float32))
        b = tf.Variable(tf.zeros([3],tf.float32))
        self.logits = tf.nn.softmax(tf.matmul(self.x,w)+b, name="softmax")
        self.pred_labels = tf.argmax(self.logits, axis=1, name="output")

    def losses(self):
        self.cost = tf.reduce_mean(-tf.reduce_sum(self.y*tf.log(self.logits), reduction_indices=1))

    def optimizer_op(self):
        optimizer = tf.train.GradientDescentOptimizer(self.learning_rate)
        self.train_ops = optimizer.minimize(self.cost)

    def init_op(self):
        self.inits = tf.global_variables_initializer()

    def save_model(self, sess):
        '''
        这里与tf.train.Saver的区别：
            Saver：保存所有的参数信息
            convert_variables_to_constants：保存计算图及神经网络的输入层经前向传播计算得到的输出层参数
        '''
        graph = tf.graph_util.convert_variables_to_constants(sess, sess.graph_def, ["output"])
        tf.train.write_graph(graph, '.', 'rf.pb', as_text=False)

    def save_model0(self, sess):
        '''

        :param sess:
        :return:
        '''
        saver = tf.train.Saver()
        saver.save(sess, "./my-model")


    def train(self, x, y):
        y2 = tf.one_hot(y, 3)
        with tf.Session() as sess:
            y2 = sess.run(y2)
            sess.run(self.inits)

            for epoch in range(self.training_epochs):
                _, c = sess.run([self.train_ops,self.cost], feed_dict={self.x: x, self.y: y2})
                if (epoch+1) % 10 == 0:
                    print("Epoch: ", '%04d'%(epoch+1), "cost=","{:.9f}".format(c))
            print("优化完毕")
            correct_prediction = tf.equal(self.pred_labels, tf.argmax(y2,1))
            acc = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
            print(sess.run(acc, feed_dict={self.x:x, self.y:y2}))
            print("保存模型")
#            self.save_model(sess)
            self.save_model0(sess)

# 获取数据集
x1, y1 = make_classification(n_samples=4000, n_features=6, n_redundant=0,n_clusters_per_class=1,n_classes=3)

Model = model(0.01, 100, 10000)
Model.build_graph()
Model.train(x1, y1)












