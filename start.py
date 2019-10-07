#!/usr/bin/env python
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
import queue


class converter:

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': 'music/%(title)s-%(id)s.%(ext)s'
    }

    def __init__(self):
        self.songname = input("song name: ")
        self.main()

    def convert(self, info):
        with youtube_dl.YoutubeDL(self.ydl_opts) as ydl:
            ydl.download([info["href"]])

	again = input("\nConvert another song? [y][n]")
	if again == "y":
            self.__init__()

    def main(self):
        try:
            songsArray = {}
            print("searching for '{song}' on youtube\n".format(song=self.songname))

            page = requests.get("https://www.youtube.com/results?search_query={filter}".format(filter=urllib.parse.quote(self.songname.encode('utf-8'))))
            soup = BeautifulSoup(page.content, 'lxml')

            n = 0

            for elem in soup.find_all(("a", {"id": "video-title"})):
                if "watch?v=" in elem.get("href") and elem.get("title"):
                    n = n + 1
                    print("{number:>3} - {title}".format(number=n, title=elem.get('title')))
                    songsArray[n] = {"title": elem.get('title'), "href": "https://www.youtube.com{}".format(elem.get('href'))}

            print("\n[0] - other song.")
            songNumberChosen = int(input("\nsong number: "))

            if songNumberChosen:
                self.convert(songsArray[songNumberChosen])
            else:
                self.__init__()

        except ValueError:
            input("\nPlease choose a number from the list.\nPress enter...")
            self.main()
        except KeyError as num:
            input("\nThe number {} isn't a valid choice, please choose again.\nPress enter...".format(num))
            self.main()


# if run directly
if __name__ == "__main__":
    try:
        converter()
    except (KeyboardInterrupt, EOFError):
        print("\nKeyboard Interrupt")
        exit()
