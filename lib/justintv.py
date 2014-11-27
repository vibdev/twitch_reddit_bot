#!/usr/bin/env python
'''
Define functions to query the twitch.tv and justin.tv streaming
websites.

More info on the Justin.TV REST api here:
  http://apiwiki.justin.tv/mediawiki/index.php/REST_API_Documentation
'''
import sys
import logging
import requests

'''
Justin.TV API stream listing request.  This API call takes a comma
separated list of channel names and returns an array of JSON objects,
one per channel that is currently streaming (so nothing is returned
for channels that were queried but aren't streaming)

   [{"login":"esltv_dota", ... many more properties ... }, ...]
'''
STREAM_URL = "https://api.twitch.tv/kraken/streams?channel=%s&oauth_token=qnqml16x2dce21yjt7t0zwml1qji08o"


# Takes an array of channel names and returns the names from the array
# which are currently streaming
def fetch_streams(channel_names):
    response = requests.get(STREAM_URL % (",".join(channel_names)))

    try:
        message = response.json()["streams"]
    except ValueError:
        # JSON Decode failed
        sys.exit("Invalid message from twitch.tv: %s" % (response.text))

    if not isinstance(message, list):
        sys.exit("Unexpected JSON from twitch.tv: %s" % (message))
    return message
