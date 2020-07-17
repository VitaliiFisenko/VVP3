import errors
from tools import is_odd
import random
UNIT = 5
aaaaaa = is_odd
if __name__ == '__main__':
    res = aaaaaa(random.randint(1, 100))
    print(res)
    try:
        aaaaaa((1,2,3))
    except errors.CumstomStrException as e:
        print(e)