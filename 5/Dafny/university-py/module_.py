import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import module_
import _dafny
import System_

assert "module_" == __name__
module_ = sys.modules[__name__]

class Mark:
    def  __init__(self):
        self.numerical: int = int(0)
        self.national: int = int(0)
        pass

    def __dafnystr__(self) -> str:
        return "_module.Mark"
    def ctor__(self, num):
        if ((0) <= (num)) and ((num) < (60)):
            (self).national = 2
        elif ((60) <= (num)) and ((num) < (75)):
            (self).national = 3
        elif ((75) <= (num)) and ((num) < (90)):
            (self).national = 4
        elif ((90) <= (num)) and ((num) <= (100)):
            (self).national = 5
        (self).numerical = num


class default__:
    def  __init__(self):
        pass

    def __dafnystr__(self) -> str:
        return "_module._default"
    @staticmethod
    def Main(noArgsParameter__):
        d_0_mark_: module_.Mark
        nw0_ = module_.Mark()
        nw0_.ctor__(100)
        d_0_mark_ = nw0_

