#!/usr/bin/env python3
"""
A script to determine range of ids to return for a particular
page.
"""


def index_range(page, page_size):
    """
    A script to determine range of ids to return for a particular
    page.
    """
    res = []
    res.append((page - 1) * page_size)
    res.append((res[0] + page_size))
    return (res[0], res[1])
