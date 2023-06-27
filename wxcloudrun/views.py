from datetime import datetime
from flask import render_template, request
from run import app
from wxcloudrun.dao import delete_counterbyid, query_counterbyid, insert_counter, update_counterbyid
from wxcloudrun.model import Counters
from wxcloudrun.response import make_succ_empty_response, make_succ_response, make_err_response
import requests
import logging
import random


# 初始化日志
logger = logging.getLogger('log')




@app.route('/')
def index():
    """
    :return: 返回index页面
    """
    return render_template('index.html')


@app.route('/api/count', methods=['POST'])
def count():
    """
    :return:计数结果/清除结果
    """

    # 获取请求体参数
    params = request.get_json()

    # 检查action参数
    if 'action' not in params:
        return make_err_response('缺少action参数')

    # 按照不同的action的值，进行不同的操作
    action = params['action']

    # 执行自增操作
    if action == 'inc':
        counter = query_counterbyid(1)
        if counter is None:
            counter = Counters()
            counter.id = 1
            counter.count = 1
            counter.created_at = datetime.now()
            counter.updated_at = datetime.now()
            insert_counter(counter)
        else:
            counter.id = 1
            counter.count += 1
            counter.updated_at = datetime.now()
            update_counterbyid(counter)
        return make_succ_response(counter.count)

    # 执行清0操作
    elif action == 'clear':
        delete_counterbyid(1)
        return make_succ_empty_response()

    # action参数错误
    else:
        return make_err_response('action参数错误')


@app.route('/api/count', methods=['GET'])
def get_count():
    """
    :return: 计数的值
    """
    counter = Counters.query.filter(Counters.id == 1).first()
    return make_succ_response(0) if counter is None else make_succ_response(counter.count)


@app.route('/api/predict', methods=['POST'])
def predict():
    """
    :return: knowledge
    """

    # 获取请求体参数
    params = request.get_json()
    logger.info('params: {}'.format(params))

    # 检查fileID参数
    if 'fileID' not in params:
        return make_err_response('缺少fileID参数')
    fileID = params['fileID']

    # 1.下载文件
    try:
        resp = requests.post(
            url='http://api.weixin.qq.com/tcb/batchdownloadfile',
            json={
                'env': 'prod-4g4980u9c357bad5',
                'file_list': [
                    {'fileid': fileID, 'max_age': 3600},
                ]
            }
        )
        data = resp.json()
        assert data['errcode'] == 0
        downloadUrl = data['file_list'][0]['download_url']    
        resp = requests.get(
            url=downloadUrl, 
            stream=True
        )
        if resp.status_code == 200:
            target = 'img_{:02d}.jpg'.format(random.randint(0, 99))
            with open(target, 'wb') as f:
                f.write(resp.content)
            logger.info('image save to {}'.format(target))
    except:
        return make_err_response('下载文件失败')

    # 2.模型预测
    try:
        from wxcloudrun.function import Factory
    except:
        logger.info('import ERROR SHIT')
        return {'index': 12, 'prob': 0.0, 'name': ''}

    # 初始化模型
    try:
        mobilenet = Factory.genMobilenet()
    except:
        return {'index': 45, 'prob': 0.0, 'name': ''}

    try:
        inputs = mobilenet.process(target)
        logger.warn('process finish')
        index, prob, name = mobilenet.predict(inputs)
        logger.warn('predict finish')
        logger.warn('predict: {} {} {}'.format(index, prob, name))

        return make_succ_response({
            'index': index[0],
            'prob': prob[0],
            'name': name[0],
        })
    except:
        print('predict ERROR SHIT')
        return {'index': 99, 'prob': 0.0, 'name': ''}

    # 3.读/写数据库

    # 4.返回结果




