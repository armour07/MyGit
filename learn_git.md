学习 git 记录
官方地址：https://learngitbranching.js.org/?locale=zh_CN

# 介绍

1. Git 网络传输从 SSH 到 HTTP
2. 防止数据丢失：分布式版本控制系统（DVCS），客户端每一次克隆操作，实际上都是一次对代码仓库的完整备份

### 特点
1. 直接记录快照，而非比较差异
2. 近乎所有操作都是本地执行，历史信息
3. 保证完整性，计算校验和 SHA-1 散列（hash，哈希），保存的信息以文件内容的哈希值来索引
4. 一般只添加数据

### 三种状态
- 已提交（committed） 表示数据已经安全地保存在本地数据库中
- 已修改（modified） 表示修改了文件，但还没保存到数据库中
- 已暂存（staged） 表示一个已修改文件的当前版本做了标记，使之包含在下次提交的快照中

### 三个阶段
- 工作区（working directory） 是对某个版本独立提取出来的内容，存放磁盘
- 暂存区（staging area） 是一个文件，保存了下次将要提交的文件列表信息，也叫索引
- Git 目录（.git directory(repository)） Git 保存项目的元数据和对象数据库的地方

### 工作流程
- 在工作区修改文件
- 将需要提交的文件选择性地添加到暂存区
- 提交更新，将快照永久性存储到 git 目录

### 命令行相关

#### 查找所有配置相关

`$ git config --list --show-origin`

#### 设置用户名和邮件地址

`$ git config --global user.name "xukai"`

`$ git config --global user.email wb.xukai03@mesg.corp.netease.com`

#### 获取帮助
```
$ git help <verb>
$ git <verb> --help
$ git man git-<verb>
$ git help config
$ git add -h
```

#### 两种获取 git 仓库的方式
1. 将尚未进行版本控制的本地目录转换为 git 仓库
   1. 命令行进入目录 `$ cd /d D:` `$ cd D://MyGit`
   2. 初始化仓库 `$ git init` 该命令会创建一个 **.git** 的子目录
   3. 添加指令 `$ git add *.c` `$ git add LICENSE`
   4. 提交指令 `$ git commit -m 'initial project version'`
2. 从其他服务器克隆一个已存在的 git 仓库
   1. 克隆 `$ git clone https://github.com/armour07/learn.git`
   2. 克隆并指定名字 `$ git clone https://github.com/armour07/learn.git mylearn`

如果是 SSH 需要公钥绑定到服务器

克隆支持协议：
1. `https://`
2. `git://`
3. `SSH:`

#### 指令介绍

##### add
`$ git add <file>`

- 跟踪文件，并处于暂存状态，如果是目录，会递归跟踪目录下的所有文件
- 跟踪只会跟踪当前命令之前的所有更改，之后再重新修改文件时，该文件会同时处于已跟踪和未跟踪两种状态，需要重新 add 一遍，或使用 commit -a 直接提交

##### rm
`$ git rm [-f] [--cached] <file>`

- 移除文件，磁盘文件删除后，需要使用命令让 git 之后从版本里也进行移除
- [-f] 强制移除，删除之前修改过或已经放到暂存区的文件
- [--cached] 移除不小心放到暂存区的文件
- \<file\> 必填，可以是文件名，也可以是目录，如有 * 需要写 \\*

##### restore
`$ git restore <file>` 还原文件修改

##### mv
`$ git mv file_name file_to` 可用于改名或者移动文件目录

##### commit
`$ git commit [-a] [--amend] [-m 'log']`

- 提交所有处于暂存区的文件
- [-a] 跳过使用暂存区的方式，把已跟踪的文件直接提交
- [--amend] 如果提交信息写错，或发现上次提交漏了几个文件，该句会把文件提交并覆盖之前的信息
- [-m]如果执行 commit 没有加 -m 添加注释的话，会进入 vm 编辑界面，需要按下 **i**、 **a**、 **o** 任意字符可进入编辑，第一行输入注释，之后按 **esc** 推出编辑模式，输入 **ZZ** 或 **:wq** 或 **:wq!** 都可以强行退出

##### status
`$ git status [-s|--short]`

- 查看当前仓库状态
- [-s|--short] 简短展示状态

##### log
`$ git log [-p|--patch] [-n] [--stat] [-S filter] [--pretty=oneline]`
- 查看提交历史
- [-p|--patch] 详细信息 
- [-n] 只查看n条信息，例如 -2
- [--stat] 查看被修改的文件，多少文件被修改，被修改的行为
- [-S filter] 过滤查找修改内容包含 filter 的提交记录
- [--pretty=oneline] 查看单行日志

