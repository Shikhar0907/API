import requests

def fetching_api():
    data = requests.get("https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=4dbc17e007ab436fb66416009dfb59a8").json()
    articles = (data['articles'])
    for art in articles:
        print(art['title'])



def main():
    fetching_api()


main()
