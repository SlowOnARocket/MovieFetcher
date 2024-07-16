# MovieFetcher

**MovieFetcher** is a software tool that retrieves torrents from yts.mx's API using your RapidAPI key and fetches the torrent content based on the IMDb ID of the movie.

## Features
- Fetch movie torrents directly from yts.mx
- Use your RapidAPI key for secure and efficient access
- Retrieve torrents by simply providing the IMDb ID of the desired movie
- Fast and reliable performance

## Requirements
- Python 3.x
- RapidAPI account and key
- Internet connection
- `requests` library (version 2.22.0)
- `PyBitTorrent` library (version 0.5.6)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/SlowOnARocket/MovieFetcher.git
   cd MovieFetcher
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. **Set Up Your RapidAPI Key:**

   Sign up on [RapidAPI]([https://rapidapi.com/](https://rapidapi.com/theapiguy/api/yts-am-torrent)) and subscribe to the yts.mx API. Obtain your API key.

2. **Update the API Key:**

   Replace the placeholder API key in the script with your own RapidAPI key:
   ```python
   headers = {
       "x-rapidapi-key": "YOUR_RAPIDAPI_KEY",
       "x-rapidapi-host": "yts-am-torrent.p.rapidapi.com"
   }
   ```

3. **Run the Script:**

   Execute the script and follow the prompts to input the IMDb ID and the output directory where you want to save the movie/torrent content:
   ```bash
   python moviefetcher.py
   ```

4. **Example Usage:**

   When prompted, enter the IMDb ID of the movie (e.g., `tt0111161` for "The Shawshank Redemption") and specify the output directory.
   The imdb id starts with tt and is located in the movie's url.

## Troubleshooting
- Ensure you have a stable internet connection.
- Verify your RapidAPI key is correct and has the necessary permissions.
- Check for typos in the IMDb ID.

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.

## Contact
For any questions or support, please open an issue on the GitHub repository.

---

**Happy movie fetching with MovieFetcher!**

## Code Structure
Here is a brief explanation of the code structure:

```python
import os
import requests
import re
import random
from PyBitTorrent.Bittorrent import TorrentClient

# Prompt user for IMDb ID and output directory
imdbd = input("what is the imdb id of the movie: ")
outd = input("where to save the Movie/Torrents content: ")

# Setup API request
url = "https://yts-am-torrent.p.rapidapi.com/movie_details.json"
querystring = {"imdb_id": imdbd}
headers = {
    "x-rapidapi-key": "YOUR_RAPIDAPI_KEY",
    "x-rapidapi-host": "yts-am-torrent.p.rapidapi.com"
}

try:
    # Make API request
    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()
    print(str(data))

    # Extract torrent URL
    urls = re.findall(r"https://yts\.mx/torrent/download/[A-Z0-9]+", str(data))
    dl = urls[2]
    print("1080p URL")
    print(dl)
    trdl = requests.get(dl)
    randint = random.randint(0, 10000)

    # Save the torrent file
    if trdl.status_code == 200:
        with open(f'movie{randint}.torrent', 'wb') as f:
            f.write(trdl.content)
        print(f"file downloaded as movie{randint}.torrent!")
        print("getting the torrent's content...")

        def main():
            torrent_client = TorrentClient(torrent=f"movie{randint}.torrent", max_peers=200, use_progress_bar=False, output_dir=outd)
            # Start downloading the file
            print("Started Downloading content!")
            torrent_client.start()

        if __name__ == '__main__':
            main()
            os.remove(f"movie{randint}.torrent")

except:
    exit("Error: No Torrent available or closed by user input.")
```

## `requirements.txt`
```plaintext
requests~=2.22.0
PyBitTorrent~=0.5.6
```
