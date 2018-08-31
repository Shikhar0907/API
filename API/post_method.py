import json
import requests

def post_method():
    URL = 'http://httpbin.org/post'
    headers = {'Content-type':'application/json'}
    data = {"data":"22.32"}
    data_json = json.dumps(data)
    response = requests.post(URL,data= data_json,headers= headers)
    print(response.json())




def main():
    post_method()

main()
