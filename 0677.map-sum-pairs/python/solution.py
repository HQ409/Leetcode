# -*- coding: utf-8 -*-

class MapSum:

    def __init__(self):
        self.d = {}

    def insert(self, key: str, val: int) -> None:
        self.d[key] = val

    def sum(self, prefix: str) -> int:
        return sum(v for k, v in self.d.items() if k.startswith(prefix))