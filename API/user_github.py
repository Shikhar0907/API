import requests

def finder():
    URL = "https://api.github.com/users/"
    user = str(input("Please enter the user: "))
    URL = URL + user + "?"
    CLIENT_ID = "be6ccef3338558eb2cf6"
    CLIENT_SECRET = "439f9ecd8e6a1cb006784ed7528765b5bdf86949"
    param = {'client_id': CLIENT_ID,'client_secret':CLIENT_SECRET}
    re = requests.get(URL,params=param)
    
    data = re.json()
    find_repo(data)

def find_repo(data):
    login = data['login']
    user_id = data['id']
    URL = data['repos_url']
    print(login,user_id,URL)
    re = requests.get(URL).json()
    for item in re:
        print(item['id'],item['name'],item['description'])
    
    
    
    
    

def main():
    finder()

main()
