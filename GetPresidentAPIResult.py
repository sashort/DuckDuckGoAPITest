"""
S. Andy Short
CSC 256.001
L09 - DuckDuckGo
11/6/22
"""

import re
import requests


def local_presidential_set():
    # load a list of the president names from a local text file.
    # Spaces are replaced by underscores, and any initial has a period after it.
    with open("PresidentsList.txt") as file:
        return set([line.rstrip().replace(' ', '_') for line in file])


def duckduckgo_presidential_api_search_set():
    # formatted query for the DuckDuckGo API using the search term "presidents of the united states"
    ddg_api_endpoint_url = "https://duckduckgo.com/?q=presidents+of+the+united+states&format=json&pretty=1&no_html=1&skip_disambig=1"

    # store the json response for the query
    response_json = requests.get(ddg_api_endpoint_url).json()

    # create a set to dump and return results
    presidential_set = set()

    # loop through each match found in the "RelatedTopics" root key
    for key in response_json["RelatedTopics"]:
        # Extract each president's name from the "Result" url subkey.

        # NOTE: extraneous names and articles appear in this list.
        # NOTE: extracted names replace spaces with underscores,
        #       use correct capitalization, and initials are followed with a period.
        #       Example: S._Andy_Short
        presidential_set.add(re.search(r'<a href="https://duckduckgo.com/(.*?)">', key["Result"]).group(1))

    return presidential_set
