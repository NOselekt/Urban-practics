import inspect
import sys
from typing import Any
from pprint import pprint
from Rep.Module_6.module_6_2.classes import Vehicle


def introspection_info(object_: Any):
    result = {'Type': type(object_),
              'Attributes': inspect.getmembers(object_, predicate=lambda x: not callable(x)),
              'Methods': inspect.getmembers(object_, predicate=callable),
              'Module': inspect.getmodule(object_), 'Size': sys.getsizeof(object_)}
    return result


veh = Vehicle('Dad', 'Supermodel', 'Red', 100)
number_info = introspection_info(42)

pprint(number_info)
pprint(veh)