# Lesson 002：把本地仓库推送到 GitHub

> 目标：把 `D:\a_deepseek_workshop\Coding` 这个本地仓库，推送到你在 GitHub 创建的
> `https://github.com/ljkkkkkk/agent-learning`，让全世界（和面试官）都能看到。

---

## 0. 核心概念：本地仓库 vs 远程仓库

- **本地仓库**：你电脑里的 `.git`（已经建好了，有第一次提交 `6c1ce0d`）
- **远程仓库**：GitHub 网站上的那份拷贝（现在还是空的）
- **push（推送）** = 把本地的快照「上传」到远程

## 1. 第一步：创建 Personal Access Token（PAT）

GitHub 出于安全，**不允许直接用密码 push**，要用令牌（Token）。

1. 打开 https://github.com/settings/tokens
2. 点右上角「Generate new token」→「Generate new token (classic)」
3. Note（说明）填 `agent-learning`；Expiration（有效期）选 90 天
4. 勾选权限：**repo** 那一大类（点开选中即可）
5. 点最下方绿色按钮「Generate token」
6. **立刻复制**显示的 `ghp_...` 字符串——只显示这一次，关掉页面就再也看不到了
7. 把 Token 存到安全的地方（比如密码管理器）；**不要发到聊天或代码里**

> 这个 Token 相当于「远程仓库的钥匙」，谁拿到谁就能改你的仓库，务必保密。

## 2. 第二步：把本地仓库关联到远程

在 VSCode 终端里执行（第一次由老师带你做，之后你自己来）：

```bash
git remote add origin https://github.com/ljkkkkkk/agent-learning.git
```

拆开解释：
- `remote` = 远程仓库；`add` = 添加
- `origin` = 给这个远程仓库起的名字（习惯叫 origin，可理解为「源头」）
- 最后是仓库地址，注意**末尾要加 `.git`**

验证：`git remote -v`，应显示两行 origin 的地址。

## 3. 第三步：推送

```bash
git push -u origin master
```

拆开解释：
- `push` = 上传
- `-u` = 记住这条推送关系（以后直接 `git push` 就行）
- `origin` = 推到哪个远程仓库
- `master` = 推哪个分支（分支后面再学，现在先照做）

第一次推送会弹出窗口要登录信息：
- 用户名填你的 GitHub 用户名
- **密码位置填 Token**（不是你的登录密码！）

## 4. 验证

1. 刷新 https://github.com/ljkkkkkk/agent-learning
2. 应该能看到 README.md、LESSONS/、LOGS/ 等所有文件和文件夹
3. 之后每次改动都走这套流程：`git add -A` → `git commit -m "说明"` → `git push`

## 5. 小抄（今后每天用）

```bash
git add -A                # 把所有改动放入暂存区
git commit -m "做了什么"    # 拍照存档
git push                  # 上传到 GitHub
```

> 这三行将是你今后最常用的命令，熟到形成肌肉记忆。
> 还有配套的命令：`git status` 看当前状态、`git log` 看历史、`git pull` 从远程拉最新代码。

---

**完成标志**：GitHub 网页上能看到你仓库的所有文件。
