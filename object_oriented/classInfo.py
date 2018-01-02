
type(123)

import types

def fn():

    pass

type(fn) == types.FunctionType
print(dir(fn))
print(getattr(fn, '__call__'))
print(hasattr(fn, 'abc'))