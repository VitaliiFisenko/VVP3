class BaseCumstomException(Exception):
    pass


class CumstomStrException(BaseCumstomException):
    def __init__(self):
        super().__init__('НЕврерный тип')