##### branch
`$ git branch [-d] [-f branch hash] newImage`

- 创建分支
- [-d] 删除分支
- [-f branch hash] 移动 branch -> hash

`$ git branch -f foo origin/main` 创建新分支 foo 指向远程分支，之后 push，origin/main 更新，foo 也更新，默认的 main 就保留原始状态

`$ git branch -u origin/main foo` 同上，只不过 foo 需要提前创建，如果当前在 foo 上，最后参数可以不指定

##### checkout

`$ git checkout [-b] newImage`

- 切换分支 后续版本 checkout 改为 switch，也可以指定某一条提交记录
- [-b] 创建并切换分支
- newImage 可以是分支名，可以加移动指针，如 HEAD^、HEAD~3、hash

`$ git checkout 2.0.0` 检出标签，不推荐
`$ git checkout -b version2 2.0.0` 创建新分支并指定标签，推荐

##### merge
`$ git merge bugFix`

- 合并分支，当前处于哪个分支，就会把 bugFix 合并进当前分支

##### rebase

`$ git rebase main` 合并分支，把当前分支的一个个记录复制一份到 main 中，并将当前分支指向 main 的后续节点

`$ git rebase main bugFix` 相当于 checkout main 然后 merge bugFix

`$ git rebase -i HEAD~4` 可手动改变 4 个节点的位置，是否合并，然后重新开启一条新的分支

##### fetch
`$ git fetch <shortname> [newname]`

- 拉取远程仓库中最新的文件到本地，不会自动合并和修改当前的内容
- [newname] 指定新的名字，默认 origin

##### pull
`$ git pull [shortname]`

- 拉去远程仓库最新文件到本地，然后自动合并内容，相当于 fetch + merge

##### remote
`$ git remote [-v] [add [shortname] <url>] [show [remote]] [rename <cur_name> <new_name>] [rm|remove <shortname>]`

- 列出当前每一个远程的名字
- [-v] 列出名字 + url
- [add [shortname] <url>] 添加远程仓库，并指定简短名，默认 origin
- [show [remote]] 查看某个远程仓库
- [rename <cur_name> <new_name>] 修改远程仓库名字
- [rm|remove <shortname>] 移除远程仓库

##### push
`$ git push [shortname [master]]` 

- 默认将 main 提交到远程仓库，并同步 origin/main = main
- [shortname [master]] shortname 表示推送到哪个仓库，master 表示合并哪个分支

##### tag
`$ git tag [-l] [-list] ["v1.*"]` 查看标签，可筛选

`$ git tag -a v1.4 -m "my v1.4"` 设置标签，并加上一句日志

`$ git show v1.4` 展示v1.4的详细信息

`$ git tag -a v1.2 <hash 前缀>` 对指定版本设置标签

`$ git describe [main]` 打印距离最近的标签

`$ git push origin <tagname>` 默认 push 不会包含标签，需要指定标签上传

`$ git push origin --tags` 推送所有标签

`$ git tag -d <tagname>` 移除标签

`$ git push origin --delete <tagname>` 移除远程标签

##### diff
通过文件补丁的格式更加具体显示哪些行发生了改变

`$ git diff` 该命令比较的时是当前文件和暂存区快照之间的差异

`$ git diff --staged` `$ git diff --cached` 该命令查看已暂存的将要添加到下次提交里的内容

### 忽略提交文件
忽略文件检测，需要建立一个名为 .gitignore 文件位于根目录，列出忽略的文件
```
*.[ao]
*~
```
第一行表示忽略 *.a 或者 *.o
第二行表示忽略所有以 ~ 结尾的文件

- 空行或 # 开头行都会被忽略
- 目录开头加开头'/' 表示只检测根目录的文件夹，防止递归，/a 表示忽略 /a 但不忽略 /b/a
- 目录结尾加'/' 表示忽略所有同名目录，a/ 表示忽略 /a 并且忽略 /b/a
- 前面加'!' 表示取反 *.txt 并且 !a.txt 表示忽略所有.txt 但不忽略 a.txt
- (*) 匹配零个或多个任意字符
- ([abc]) 匹配任何一个在方括号里的字符
- (?) 匹配任意一个字符
- ([0-9]) 匹配 0-9的数字
- (a/**/z) 匹配任意中间目录，如 a/z, a/b/z, a/b/c/z

### 技巧

```
$ git rebase -i HEAD~2 先交换位置
$ git commit --amend   再修改最后一条日志
$ git rebase -i HEAD~2 在恢复位置
```

`$ git config --global alias.别名 'commit'` 建别名，后续便可以使用 git 别名 来代替提交
