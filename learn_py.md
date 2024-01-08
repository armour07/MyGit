

```python
# 注释注释
"""这是一段文档注释
111
222
"""
"""也可以这么写"""

# 文本切片，[a:b]包含 a 不包含 b
word == word[0:n] + word[n:len(word)]
word[0]
word[5]
word[:2]
word[0:2]
word[2:]
word[-2:]

# format 打印
a = 1
b = 2
print("a = {} b = {}".format(a, b))

for 循环
for v in list:
    print(v)

# 可通过 func 对数据进行修改，快速封装成新数组
new_list = [ func(i) for i in list]

2 ** 8 # = 2^8

'C:\name' # \n 会被转义
r'C:\name' # 则可以忽略转义

3 * 'a' + 'b' # 输出 aaab

# 利用 * 解参数，类似 lua 的 unpack(args)
args = [1, 5]
for i in range(*args):
    print(i)

# 利用 ** 解字典参数
def foo(a=0, b=0):
    return 'a = {} b = {}'.format(a, b)

arg = {'a': 1, 'b': 2}
print(foo(**arg))

# * 接收数组， ** 接收字典， * 必须在 ** 后面
def test(*b, **c):
    for bb in b:
        print(bb, end=', ')
    print()
    print('*' * 40)
    for cc in c:
        print(cc, ':', c[cc])

test('a', 'b', 'c', a=1, b=2, c=3)

# 函数参数限制
# test(0) or test(arg=0)
def test(arg):
    pass

# test(0)
def test(arg, /):
    pass

# test(arg=0)
def test(*, arg):
    pass

# test(1, 2, 3, d=4) or test(1, 2, c=3, d=4)
def test(a, b, /, c, *, d):
    pass


# lambda 表达式
def foo():
    return lambda x: x + 1

f = foo()
print(f(1))

# 实现队列，推荐使用 collections.deque，而非 list.remove(0)
from collections import deque

queue = deque(['a', 'b', 'c'])
queue.append('e')
queue.append('f')

print(queue.popleft())
print(queue)
a
deque(['b', 'c', 'e', 'f'])

print(queue.popleft())
print(queue)
b
deque(['c', 'e', 'f'])

for q in queue:
    print(q)

# del 删除元素
l = [1, 2, 3]
del l[0] # [2, 3]

# 元组 tuple，数组可以改变，元组不可以
t = (111, '222', 333)
print(t)

# 集合，集合是由不重复元素组成的无序容器
a = {'a', 'b', 'c'}
b = {'b', 'c', 'd'}

print(a)        # {'c', 'b', 'a'}
print(b)        # {'c', 'b', 'd'}
print(a & b)    # {'c', 'b'}
print(a | b)    # {'c', 'a', 'b', 'd'}
print(a - b)    # {'a'}
print(a ^ b)    # {'a', 'd'}

# 字典
a = {'a': 1, 'b': 2, 'c': 3}
b = dict([('a', 1), ('b', 2), ('c', 3)])
c = dict(a=1, b=2, c=3)

# 循环技巧
# dict.items() 可以同时提取键值
for k, v in a.items():
    print(k, v)

# list 可以用 enumerate 来提取键值
for i, v in enumerate(l):
    print(i, v)

# zip 可以同时遍历两个数组，以其中最低数量为准
list1 = ['a', 'b', 'c']
list2 = ['d', 'e', 'f', 'g']

for l1, l2 in zip(list1, list2):
    print(l1, l2)

# reversed 反向遍历
for i in reversed(range(5)):
    print(i) # 输出 4 3 2 1 0

# sorted 排序遍历
list = ['a', 'd', 'e', 'b', 'c']

for l in sorted(list):
    print(l) # 输出 a b c d e
    
# sorted + set 实现唯一 + 排序
list = ['a', 'd', 'e', 'b', 'c', 'a', 'b']

for l in sorted(set(list)):
    print(l) # 输出 a b c d e


# 普通类
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

# 枚举类
from Enum import enum
class Color(Enum):
    Red = 0
    Green = 1
    Blue = 2


# dir 获取该模块定义的所有名称，有序，没有参数时列出当前模块
dir(module)

# f'sss {自定义数据} sss'
import math
# :.nf 四舍五入
print(f'pi = {math.pi:.3f}')

# format
print('a b {} d {} f'.format('c', 'e'))
print('a b {1} d {0} f'.format('e', 'c'))
print('a b {c} d {d} f'.format(c='c', e='e'))


# 读写文件 r 只读 w 只写 r+ 读写 a 追加
with open('test.py', 'r+', encoding='utf-8') as f:
    read_data = f.read()
    f.write(read_data)
    f.close()
```

