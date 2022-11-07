"""
S. Andy Short
CSC 256.001
L09 - DuckDuckGo
11/6/22
"""

import pytest
from GetPresidentAPIResult import *


# Tests to see if DuckDuckGo returns a list containing all the US presidents.
def test_all_presidents_found():
    local_pres_set = local_presidential_set()
    ddg_pres_set = duckduckgo_presidential_api_search_set()

    difference = local_pres_set - ddg_pres_set

    if len(difference) != 0:
        print("The following presidents were not found with a literal match in any URL:\n")
        print(str(difference).replace("{", "\t").replace(", ", "\n\t").replace("}", ""))
    else:
        print("\nAll " + str(len(local_pres_set)) + " presidents were found.")
    assert len(difference) == 0
