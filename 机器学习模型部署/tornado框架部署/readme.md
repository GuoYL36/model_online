### tornado框架部署lightgbm模型服务
+ 步骤
    + 准备模型文件
    + 第一步，运行deploy.py文件
    + 第二步，打开浏览器输入http://localhost:9999/，查看页面是否有“Hello, 666666”，出现这个说明服务已经起来了。
    + 第三步，打开postman工具，选择post，地址栏输入http://localhost:9999/，在body内填写{"data":[1,2,3,4]}，点击send即可看到模型返回结果。
+ 参考：https://blog.csdn.net/NOT_GUY/article/details/116206692
