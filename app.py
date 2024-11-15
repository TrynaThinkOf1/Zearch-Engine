import requests
import eel

class Search:
    def __init__(self, url):
        self.url = url

    def search(self):
        print(f"Searching for {self.url} \n")

        if "https://" not in url:
            self.url = "https://" + self.url

        html = requests.get(self.url).text
        f = open("web/index.html", "w")
        f.write(html)
        f.close()

        eel.init("web")
        eel.start("index.html")

url = input("Enter the URL: ")

search = Search(url)
search.search()
