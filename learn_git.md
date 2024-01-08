学习：https://learngitbranching.js.org/?locale=zh_CN

Git 网络传输从 SSH 到 HTTP
防止数据丢失：分布式版本控制系统（DVCS），客户端每一次克隆操作，实际上都是一次对代码仓库的完整备份

特点：
直接记录快照，而非比较差异
近乎所有操作都是本地执行，历史信息
保证完整性，计算校验和 SHA-1 散列（hash，哈希），保存的信息以文件内容的哈希值来索引
一般只添加数据

三种状态
- 已提交（committed） 表示数据已经安全地保存在本地数据库中
- 已修改（modified） 表示修改了文件，但还没保存到数据库中
- 已暂存（staged） 表示一个已修改文件的当前版本做了标记，使之包含在下次提交的快照中

三个阶段
- 工作区（working directory） 是对某个版本独立提取出来的内容，存放磁盘
- 暂存区（staging area） 是一个文件，保存了下次将要提交的文件列表信息，也叫索引
- Git 目录（.git directory(repository)） Git 保存项目的元数据和对象数据库的地方

工作流程
- 在工作区修改文件
- 将需要提交的文件选择性地添加到暂存区
- 提交更新，将快照永久性存储到 git 目录

命令行相关

查找所有配置相关

`$ git config --list --show-origin`

设置用户名和邮件地址

`$ git config --global user.name "xukai"`

`$ git config --global user.email wb.xukai03@mesg.corp.netease.com`

获取帮助
```
$ git help <verb>
$ git <verb> --help
$ git man git-<verb>
$ git help config
$ git add -h
```

两种获取 git 仓库的方式
1. 将尚未进行版本控制的本地目录转换为 git 仓库
2. 从其他服务器 克隆 一个已存在的 git 仓库

步骤：
1. 命令行进入目录 `$ cd /d D:` `$ cd D://MyGit`
2. 初始化仓库 `$ git init` 该命令会创建一个 .git 的子目录
3. 添加文件 `$ git add *.c` `$ git add LICENSE`
4. 提交文件 `$ git commit -m 'initial project version'`

`$ git commit` 如果没有加 -m 添加注释的话，会进入 vm 编辑界面
按下 i a o 任意字符可进入编辑，第一行输入注释，之后按 esc 推出编辑模式，输入 ZZ 或 :wq 或 :wq! 都可以强行退出
`$ git commit -a` 可以跳过使用暂存区的方式，把已跟踪的文件直接提交
例如 a.txt 文件修改后 add 到暂存区，再重新修改 a.txt，如果普通提交则不包含第二次更改，加上 -a 后会把后续修改一并提交
`$ git commit --amend` 如果提交信息写错，或者发现有未提交的文件，执行该句会把文件提交并覆盖之前的信息

克隆一个仓库
`$ git clone https://github.com/libgit2/libgit2`
指定新的文件名
`$ git clone https://github.com/libgit2/libgit2 mylibgit`

如果是 SSH 需要公钥绑定到服务器

支持协议：
`https://`
`git://`
`SSH: user@server:path/to/repo.git`

`$ git add <file>` 跟踪文件，并处于暂存状态，如果是目录，会递归跟踪目录下的所有文件
跟踪只会跟踪当前命令之前的所有更改，之后再重新修改文件时，该文件会同时处于已跟踪和未跟踪两种状态，需要重新 add 一遍

`$ git rm <file>` 移除文件，磁盘文件删除后，需要使用命令让 git 之后从版本里也进行移除
`$ git rm -f <file>` 强制移除，删除之前修改过或已经放到暂存区的文件（不是特别理解）
`$ git rm --cached README` 移除不小心放到暂存区的文件
`$ git rm log/\*.log` 可以是目录，* 需要反斜杠

`$ git restore <file>` 还原文件修改
`$ git mv file_name file_to` 可用于改名或者移动文件目录

`$ git log` 查看提交历史 参数：-p --patch 详细信息 -2 只查看两条信息 --stat 查看被修改的文件，多少文件被修改，被修改的行为 -S xxx 表示过滤查找修改内容包含xxx的提交记录

`$ git status` 查看当前文件状态
`$ git status -s` 简短展示状态
`$git status --short` 简短展示状态


通过文件补丁的格式更加具体显示哪些行发生了改变
`$ git diff` 该命令比较的时是当前文件和暂存区快照之间的差异
`$ git diff --staged` `$ git diff --cached` 该命令查看已暂存的将要添加到下次提交里的内容

`$ git reset HEAD <file>` 取消 file 暂存

