import requests


def getToken():
    resp = requests.get(
        'http://api.weixin.qq.com/cgi-bin/token',
        params={
            'grant_type': 'client_credential',
            'appid': 'wxd90035c7dc427924',
            'secret': 'Carlogo123',
        }
    )
    print(resp)
    print(resp.json())


def batchDownloadFile():
    resp = requests.post(
        'http://api.weixin.qq.com/tcb/batchdownloadfile',
        data={
            'env': 'prod-4g4980u9c357bad5',
            'file_list': [
                {'fileid': 'cloud://prod-4g4980u9c357bad5.7072-prod-4g4980u9c357bad5-1309812088/userUpload/sn7xWrI8Ffh21427c6caeeb17e7f2ae1a362d34e4530', 'max_age': 3600},
            ]
        }
    )
    print(resp)
    print(resp.json())



batchDownloadFile()
