wb.xukai03@mesg.corp.netease.com

#### 版本要求
Python 3.11.1
UE 5.2.1

#### 游戏体验
逆水寒
PVE 闲趣：琉璃  副本：琼玉
PVP 公平论武 试剑天下 逐鹿仙原：琼玉

塞尔达：旷野之息
全地图点亮 70个神庙 四神兽 50呀哈哈收集

[日报]DH3D-徐铠
接收人： dhwang@corp.netease.com
抄送人： wangxiang@corp.netease.com

2023/12/06
2天git， 3天python

clone UE 5.2.*
git clone -b 5.2.1-release git@github.com:EpicGames/UnrealEngine.git

2023/12/13
从今天到下周一学习 UnrealEngine 为主。 

作业如下：
1，入门作业： 需要clone github的 UnrealEngine 5.2.1 或者 5.2.后续版本   的代码下来，并编译通过。也新建了一个自己的项目 MyGame
2，基础作业：需要在自己的MyGame项目中 新建一个 C++的插件，插件名为MyPlugin，放到 MyGame/Plugins/目录中。在 插件启动和退出时各打印一个log
3，高级作业：需要在自己的插件MyPlugin中，写一个 自己的命令行UMyTestCommandlet出来，继承 UCommandlet 即可。 能使用 -run=MyTest 执行这个命令行。 这个命令行只需要打印几个Display层级以上的Log就行。
4，扩展作业： 需要在自己的插件MyPlugin中，扩展编辑器的菜单或者工具栏，增加一个自己的表项“MyTest" 菜单/工具栏按钮。 点击时，能弹出一个自己用 Slate写的一个简单界面。

3 运行命令行（C:\UE52\UnrealEngine\Engine\Binaries\Win64\UnrealEditor.exe D:\UE52\Projects\MyGame\MyGame.uproject -skipcompile -run=MyTest -a=100）

2023/12/20
1，独立程序 可以解析 命令行参数
2，可以使用 LoadPackage 去加载一个资源包
3，可以解析 资源包对应的 UClass的名字

比如我们一个资源是 在你的 MyGame/Content/AA/aa.uasset ， 那么我们可以使用 /game/AA.aa.uasset 作为路径，调用 LoadPacakge函数去加载这个资源包。




#### 地址相关
[配置 VS code 相关](https://km.netease.com/wiki/702/page/95816)
[作业地址](http://git-internal.nie.netease.com/dh3d/program_pub/homework/xukai/homework)
作业 git 地址：ssh://git@git-internal.nie.netease.com:32200/dh3d/program_pub/homework/xukai/homework.git
[配置 git 相关](https://km.netease.com/wiki/702/page/132156)
[CodeMaker vs code 插件](https://codemaker.netease.com/)
popo:ChatGPT

#### vs code 相关：
##### 插件：
- Python
- Pylance
- autopep8
- Flake8
- isort

##### setting:
```json
{
    "[python]": {
        "editor.defaultFormatter": "ms-python.autopep8",
        "editor.codeActionsOnSave": {
            "source.organizeImports": true,
        },
    },
    "flake8.args": [
        "--config=flake8.ini",
    ],
    "autopep8.args": [
        "--global-config=autopep8.ini",
    ],
    "isort.args": [
        "--settings-file=.isort.cfg"
    ],
    "python.analysis.extraPaths": [
        ".",
        "./core/Lib/packages_ext",
        "./core/engine",
        "./core/engine/Lib",
        "./server/Lib",
    ],
    "python.languageServer": "Pylance",
}
```

#### 群相关
群号：1563891   程序群
群号：1518659  整个项目组开发群
群号：4649351  程序QA群



#### 部署项目
新建 dh3d
git clone ssh://git@git-internal.nie.netease.com:32200/dh3d/SrcAutoSetup.git
copy wbprogamer.ini -> config.ini
python Main.py init

进游戏
注册新账号-143-1162

打开界面
genv.client_mgr.ui_mgr.show_ui("mission.mission_tip")

获取配置
genv.client_mgr.scripts_config_mgr.get_config("LoginConfig")

Game
- subSystemMgr
- uiMgr
- eventMgr

UIMgr

EventMgr

SubsystemMgr
- GetSubsystem<T>

BaseSubsystem
BagSubSystem