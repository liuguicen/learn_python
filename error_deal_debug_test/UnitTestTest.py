import unittest
from error_deal_debug_test.UnitTestTarget import MyDict


class TestMyDict(unittest.TestCase):
    def setUp(self):
        self.dict = MyDict(a='aaaa')

        print('setUp has run')

    def tearDown(self):
        print('data from setup', self.dict.a)

    def test_init(self):
        d = MyDict(a=1, b="xiaoming")
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, "xiaoming")
        print('finish test one')

    def not_test(self):
        print('not test')

    def test_key(self):
        d = MyDict()
        d['key'] = 'value'
        self.assertEqual('key' in d, False)
        self.assertEqual(d.key, 'value')

    def test_keyerror(self):
        d = MyDict()
        with self.assertRaises(KeyError):
            value = d['empty']
        print('finish test 3')

    def test_attrError(self):
        d = MyDict()
        with self.assertRaises(AttributeError):
            value = d.empty
