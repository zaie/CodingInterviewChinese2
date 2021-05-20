# 解法1 有限状态自动机
def isNumber(s):
    states = [
        { ' ': 0, 's': 1, 'd': 2, '.': 4 }, # 0. start with 'blank'
        { 'd': 2, '.': 4 } ,                # 1. 'sign' before 'e'
        { 'd': 2, '.': 3, 'e': 5, ' ': 8 }, # 2. 'digit' before 'dot'
        { 'd': 3, 'e': 5, ' ': 8 },         # 3. 'digit' after 'dot'
        { 'd': 3 },                         # 4. 'digit' after 'dot' (‘blank’ before 'dot')
        { 's': 6, 'd': 7 },                 # 5. 'e'
        { 'd': 7 },                         # 6. 'sign' after 'e'
        { 'd': 7, ' ': 8 },                 # 7. 'digit' after 'e'
        { ' ': 8 }                          # 8. end with 'blank'
    ]
    print('状态states 长度为：',len(states))
    p = 0                           # start with state 0
    print('字符串s 的总长度为：',len(s))
    for c in s:
        if '0' <= c <= '9': 
            t = 'd' # digit
            print('当前字符c=%s,\t属于 数字digit'%c)
        elif c in "+-": 
            t = 's'     # sign
            print('当前字符c = %s,\t属于 正负号sign'%c)
        elif c in "eE": 
            t = 'e'     # e or E
            print('当前字符c = %s,\t属于 幂符号e'%c)
        elif c in ". ": 
            t = c       # dot, blank
            print('当前字符c = %s,\t属于 小数点.dot'%c)
        else: 
            t = '?'               # unknown
            print('当前字符c = %s,Unknown'%c)
        if t not in states[p]: 
            return False
        print('当前状态p =',p,end='\t')
        print('记录字符t =',t)
        p = states[p][t]
        print('故得到新状态p =',p,end='\t')
        print('跳转到states[%s]的字典中 找下一个状态\n'%p)
    return p in (2, 3, 7, 8)

if __name__ == "__main__":
    s = '5.2e-3'
    print(isNumber(s))

# 解法2
def is_numeric(string):
    if not isinstance(string, str):
        return False

    index = 0
    result, index = scan_integer(string, index)
    if index < len(string) and string[index] == '.':
        index += 1
        has_float, index = scan_unsigned_integer(string, index)
        result = result or has_float

    if index < len(string) and string[index] in ('e', 'E'):
        index += 1
        has_exp, index = scan_integer(string, index)
        result = result and has_exp
    return result and index == len(string)


def scan_integer(string, index):
    if index < len(string) and string[index] in ('-', '+'):
        index += 1
    return scan_unsigned_integer(string, index)


def scan_unsigned_integer(string, index):
    old_index = index
    while index < len(string) and string[index] in '0123456789':
        index += 1
    return (old_index != index), index


if __name__ == "__main__":
    print(is_numeric("+100"))
    print(is_numeric("5e2"))
    print(is_numeric("-200"))
    print(is_numeric("3.1415926"))
    print(is_numeric("1.34e-2"))
    print(is_numeric("1.34e"))

