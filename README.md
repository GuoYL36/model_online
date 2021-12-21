# model_online
> Some methods of model deploy online

## 主要分传统机器学习模型部署和深度学习模型部署
+ 路径
    + 机器学习模型部署
        + tornado框架部署
            + lightgbm模型
		+ flask框架部署
			+ tensorflow模型
    + tensorflow部署
        + 跨语言API方式
            + client_api
        + 跨平台PMML方式
        + tensorflow serving方式

## 线上
> 参考：https://mp.weixin.qq.com/s/IAWO5C4WRSC6Qu6ffsdbig
### 要求
+ 保持线上与线下逻辑一致
	+ 线上数据清洗和特征提取流程与线下一致，使用同一套代码；
	+ 由于线上数据是json格式，线下处理时最好保持输入是json格式数据
+ 模型分数预测
	+ 要求线上与线下测试100%一致，理论上小数点后10位要一模一样
	+ 线上测试效率要求1条数据需要在200—500ms内返回
+ 实时模型监控
	+ 数据特征监控
		+ 有数据异常时，便于定位问题
	+ 模型状态监控
		+ 模型在预测过程中可能会出现一些意想不到的情况，比如网络延时导致的效率低、输出有问题等，都需要记录下来
	+ 模型分数监控
		+ 监控模型分数的分布（PSI指标）
		+ 推荐设定预警系统

### tensorflow-serving
> 利用tf.keras.models.save_model函数保存最新模型
```python
从下面的代码中你可以看到，这一函数需要传入的参数有要保存的 model 结构，保存的路径，还有是否覆盖路径 overwrite 等等。其中，我们要注意的是保存路径。你可以看到，我在保存路径中加上了一个模型版本号 002，这对于 TensorFlow Serving 是很重要的，因为 TensorFlow Serving 总是会找到版本号最大的模型文件进行载入，这样做就保证了我们每次载入的都是最新训练的模型。详细代码请你参考 NeuralCF.py

tf.keras.models.save_model(
    model,
  "file:///Users/zhewang/Workspace/SparrowRecSys/src/main/resources/webroot/modeldata/neuralcf/002",
    overwrite=True,
    include_optimizer=True,
    save_format=None,
    signatures=None,
    options=None
)
其次是模型的导入，导入命令非常简单就是 TensorFlow Serving API 的启动命令，我们直接看下面命令中的参数。

docker run -t --rm -p 8501:8501     -v "/Users/zhewang/Workspace/SparrowRecSys/src/main/resources/webroot/modeldata/neuralcf:/models/recmodel"     -e MODEL_NAME=recmodel     tensorflow/serving &
这里面最重要的参数，就是指定载入模型的路径和预估 url，而载入路径就是我们刚才保存模型的路径：/Users/zhewang/Workspace/SparrowRecSys/src/main/resources/webroot/modeldata/neuralcf。但是在这里，我们没有加模型的版本号。这是为什么呢？因为版本号是供 TensorFlow Serving 查找最新模型用的，TensorFlow Serving 在模型路径上会自动找到版本号最大的模型载入，因此不可以在载入路径上再加上版本号。除此之外，冒号后的部分“/models/recmodel”指的是 TensorFlow Serving API 在这个模型上的具体 url，刚才我们是通过请求 http://localhost:8501/v1/models/recmodel:predict 获取模型预估值的，请求连接中的 models/recmodel 就是在这里设定的。
```


### 问题
+ 线上json缺少特征，如何处理？
	+ 返回“数据错误”
+ 线上与线下分数预测不一致
	+ 保证线上与线下逻辑的一致性；
	+ 如果线上与线下逻辑一致，则从以下几点考虑
		+ 机器的精度
		+ 在gpu上训练，在cpu上测试
		+ python包版本不一致
		+ 特征有存储后读出的逻辑使得精度改变
		

