import errors


def is_odd(num):
    if isinstance(num, (str, tuple)):
        raise errors.CumstomStrException()
    if type(num) == str or type(num) == tuple:
        raise errors.CumstomStrException()
    if any((type(num) == str, type(num) == tuple)):
        raise errors.CumstomStrException()
    return num % 2 == 0
