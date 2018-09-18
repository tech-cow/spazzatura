#!/usr/bin/python
# -*- coding: utf-8 -*-

from random import *
from statistics import *
from collections import *


def shaoling():
    # 偷一次
    l = choices(['被发现了', '得到天山大便掌', '得到东北娘们掌', '得到拈花指','得到易筋经'],[50, 5,5,1,1])

    # 偷k次
    c = Counter(choices(['被发现了', '天山大便掌', '东北娘们掌', '拈花指','易筋经'],[50, 5,5,1,1], k = 6))
    print(c)

if __name__ == '__main__':
    shaoling()
