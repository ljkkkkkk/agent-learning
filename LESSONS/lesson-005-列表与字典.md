# Lesson 005：列表与字典（Python 基础 · 第三课）

> 本节课学 Python 最常用的两种**容器**：列表 `list`（有序的一排数据）和字典 `dict`（带名字标签的数据）。
> **预告**：以后大模型 API 返回的数据就是「字典套列表、列表套字典」的格式，这一课是 Agent 开发的地基。

---

## 1. 列表 list：有序的收纳盒

```python
fruits = ["苹果", "香蕉", "橙子"]   # 用方括号 [ ]，逗号分隔
```

**三个重点**：
1. **下标从 0 开始**：`fruits[0]` 是 "苹果"，`fruits[1]` 是 "香蕉"（不是从 1 开始！）
2. **负数下标**从末尾数：`fruits[-1]` 是最后一个 "橙子"
3. 可以**放不同类型的混合数据**：`mix = [1, "hello", 3.14, True]`

**常用操作**（写代码时最常用的 6 个）：

```python
fruits.append("西瓜")        # 末尾追加
fruits.insert(1, "葡萄")     # 插到下标 1 的位置
fruits[0] = "大苹果"         # 修改下标 0 的元素
fruits.remove("香蕉")        # 按内容删除
last = fruits.pop()          # 弹出并返回最后一个
print(len(fruits))           # 长度（有几个）
print("苹果" in fruits)      # True：判断在不在里面
print(fruits[1:3])           # 切片：下标 1 到 2（含头不含尾）
```

**遍历列表**（配合 for，最常用）：

```python
for f in fruits:
    print(f)
```

## 2. 字典 dict：带标签的柜子

列表用数字下标找东西，字典用**名字（键）**找东西：

```python
student = {"name": "小明", "age": 18}   # 花括号 { }，键: 值
print(student["name"])     # 小明（用键取值）
student["age"] = 19        # 修改已有键
student["city"] = "北京"    # 新增键
del student["city"]        # 删除键
```

**遍历字典**（3 种方式）：

```python
for key in student:                 # 只拿键
    print(key)
for key, value in student.items():  # 键值一起拿（最常用）
    print(key, value)
for value in student.values():      # 只拿值
    print(value)
```

**判断键是否存在**：`print("name" in student)` → True
（不存在的键直接取值会报 `KeyError`，用 `in` 先判断更安全）

## 3. 列表里放字典（超超超常用！）

一个列表装着很多个「人」，每个人是字典：

```python
students = [
    {"name": "小明", "age": 18},
    {"name": "小红", "age": 17},
    {"name": "小刚", "age": 19},
]

for s in students:                       # 先遍历列表
    print(f"{s['name']} 今年 {s['age']} 岁")   # 再取字典的键
```

> 注意：字典里取键用 `["name"]`，但 f-string 的 `{}` 里要用**单引号**（`s['name']`），
> 因为外层已经是双引号了。这是新手最常报的 `SyntaxError` 之一。

## 4. 为什么这一课这么重要

- **数据组织**：程序里绝大部分数据都是「一批对象，每个对象有多个属性」→ 就是「列表套字典」
- **JSON 格式**：大模型 API 返回的结构化数据、配置文件、网页数据，全是这种结构
- 学会了这一课，你就能读懂大模型返回的数据、能操作它——**这是 Agent 开发的第一步**

## 5. 练习（动手写！）

1. **购物清单**：建一个列表，练习 append / 修改 / remove / 遍历打印
2. **成绩统计**：`scores = {"语文": 88, "数学": 95, "英语": 79}`，用循环算出平均分并打印
3. **找最大**：建一个 3 个学生的列表（字典），用循环找出年龄最大的学生的名字
   （提示：用一个变量记住「目前最大」，边遍历边比较）

做完存进 `PROJECTS/`，比如 `04-lists-dicts/`。

## 6. 常见错误对照表

| 报错 | 原因 | 解决 |
|------|------|------|
| `IndexError: list index out of range` | 下标越界（比如只有 3 个元素却取 `[5]`） | 检查下标，别忘了从 0 开始 |
| `KeyError: 'xxx'` | 取了一个不存在的键 | 先用 `in` 判断，或确认拼写 |
| `SyntaxError`（f-string 里） | 外层双引号、里层又用双引号 | f-string 里用单引号：`f"{s['name']}"` |

---

**完成标志**：3 道练习独立跑通；特别是练习 3——「列表套字典 + 循环 + 条件」的组合是以后写 Agent 的基本功。
