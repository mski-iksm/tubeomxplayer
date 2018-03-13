#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""Code for streaming video from Youtube.

Works on raspberry pi with omxplayer installed.
You also need Youtube Data API v3 secr
Refer to the following URL for more information.
https://developers.google.com/youtube/v3/getting-started

USAGE:
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
"""

from apiclient.discovery import build
import argparse
import os
import numpy as np

YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"


def youtube_search(options):
    """Main youtube serch function."""
    DEVELOPER_KEY = options.key
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                    developerKey=DEVELOPER_KEY)

    # Call the search.list method to retrieve results matching the specified
    # query term.
    search_response = youtube.search().list(
        q=options.query,
        part="id,snippet",
        maxResults=options.max_results
    ).execute()

    video_urls = []
    video_names = []

    if options.mode == "video":
        for search_result in search_response.get("items", []):
            if search_result["id"]["kind"] == "youtube#video":
                video_urls.append("https://www.youtube.com/watch?v={}".
                                  format(search_result["id"]["videoId"]))
                video_names.append(search_result["snippet"]["title"])
    if options.mode == "playlist":
        for search_result in search_response.get("items", []):
            if search_result["id"]["kind"] == "youtube#playlist":
                video_urls.append("https://www.youtube.com/playlist?list={}".
                                  format(search_result["id"]["playlistId"]))
                video_names.append(search_result["snippet"]["title"])

    return [video_urls, video_names]

parser = argparse.ArgumentParser(description='Stream video by passing URLs of \
                                 Youtube search result to omxplayer.')
parser.add_argument("-q", "--query", help="Search term. REQUIRED.",
                    default="Google", required=True)
parser.add_argument("-k", "--key",
                    help="Developer key for Youtube API v3. REQUIRED.",
                    required=True)
parser.add_argument("-r", "--max_results", help="Max results. If not set, 1.",
                    default=1, type=int)
parser.add_argument("-m", "--mode",
                    help='Video play mode. "video". Mode for playing playlist\
                     will be supported in the future update.', default="video")

args = parser.parse_args()
print(args)

video_url_list, video_name_list = youtube_search(args)

for i in np.arange(len(video_url_list)):
    print(video_name_list[i])
    os.system("sh {}/youtube.sh '{}'".
              format(os.path.dirname(os.path.abspath(__file__)),
                     video_url_list[i]))
