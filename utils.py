import functools
import gin


@gin.configurable
def gin_print(arg):
    return functools.partial(print, arg)


@gin.configurable
class TestClass:
    def __init__(self, arg):
        print("arg is ", arg)


@gin.configurable
def construct_class():
    return TestClass(arg=True)
