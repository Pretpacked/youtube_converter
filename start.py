#
# made by:              Pretpacked
# creation date:        04-10-2019
# purpose:              Exporting music from youtube faster and auto download.
#

from __future__ import unicode_literals
import youtube_dl
import requests
from bs4 import BeautifulSoup
import urllib.parse

class converter():

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl':'music/%(title)s-%(id)s.%(ext)s'
    }

    def __init__(self):
        self.songname = input("song name: ")
        self.main()

    def convert(self, info):
        with youtube_dl.YoutubeDL(self.ydl_opts) as ydl:
            ydl.download([info["href"]])

    def main(self):
        try:
            self.songsArray = [{}]
            print("searching for '{song}' on youtube\n".format(song= self.songname))

            i = 0
            page = requests.get("https://www.youtube.com/results?search_query={filter}".format(filter=urllib.parse.quote(self.songname.encode('utf-8'))))
            soup = BeautifulSoup(page.content, 'lxml')
            for elem in soup.find_all(("a", {"id" : "video-title"})):
                if "watch?v=" in elem.get("href") and elem.get("title"):
                    i = i + 1
                    print("{number} - {title}".format(number=i,title=elem.get('title')))
                    self.songsArray[0][i] = {"title":elem.get('title'),"href":"https://www.youtube.com{}".format(elem.get('href'))}

            print("\n[0] - other song.")
            self.songNumberChoosen = int(input("\nsong number: "))

            if not self.songNumberChoosen == 0:
                self.convert(self.songsArray[0][self.songNumberChoosen])
            else:
                self.__init__()

        except:
            print("Error, please try again")
            self.main()

if __name__ == "__main__":
    converter()