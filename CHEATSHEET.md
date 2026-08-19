# 速查表（CHEATSHEET）

> 学过的命令和知识点都汇总在这里。**忘了就翻这里**，不用回翻讲义。
> 随学习进度持续更新。

---

## 一、终端命令（Windows）

| 命令 | 作用 |
|------|------|
| `cd 路径` | 进入文件夹 |
| `dir` | 列出当前文件夹内容 |
| `cls` | 清空屏幕 |
| `python` | 进入 Python 交互模式（看到 `>>>`） |
| `exit()` | 退出交互模式 |
| ↑ ↓ 方向键 | 翻看历史命令 |
| Tab | 自动补全路径/文件名 |

## 二、Git 命令（黄金三连：add → commit → push）

| 命令 | 作用 |
|------|------|
| `git init` | 初始化仓库（建时光机） |
| `git status` | 查看当前状态 |
| `git add -A` | 所有改动进暂存区 |
| `git commit -m "说明"` | 拍照存档 |
| `git log --oneline` | 查看提交历史 |
| `git remote -v` | 查看远程仓库 |
| `git remote add origin 地址` | 关联远程仓库 |
| `git push -u origin master` | 首次推送 |
| `git push` | 以后推送 |
| `git pull` | 拉取远程更新 |
| `git branch` | 查看所有分支（`*` = 当前所在分支） |
| `git switch 分支名` | 切换到某个分支 |
| `git switch -c 新分支名` | **创建并切换**到新分支（最常用） |
| `git branch -M 新名字` | 重命名当前分支（-M = 强制改名） |

## 三、Python（已学内容）

```python
print("你好")            # 打印
type(x)                 # 查看类型
# 基本类型：int 整数 / float 小数 / str 字符串 / bool 布尔(True/False)

name = "小明"            # 变量 = 贴标签的盒子
age = int(input("年龄："))  # 输入（返回字符串，记得转换）

print(f"我叫{name}，今年{age}岁")  # f-string 格式化（最重要！）

# 运算符：+ - * / //(整除) %(取余) **(幂)
# 字符串：+ 拼接、* 重复、len() 长度
```

## 四、学习心态

1. **报错不可怕**——先读报错信息，重点看最后一行和它提示的行号
2. 想 5 分钟再问，记得更牢
3. 作业做完放进 `PROJECTS/`，每个项目能自己讲一遍
4. 笔记写进 `NOTES/`，写给未来的自己看
