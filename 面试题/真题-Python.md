# Python真题

## Python函数的*arg和**kwargs有什么区别？

在 Python 中，`*args` 和 `**kwargs` 主要用于函数的可变参数，它们的作用如下：

| 方式 | 类型 | 作用 | 传递的数据类型 |
|------|------|------|--------------|
| `*args` | 位置参数 | 接收多个 **位置参数** （参数数量不固定） | 元组 `tuple` |
| `**kwargs` | 关键字参数 | 接收多个 **关键字参数** （参数名和数量都不确定） | 字典 `dict` |

**示例：**
```python
def demo_args_kwargs(*args, **kwargs):
    print("args:", args)
    print("kwargs:", kwargs)

demo_args_kwargs(1, 2, 3, name="Alice", age=25) # kwargs要带关键字传进去
# 输出:
# args: (1, 2, 3)
# kwargs: {'name': 'Alice', 'age': 25}
# 函数内都需要解包才能取值使用

# 函数外传进去也可解包传进去
def greet(name, age):
    print(f"Hello, my name is {name} and I am {age} years old.")

# 通过 * 解包元组
info = ("Alice", 25)
greet(*info)

# 通过 ** 解包字典
info_dict = {"name": "Bob", "age": 30}
greet(**info_dict)
```

---

## Python中列表（list）、元组（tuple）、集合（set）有什么区别？

| 特性  | **列表（list）** | **元组（tuple）** | **集合（set）** |
|------|---------------|---------------|---------------|
| **可变性** | ✅ 可变（mutable） | ❌ 不可变（immutable） | ✅ 可变（mutable） |
| **是否允许重复元素** | ✅ 允许 | ✅ 允许 | ❌ 不允许 |
| **索引和切片** | ✅ 支持索引和切片 | ✅ 支持索引和切片 | ❌ 不支持 |
| **存储结构** | 有序（顺序存储） | 有序（顺序存储） | 无序（哈希表存储） |
| **元素访问速度** | 较快（索引访问 O(1)） | 最快（索引访问 O(1)） | 较慢（哈希查找 O(1)，但无索引） |
| **常见用途** | 存储可变数据，如列表、队列等 | 存储不可变数据，如数据库记录、键值对等 | 存储唯一值集合，去重、数学集合运算 |
| **定义方式** | `list1 = [1, 2, 3]` | `tuple1 = (1, 2, 3)` | `set1 = {1, 2, 3}` |
| **可哈希性（能否作为字典键）** | ❌ 不能哈希 | ✅ 可哈希（如果内部元素也可哈希） | ❌ 不能哈希 |

总结：
- **列表（list）**：有序、可变、允许重复，适合存储和修改数据。
- **元组（tuple）**：有序、不可变、允许重复，适合存储固定数据，性能更优。
- **集合（set）**：无序、可变、不允许重复，适合去重和数学集合操作（交集、并集、差集）。

---

## Python中import日志模块logging，logging.info("hello world")没有输出是为什么？
   
   **未正确配置 `logging`**
   - `logging` 默认的日志级别是 **WARNING**，所以 `logging.info("hello world")` 不会被输出（因为 `INFO` 级别低于默认的 `WARNING`）。



### **正确的使用方法**
#### **方法 1：快速配置**
```python
import logging

logging.basicConfig(level=logging.INFO)  # 设置最低级别为 INFO
logging.info("Hello, world!")
```
✅ **输出**
```
INFO:root:Hello, world!
```

#### **方法 2：自定义 Logger**
如果想自定义日志格式，或者创建不同的日志记录器（`logger`），可以这样做：

```python
import logging

# 创建 Logger
logger = logging.getLogger("my_logger")  # 自定义 logger 名称
logger.setLevel(logging.INFO)  # 设置日志级别

# 创建 Handler（控制台输出）
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)  # 确保 handler 允许 INFO 级别日志

# 设置日志格式
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
console_handler.setFormatter(formatter)

# 将 Handler 添加到 Logger
logger.addHandler(console_handler)

# 记录日志
logger.info("Hello, world!")
```
✅ **示例输出**
```
2025-02-12 10:00:00 - my_logger - INFO - Hello, world!
```

---
