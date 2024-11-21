import requests
import platform
from os import getlogin
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import QMainWindow, QApplication

api_url = 'https://api.api-ninjas.com/v1/randomword'
app_id = '5850c05b'
dict_key = '2a9ba447-8520-4efc-859a-c40da7b948d9'

word = ''

response = requests.get(api_url, headers={'X-Api-Key': 'bI9iehDklfwNst+JsMH4lw==rVhU5hONdQ40Cvew'})
if response.status_code == requests.codes.ok:
    word = response.json()
    word = word['word'][0]

else:
    print("Error:", response.status_code, response.text)

url = f"https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={dict_key}"

meaning_resp = requests.get(url, headers={
    "X-RapidAPI-Key": dict_key,
    "X-RapidAPI-Host": "wordsapiv1.p.rapidapi.com"
})

data = meaning_resp.json()
meaning = data[0]
meaning_ = meaning['shortdef'][0]
print(meaning_)

username = ''
system_ = platform.uname().system

username = getlogin()

fields = ['$word', '$meaning', '$username']
val = [word, meaning_, username]

with open('index.html', 'r') as content:
    con_ = content.read()
    for index, field in enumerate(fields):
        con_ = con_.replace(field, val[index])
        content.close()



class Window(QMainWindow):
    def __init__(self, content: str):
        super().__init__()

        self.setWindowTitle("Dictionary")
        self.engine_view = QWebEngineView()        
        self.engine_view.setHtml(content)

        self.engine_view.show()


app = QApplication()
window = Window(con_)
window.setWindowTitle("Today's Word")
app.exec()