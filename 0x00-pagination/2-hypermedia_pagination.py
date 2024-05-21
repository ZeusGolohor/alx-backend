#!/usr/bin/env python3
"""
A script to implement pagination.
"""
import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        A method to implement pagination.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        res = []
        res.append((page - 1) * page_size)
        res.append((res[0] + page_size))
        data = self.dataset()
        return (data[res[0]: res[1]])

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
        Implement a get_hyper method that takes the same
        arguments (and defaults) as get_page
        """
        res = {}
        data = self.get_page(page, page_size)
        res["page_size"] = len(data)
        res["page"] = page
        res["data"] = data
        res["next_page"] = None
        data = self.dataset()
        res1 = []
        res1.append((page) * page_size)
        res1.append((res1[0] + page_size))
        if ((len(data[res1[0]: res1[1]]) > 0)):
            res["next_page"] = page + 1
        res["prev_page"] = None
        res2 = []
        res2.append((page - 2) * page_size)
        res2.append((res2[0] + page_size))
        if ((len(data[res2[0]: res2[1]]) > 0)):
            res["prev_page"] = page - 1
        res["total_pages"] = int(int(len(data)) / page_size)
        if ((int(len(data)) % page_size) > 0):
            res["total_pages"] += 1
        return (res)
