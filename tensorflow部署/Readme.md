# tensorflow机器学习模型的跨平台上线

## tensorflow机器学习模型的跨平台上线的备选方案
+ 跨平台PMML方式
    + 利用java库jpmml-tensorflow转化生成PMML文件
    + 对于超大模型，使用Pmml文件加载预测速度非常慢，此时没必要考虑跨平台了，建议使用专有环境。
+ tensorflow serving方式
    + 适用于模型和应用比较大规模的情况
    + 需要自己搭建serving集群，比较笨重
+ 跨语言API方式
    + 利用tensorflow的python API生成模型文件，然后利用tensorflow的客户端库java或C++做模型在线预测
    + 适用于中小型的模型和应用场景。


### 参考
+ https://www.cnblogs.com/pinard/p/9251296.html
+ https://blog.csdn.net/bowenlaw/article/details/107015345?spm=1001.2014.3001.5502