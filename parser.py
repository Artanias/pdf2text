from abc import ABCMeta, abstractmethod


class Parser:

    def __init__(self):
        pass

    __metaclass__ = ABCMeta

    @abstractmethod
    def parse_document(self):
        """"""

    @property
    def path_to_document(self):
        return

    @property
    def path_to_json_out(self):
        return
