# a = True
# print(a)
# print(r'a\nb')  # r加在前面表转义符不起作用


# 字符串与编码
# print(ord("中"))
# print(chr(123))

# 字符串与byte
# print('ABC'.encode('ascii'))
# print(b'a')
# print('中文'.encode('utf-8'))
# print(b"\xe4\xb8\xad\xe6\x96\x87".decode('utf-8', errors='ignore'))
# print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125))
# print('Hello, {1}, 成绩提升了 {1:.1f}%'.format('小明', 17.125))
# print('')

# 条件语句与循环语句
# age = 20
# if age >= 18:
#     print('your age is', age)
#     print('adult')
#
# birth = input('birth: ')
# birth = int(birth)
# if birth < 2000:
#     print('00前')
# else:
#     print('00后')
#
# for i in range(10, 13):
#     print(i)
# d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
# d.pop()

s = ([1,2,3]);
for i in s:
    print(i)