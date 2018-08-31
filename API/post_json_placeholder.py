import requests
import pprint


def json_post():
    URL = "https://jsonplaceholder.typicode.com/posts"
    r = requests.post(URL,data = {'userId':1,'title':"helllo Shikhar",'body':"This is test"})
    print(r.status_code,r.reason)
    pprint.pprint(r.json())



def main():
    json_post()


main()
