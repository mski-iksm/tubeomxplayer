tubeomxp
=========
Automatic Youtube player for raspberry pi.<br>
Plays youtube videos by using youtube-dl and omxplayer.<br>
Although this software use youtube-dl, videos are played by streaming instead of downloading video files (due to leagal restrictions).


Dependencies
------
You need following packages/libraries to use this code.

* python3
* [youtube-dl](https://rg3.github.io/youtube-dl/download.html)
* [omxplayer](https://github.com/popcornmix/omxplayer)
* Google API Client Library `pip install --upgrade google-api-python-client`

Also, you need to get a Youtube Developer's API v3 key.
Instructions are described in the following link.
[https://developers.google.com/youtube/v3/getting-started](https://developers.google.com/youtube/v3/getting-started)


Usage
------
* Searching and playing video is posiible with follwing code: `python youtube_search.py -q [serch terms] -k [youtube API key]`
* Example `python youtube_search.py -q 宇多田ヒカル -k XXXXXXXXXXXXXXXXXXXXX`


```
HELP:
Stream video by passing URLs of Youtube search result to omxplayer.

optional arguments:
  -h, --help            show this help message and exit
  -q QUERY, --query QUERY
                        Search term. REQUIRED.
  -k KEY, --key KEY     Developer key for Youtube API v3. REQUIRED.
  -r MAX_RESULTS, --max_results MAX_RESULTS
                        Max results. If not set, 1.
  -m MODE, --mode MODE  Video play mode. "video". Mode for playing playlist
                        will be supported in the future update.
```