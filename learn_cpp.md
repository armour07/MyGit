## ::

```cpp
using namespace std;

int x;

int main()
{
    int x = 10;
    return 0;
}
// ::x = 0
// x = 10
```

a.h
```cpp
class A
{
public:
    void fun();
}
```
a.cpp
```cpp
#include "a.h"
#include "iostream"
using namespace std;
void A::fun()
{
    cout << "call func" << endl;
}

int main()
{
    A a;
    a.fun();
    return 0;
}
```

## 宏

### 定义宏
```cpp
#difine PI 3.141592635
#define NULL ((void*)0)
#define SYSTEM_API

double p = d * 3.1415926535 => double p = d * PI
class SYSTEM_API CSystem; => class CSystem;
```

### 参数
```cpp
#define MUL(x, y) x * y
int ret = MUL(2, 3); => int ret = 2 * 3;
int ret = MUL(2 + 3, 4); => int ret = 2 + 3 * 4
//修复
#define MUL(x, y) (x) * (y)
int ret = MUL(2 + 3, 4); => int ret = (2 + 3) * (4)

#define ADD(x, y) (x) + (y)
int ret = Add(2, 3) * ADD(4, 5) => int ret = 2 + 3 * 4 + 5
// 修复
#define ADD(x, y) ((x) + (y))
int ret = ADD(2, 3) * ADD(4, 5) => int ret = (2 + 3) * (4 + 5)

```
### 符号 # 和 ##
```cpp
#define STRING(x) #x
const char* str = STRING(test); => const char* str = "test";

#define VAR(index) INT_##index
int VAR(1); => int INT_1;
```
### 可变参数
```cpp
#define TRACE(fmt, ...) printf(fmt, ##__VA_ARGS__)
TRACE("goto a number %d", 35);
```
### 多行
```cpp
#define ADD(x, y) do { int sum = (x) + (y); return sum; } while (0)

#define ADD(x, y) \
do \
{ \
    int sum = (x) + (y); \
    return sum; \
} while (0)
```
### 取消宏定义
```cpp
#undef ADD
```
### 判断宏
```cpp
ifdef _WIN32
    OutputDebugString("this is a windows log");
#else
    NSLog(@"this is a mac log");
#endif

#if defined(_WIN32) || defined(WIN32)
    OutputDebugString("this is a windows log");
#endif
```
#ifdef 有宏就 true，#if 则需要判断宏的内容，必须为整数
```cpp
// 1 会触发打印
#define ENABLE_LOG 1
#if ENABLE_LOG
    trace("when enabled then print this log")
#endif

// 0 不会触发打印
#define ENABLE_LOG 0
#if ENABLE_LOG
    trace("when enabled then print this log")
#endif
```
### 打印错误信息
`__FILE__`：输出文件名

`__LINE__`：输出当前行数
```cpp
print("%s %d printf message %s \n", __FINE__, __LINE__, "some reason");

改成宏
#define trace(fmt, ...) printf("%s %d "fmt, __FILE__, __LINE__, ##__VA_ARGS__)

trace("printf message %s\n", "some reason");
```

### 常见的 do{}while(0)
```cpp
#define swapint(x, y) int temp = x; x = y; y = temp;

int x = 1, y = 2;
swapint(x, y);  // 编译正常

switch(value)
{
    case 1:
        swapint(x, y);  // 编译出错，switch 不允许声明变量
        break;
}
// 解决
#define swapint(x, y) {int temp = x; x = y; y = temp;}

if(x < y)
    swapint(x, y); // -> {int temp = x; x = y; y = temp;};  // 编译出错，else 前面多了分号
else
    action();

// 解决
#define swapint(x, y) do{int temp = x; x = y; y = temp;} while(0)


#define UE_PRIVATE_SCOPE_EXIT_JOIN(A, B) UE_PRIVATE_SCOPE_EXIT_JOIN_INNER(A, B)
#define UE_PRIVATE_SCOPE_EXIT_JOIN_INNER(A, B) A##B
#define ON_SCOPE_EXIT const auto UE_PRIVATE_SCOPE_EXIT_JOIN(ScopeGuard_, LINE) = ::ScopeExitSupport::FScopeGuardSyntaxSupport() + [&]()

ON_SCOPE_EXIT { GEnginePreInitPreStartupScreenEndTime = FPlatformTime::Seconds(); };

// 等于

const auto ScopeGuard_37 = ::ScopeExitSupport::FScopeGuardSyntaxSupport() + [&]() { GEnginePreInitPreStartupScreenEndTime = FPlatformTime::Seconds(); };

```
指针相关

```cpp
int a = 10;
// *a 不存在这种写法，*只能解析地址获取值，*&a
// &a 表示 a 的地址

// int* b 表示我只存储地址，不要给我值，如果传入 a 异常，只能 &a
int* b = &a;  // *b 可以解析这个地址指向的值，也就是 10

// int& c 会把指针指向 a，相当于就是 a，相当于两个键盘控制同一台电脑
int& c = a; // 只能是 a，不能 &a 或者 *a 但可以 *b





```