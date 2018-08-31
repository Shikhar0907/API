import requests
import sqlite3

def finder():
    URL = "https://api.github.com/users"
    req = requests.get(URL).json()
    for item in req:
        insert_table(item['login'],item['id'],item['url'])

def sql_link():
    conn = sqlite3.connect('github.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS git
                ( LOGIN TEXT(50) NOT NULL,
                ID INTERGER,
                URL TEXT(70))
                ''')
    
def insert_table(login,user_id,url):
    conn = sqlite3.connect('github.db')
    con = conn.cursor()
    con.execute("insert into git(LOGIN,ID,URL) values (?,?,?)",(login,user_id,url))
    conn.commit()
    
def select_data():
    conn = sqlite3.connect('github.db')
    con = conn.cursor()
    con.execute("select * from git")
    select = []
    select = (con.fetchall())
    for item in select:
        print(item)


def main():
    sql_link()
    finder()
    select_data()

main()