PyQt5 相关
```
pyuic5 .\main_window.ui -o main_window.py
pylupdate5.exe .\main_window.py -ts cn.ts
```
type hints
```python

from typing import TypeVar, Type
T = TypeVar('T')
T = TypeVar('T', int, str)  # 指定只能 int 或 str == union[int, str]
T = TypeVar('T', bound=BaseUI) # 指定是 BaseUI 的子类


def test(cls: Type[T]) -> T {

}

test(Actor).xxx

from typing import Iterable
# 返回只读
def get_all_comps() -> Iterable[Component] {

}

# 提高 dict,tuple 可读性
from typing import TypedDict
from typing import TypedTuple

class Employee(TypedDict):
    name: str
    age: int

class Vector3(TypedTuple):
    x: float
    y: float = 0
    z: float = 0

```

```python
import json
self.config = {
    'language': LanguageType.CN.value,
}
with open(json_config_path, 'w') as f:
    json.dump(self.config, f)

with open(json_config_path, 'r') as f:
    self.config = json.load(f)
```
```python
import configparser

config = configparser.ConfigParser()
config['mysql'] = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'password': '123456',
}
with open(ini_config_path, 'w') as f:
    config.write(f)

config = configparser.ConfigParser()
config.read(ini_config_path)

sections = config.sections()
print(sections)
option = config.options(sections[0])
print(option)
value = config.get(sections[0], option[0])
print(value)
item = config.items(sections[0])
print(item)

config.add_section('test')
config.set('test', 'name', 'kk')
config.set('test', 'age', '20')

with open(ini_config_path, 'w') as f:
    config.write(f)
```
```python
from PyQt5.QtCore import QThread, pyqtSignal, QMutex, QWaitCondition

class Thread(QThread):
    tirgger = pyqtSignal(str)

    def __init__(self, parent):
        QThread.__init__(self, parent)
        self.working = True
        self.idx = 0
        self.mutex = QMutex()
        self.condition = QWaitCondition()
        self.paused = False
        self.stop_flag = False

    def __del__(self):
        self.working = False
        self.wait()

    def run(self):
        while not self.stop_flag:
            self.mutex.lock()
            if self.paused:
                self.condition.wait(self.mutex)
            self.mutex.unlock()

            self.tirgger.emit(str(self.idx))
            self.idx += 1
            time.sleep(1)

    def pause(self):
        self.paused = True

    def resume(self):
        self.paused = False
        self.condition.wakeAll()

    def stop(self):
        self.stop_flag = True
```

```python
from functools import cache

@cache
def test():
    a = 0
    for i in range(1000000):
        a += i
    return a


if __name__ == "__main__":
    for i in range(4):
        start = time.time()
        test()
        print(time.time() - start)
```
不加 cache
0.11799931526184082
0.11803150177001953
0.11703777313232422
0.11702966690063477
加 cache
0.11800050735473633
0.0
0.0
0.0

```python
import inspect

def test(a, b, c=1):
    return a + b + c

sig = inspect.signature(test)
print(sig)
for name, param in sig.parameters.items():
    print(name, param.kind, param.default)

# (a, b, c=1)
# a POSITIONAL_OR_KEYWORD <class 'inspect._empty'>
# b POSITIONAL_OR_KEYWORD <class 'inspect._empty'>
# c POSITIONAL_OR_KEYWORD 1
```
```python
import psutil

# 遍历所有运行中的进程
for proc in psutil.process_iter(['name']):
    print(proc.info['name'])
    # 检查进程名是否为 'UE'
    if proc.info['name'] == 'UnrealEditor.exe':
        print('UE is running')
        break
else:
    print('UE is not running')
```

```python
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(('8.8.8.8', 53))  # UDP 连接，利用谷歌 DNS 服务器，但不发送数据，只连接
print(f'ip: {s.getsockname()[0]} port: {s.getsockname()[1]}')
s.close()

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
print(f'hostname: {hostname} ip: {ip}')

interfaces = socket.getaddrinfo(socket.gethostname(), None)
for interface in interfaces:
    print(f'ip: {interface[4][0]} port: {interface[4][1]}')
```

@classmethod 是 Python 中的一个装饰器，用于定义类方法。类方法是一种特殊的方法，它与实例方法不同，可以直接通过类名调用，而不需要先创建类的实例。类方法通常用于实现与类相关的操作，例如创建类的实例、访问类的属性等。

@classmethod 装饰器的语法如下：
```python
class MyClass:
    @classmethod
    def my_class_method(cls, arg1, arg2, ...):
        # 方法体

class Person:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year

    @classmethod
    def from_birth_year(cls, name, birth_year):
        age = datetime.date.today().year - birth_year
        return cls(name, age)

person = Person.from_birth_year('Alice', 1990)
print(person.name)  # 输出 'Alice'
print(person.birth_year)  # 输出 31
```