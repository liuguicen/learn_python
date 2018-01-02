
"我是这个module文件的文档，\n目前我没有任何内容。"

import sys


def test():
    args = sys.argv
    if len(args) == 1:
        print('hello world')
    elif len(args) == 2:
        print('hello %s' % args[1])
    else:
        print('too many arguments')


def _private_test():
    print('I am a private function which is should not to be reference')


if __name__ == '__main__':
    test()

print(__doc__)
