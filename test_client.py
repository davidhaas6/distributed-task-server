import requests
from time import sleep
import json

def dummy_task(data, poll_interval=1, max_attempts=10):
    base_uri = r'http://127.0.0.1:8080'

    predict_task_uri = base_uri + '/model/predict'

    task = requests.post(predict_task_uri, json=data)
    task_id = task.json()['task_id']

    predict_result_uri = base_uri + '/model/result/' + task_id

    attempts = 0
    result = None
    while attempts < max_attempts:
        attempts += 1
        result_response = requests.get(predict_result_uri)
        if result_response.status_code == 200:
            result = result_response.json()
            break
        sleep(poll_interval)
    return result


if __name__ == '__main__':
    mydata={'features': [1,2,3,4]}
    prediction = dummy_task(mydata)
    print(prediction)
