'''
测试flask部署的模型
'''

from datetime import datetime
import requests
import numpy as np

starttime = datetime.now()


def predict():

    print("="*5,"数据处理部分","="*5)
    # text_path = "./test_files/000.txt"  # 文本路径

    # content = [] # 临时存储文本
    # with open(text_path, 'r', encoding='utf-8') as f:
    #     content = f.readlines()
    #
    # line = ''.join(content)
    x = [str(i) for i in np.random.random((1, 6))[0]]
    data = {"input": ",".join(x)}
    headers = {
        'Connection': 'close',
        }

    r = requests.post('http://127.0.0.1:8000/predict', data=data, headers=headers)
    print("r: ",r)
    print()
    print("="*5,"模型预测结果","="*5)
    if str(r.status_code) == '200':
        print("status: ",r.status_code," ","返回值: ", r.text)
    else:
        print("status: ",r.status_code)


    endtime = datetime.now()
    time_consume = endtime - starttime
    print('敏感词检测完成，共用时{}'.format(time_consume))

predict()





