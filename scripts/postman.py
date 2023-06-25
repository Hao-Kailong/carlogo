import requests


def carlogoPredict():
    resp = requests.post(
        url='http://127.0.0.1:27081/api/predict',
        json={
            'fileID': 'cloud://prod-4g4980u9c357bad5.7072-prod-4g4980u9c357bad5-1309812088/userUpload/hmeOlWhMDPMq5b915ca16c5c117e1a2c8b80c33b3d10',
            'placeholder': 'love',
        }
    )
    print(resp)
    print(resp.json())



carlogoPredict()

