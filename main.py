import os

import requests
import re
import random
from PyBitTorrent.Bittorrent import TorrentClient
imdbd = input("what is the imbd id of the movie: ")
outd = input("where to save the Movie/Torrents content: ")
url = "https://yts-am-torrent.p.rapidapi.com/movie_details.json"

querystring = {"imdb_id": imdbd}

headers = {
    "x-rapidapi-key": "c0bead6f29msh4d9e7d3d14843aep13418ejsn36aca17680de",
    "x-rapidapi-host": "yts-am-torrent.p.rapidapi.com"
}
try:
    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()
    print(str(data))
    urls = re.findall(r"https://yts\.mx/torrent/download/[A-Z0-9]+", str(data))
    dl = urls[2]
    print("1080p URL")
    print(dl)
    trdl = requests.get(dl)
    randint = random.randint(0, 10000)
    if trdl.status_code == 200:
        with open(f'movie{randint}.torrent', 'wb') as f:
            f.write(trdl.content)
        print(f"file downloaded as movie{randint}.torrent!")
        print("getting the torrent's content...")

        def main():
            torrent_client = TorrentClient(torrent=f"movie{randint}.torrent", max_peers=200,
                                           use_progress_bar=False,
                                           output_dir=outd)

            # Start downloading the file
            print("Started Downloading content!")
            torrent_client.start()


        if __name__ == '__main__':
            main()
            os.remove(f"movie{randint}.torrent")

except:
    exit("Error: No Torrent available or closed by user input.")
