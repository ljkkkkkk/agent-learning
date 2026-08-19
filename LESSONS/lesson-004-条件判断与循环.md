# Lesson 004：条件判断与循环（Python 基础 · 第二课）

> 本节课学程序的两大「控制流」：**条件判断**（让程序会做选择）和**循环**（让程序会重复干活）。
> 学完这两个，你就能写出真正的「有逻辑」的程序了。

---

## 1. 条件判断：if / elif / else

程序默认从上往下一条条执行。`if` 让程序**根据条件决定走哪条路**：

```python
age = 20

if age >= 18:
    print("成年了")
else:
    print("未成年")
```

**三个要点**：
1. `if` 后面跟一个**条件**（结果是 True 或 False），条件末尾要**加冒号 `:`**
2. 下一行必须**缩进**（按 Tab 或 4 个空格）——**Python 用缩进表示代码块**，这是 Python 的特色！
3. `else` 是「否则」分支；多分支用 `elif`（else if 的缩写）

```python
score = 85

if score >= 90:
    print("优秀")
elif score >= 60:
    print("及格")
else:
    print("不及格")
```

**比较运算符**（产生 True/False）：

| 运算符 | 意思 | 例子 |
|--------|------|------|
| `==` | 相等（注意是两个等号！） | `x == 5` |
| `!=` | 不相等 | `x != 5` |
| `>` `<` `>=` `<=` | 大于 / 小于 / 大于等于 / 小于等于 | `x >= 18` |

**逻辑运算**：`and`（并且）、`or`（或者）、`not`（取反）

```python
age = 20
is_student = True

if age >= 18 and is_student:
    print("成年学生")
```

## 2. for 循环：数数 / 遍历

`for` 用于**有确定次数**的重复：

```python
for i in range(5):          # i 依次取 0,1,2,3,4
    print(f"第{i}次")

for name in ["张三", "李四", "王五"]:   # 遍历列表
    print(name)

for ch in "hello":          # 遍历字符串的每个字符
    print(ch)
```

**range 详解**：`range(5)` → 0~4；`range(2, 5)` → 2~4；`range(0, 10, 2)` → 0,2,4,6,8（第三个是步长）

## 3. while 循环：条件满足就一直做

```python
count = 0
while count < 3:            # 条件为 True 就继续
    print(f"count = {count}")
    count = count + 1       # 千万别忘！否则死循环
```

- **死循环**：条件永远为 True，程序停不下来。在终端按 `Ctrl+C` 强制停止
- `break`：立刻跳出循环；`continue`：跳过本次，进入下一次

```python
for i in range(10):
    if i == 3:
        continue        # 跳过 3
    if i == 8:
        break           # 到 8 就全停
    print(i)            # 输出 0 1 2 4 5 6 7
```

**怎么选**：知道要循环多少次用 `for`；不知道次数、靠条件结束用 `while`（比如猜数字游戏）。

## 4. 练习（动手写！）

1. **猜数字**：程序随机想一个 1~10 的数字（`import random` + `random.randint(1, 10)`），用户猜，大了提示「大了」、小了提示「小了」，猜对恭喜退出（用 while + break）
2. **乘法口诀表**：用嵌套 for 打印 1~9 乘法表（提示：`print` 加 `end="\t"` 可以不换行）
3. **1 到 100 求和**：用 for 循环算 1+2+...+100，打印结果（应该是 5050）

做完存进 `PROJECTS/`（可以建 `02-guess/`、`03-multiplication/` 等文件夹）。

## 5. 常见错误对照表

| 报错/现象 | 原因 | 解决 |
|------|------|------|
| `IndentationError` | 缩进不对 | 检查代码块是否统一用 Tab 或空格 |
| `SyntaxError: expected ':'` | if/for/while 行末忘加冒号 | 补上 `:` |
| 程序卡住不结束 | 死循环 | `Ctrl+C` 停；检查 while 条件有没有变化 |
| `if x = 5` 报错 | 把 `==` 写成了 `=` | 比较用 `==`，赋值才用 `=` |

---

**完成标志**：3 道练习全部跑通，尤其是猜数字游戏——它用到了 if、while、break、input、random，是你第一个「完整的小程序」。
