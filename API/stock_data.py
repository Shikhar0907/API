import requests


def alpha_vantage():
    URL = "https://www.alphavantage.co/query?"
    sym = str(input("Please enter the symbol code: "))
    func = 'TIME_SERIES_WEEKLY'
    key = 'YQFZQT7LLOM4UX92'
    Param = {'function': func ,'symbol' : sym,'apikey' : key}
    r = requests.get(url=URL,params=Param)
    data = r.json()
    print(data['Weekly Time Series'].items())


def main():
    alpha_vantage()

main()