-- 
`$ git branch newImage` 创建分支
`$ git branch newImage main^^2^` 创建分支后 checkout 到 main 的相对位置
`$ git checkout newImage` 切换分支 后续版本 checkout 改为 switch，也可以指定某一条提交记录
`$ git checkout -b newImage` 创建并切换分支
`$ git checkout HEAD^` 强制移动到 HEAD 的上一级，^ 向上移动一个提交记录，~3 向上移动多个提交记录，checkout 只能移动 HEAD
`$ git checkout c1` 移动 HEAD 到 c1
`$ git checkout HEAD^2` 如果当前节点有两个父节点（主，分支），HEAD^ 指向主，HEAD^2 指向分支
如果当前节点父节点只有一个，HEAD^2 指向父节点的父节点
`$ git switch -b newImage` 创建分支(-b)并切换到分支(switch)
`$ git merge bugFix` 合并分支，当前处于哪个分支，就会把 bugFix 合并进当前分支
`$ git rebase main` 合并分支，把当前分支的一个个记录复制一份到 main 中，并将当前分支指向 main 的后续节点
`$ git rebase main bugFix` 相当于 checkout main 然后 merge bugFix
`$ git rebase -i HEAD~4` 可手动改变 4 个节点的位置，是否合并，然后重新开启一条新的分支
`$ git branch -f main HEAD~3` 强制移动 main 到 HEAD 的上3级
`$ git branch -f main c3` 指定对应的 hash 值，如 c3 ，强制移动 main 到 c3，正式环境是40位 hash
`$ git branch -d hotfix` 删除分支
`$ git reset HEAD~1` 回退一个版本，对远程无效，HEAD 可以换成分支名或者 hash 名
`$ git revert HEAD` 回退一个版本，对远程有效，实际是生成一个新的版本，新版本等于上一个版本
`$ git cherry-pick c1 c2 c3` 指针在 main，执行该指令后 c1,c2,c3 会复制到 main 后

远程
`$ git clone <url>` 默认会命名为"origin"
`$ git remote` 列出当前每一个远程的名字
`$ git remote -v` 列出名字 + url
`$ git remote add <shortname> <url>` 添加远程仓库，并指定简短名，默认 origin
`$ git fetch <shortname>` 拉取远程仓库中最新的文件到本地，不会自动合并和修改当前的内容
`$ git fetch origin foo`
`$ git fetch origin foo~1:bar`
`$ git fetch origin :bar` fetch 空到本地，本地不存在 bar 时，会创建一个 bar 分支
`$ git pull <shortname>` 相当于 fetch 后 merge
`$ git pull --rebase` 相当于 fetch 后 rebase
fetch 后合并，可以用 rebase 或者 merge ，区别就是 rebase 指向远程仓库为父节点，merge 指向当前节点为父节点，影响 ^ ^2 的判断
`$ git push` 默认将 main 提交到远程仓库，并同步 origin/main = main
`$ git push <shortname> <master>` 推送到远程仓库，master 表示指定分支
`$ git push origin :foo` 空会删除远程仓库的 foo 分支
`$ git remote show <remote>` 查看某个远程仓库
`$ git remote rename <cur_name> <new_name>` 修改远程仓库名字
`$ git remote remove <name>` `git remote rm <name>` 移除远程仓库
`$ git branch -f foo origin/main` 创建新分支 foo 指向远程分支，之后 push，origin/main 更新，foo 也更新，默认的 main 就保留原始状态
`$ git branch -u origin/main foo` 同上，只不过 foo 需要提前创建，如果当前在 foo 上，最后参数可以不指定

`$ git tag [-l] [-list] ["v1.*"]` 查看标签，可筛选
`$ git tag -a v1.4 -m "my v1.4"` 设置标签，并加上一句日志
`$ git show v1.4` 展示v1.4的详细信息
`$ git log --pretty=oneline` 先查看单行日志
`$ git tag -a v1.2 <hash 前缀>` 对指定版本设置标签
`$ git describe [main]` 打印距离最近的标签
`$ git push origin <tagname>` 默认 push 不会包含标签，需要指定标签上传
`$ git push origin --tags` 推送所有标签
`$ git tag -d <tagname>` 移除标签
`$ git push origin --delete <tagname>` 移除远程标签
`$ git checkout 2.0.0` 检出标签， 不推荐
`$ git checkout -b version2 2.0.0` 创建新分支并指定标签，推荐

`$ git config --global alias.别名 'commit'` 建别名，后续便可以使用 git 别名 来代替提交

贮藏 sashing



技巧
```
$ git rebase -i HEAD~2 先交换位置
$ git commit --amend   再修改最后一条日志
$ git rebase -i HEAD~2 在恢复位置
```

忽略文件检测，需要建立一个名为 .gitignore 文件，列出忽略的文件
```
*.[ao]
*~
```
第一行表示忽略 *.a 或者 *.o
第二行表示忽略所有以 ~ 结尾的文件

空行或 # 开头行都会被忽略
目录开头加开头'/' 防止递归 /a 表示忽略 /a 但不忽略 /b/a
目录结尾加'/' 忽略所有同名目录 a/ 表示忽略 /a 并且忽略 /b/a
前面加'!' 表示取反 *.txt 并且 !a.txt 表示忽略所有.txt 但不忽略 a.txt
(*) 匹配零个或多个任意字符
([abc]) 匹配任何一个在方括号里的字符
(?) 匹配任意一个字符
([0-9]) 匹配 0-9的数字
(a/**/z) 匹配任意中间目录，如 a/z, a/b/z, a/b/c/z















