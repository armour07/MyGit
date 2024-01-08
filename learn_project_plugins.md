
文件介绍
plug_utils.py
插件工具类
plugin_mgr.py
插件管理类
EditorSite.py
编辑器运行时，入口文件

插件结构
plugin_conf.py 插件配置文件，初始化时根据配置分类以及开启
plugin.py 插件开启时调用该文件中继承 InnerPlugin 类的 initialize 函数
subclassing
  - menu_extender.py 菜单注册相关
  - editor_utility_widgets.py 编辑器工具父类相关

插件运行流程：
UE 插件 NePy 初始化时调用
EditorSite.py -> on_init

以下描述的插件都是 python 中的插件，内嵌在 NePy 中

是否开启插件通过以下两个判断
"asiocore_64" in sys.modules
genv.WITH_PLUGIN = import_util.find_spec("innerplugins")

初始化插件
EditorSite.py -> on_init -> plug_utils.py -> load_client_inner_plugin(PluginLoadPhase.EditorInit)

load_client_inner_plugin 包含
  - 插件分类 plugin_mgr.py -> search_all_plug_conf
  - 插件初始化 plugin_mgr.py -> load_plugins

菜单注册时机
将函数注册到EditorSite.g_engineloop_init_completes中， EditorSite.add_engineloop_init_complete_callback(self.func)
UnrealEngine 初始化完成时触发 EditorSite.py -> on_post_engine_init -> on_engineloop_init_complete -> 执行所有注册的函数

菜单注册方法
需要先建立菜单按钮对应的类，类写在 subclassing/menu_extender.py
类格式
```python
import ue
from base.both.utils.translate_util import TEXT # 中文需要引入 TEXT
@ue.uclass()
class XXXMenu(ue.ToolMenuEntryScript):
	def init(self):
		Data: ue.ToolMenuEntryScriptData = self.Data
        Data.Menu = "LevelEditor.LevelEditorToolBar.User"   # 菜单路径
        Data.Name = "SVNCommitHelper"   # 菜单名称
        Data.Section = "SVNCommitHelper"    # 菜单组，给子菜单填写路径用
        Data.ToolTip = TEXT("SVN提交助手")  # 提示
        Data.Label = "SVN"  # 按钮显示文本
        Icon = Data.Icon
        ... # 图标相关
        Data.Icon = Icon
        Addvanced = Data.Advanced
        Addvanced.EntryType = ue.EMultiBlockType.ToolBarComboButton | ue.EMultiBlockType.MenuEntry
        Data.Advanced = Advanced
        self.Data = Data
```

界面 umg 相关
创建 - 控件蓝图 - 制作界面
创建 - 编辑器工具 - 把控件蓝图拉进来
  - 文件 - 重设蓝图父项 - 


view
control
  - view
  - data

### pyrsistent
1. PRecord:PRecord是pyrsistent库中的一个类，用于创建可持久化的记录（record）数据结构。记录是一个带有命名字段的数据结构，类似于Python中的命名元组（named tuple）或字典（dictionary）。PRecord的主要特点是不可变性，一旦创建后，不能修改其字段的值。可以通过定义字段和默认值的方式来创建PRecord类，并通过实例化类来创建具体的记录对象。
2. pvector:pvector是pyrsistent库中的一个类，用于创建可持久化的矢量数据结构。矢量是一个不可变的有序序列，类似于Python中的列表（list）。pvector类提供了一系列操作方法，例如添加、删除、修改等，这些操作方法返回一个新的pvector对象，而不会改变原始的pvector。
装饰器相关
1. field:field是用于定义PRecord类中字段的装饰器。通过在字段上添加@field装饰器，可以为字段提供类型注解和默认值。field装饰器还提供了一些额外的功能，比如字段验证器，可以在字段赋值时对值进行验证。
2. pvector_field:pvector_field是用于定义PRecord类中矢量字段的装饰器。矢量字段是一个特殊类型的字段，它可以存储一个不可变的有序序列。通过在字段上添加@pvector_field装饰器，可以为矢量字段提供类型注解和默认值。



### 子系统
- ue.SubsystemBlueprintLibrary
  - GetEngineSubsystem(TSubclassOf<UEngineSubsystem> Class)
  - GetGameInstanceSubsystem(UObject* ContextObject, TSubclassOf<UGameInstanceSubsystem> Class)
  - GetLocalPlayerSubsystem(UObject* ContextObject, TSubclassOf<ULocalPlayerSubsystem> Class)
  - GetWorldSubsystem(UObject* ContextObject, TSubclassOf<UWorldSubsystem> Class)
  - GetAudioEngineSubsystem(UObject* ContextObject, TSubclassOf<UAudioEngineSubsystem> Class)
- ue.EditorSubsystemBlueprintLibrary
  - GetEditorSubsystem(TSubclassOf<UEditorSubsystem> Class)

引用
from base.client.runtime.ue_utils.ue_genclass_utils import CPF, uproperty, uclass

编辑器世界
editor_world = ue.GetEditorWorld()

加载 DataLayerAsset，DataLayerAsset继承自 UObject，用 LoadObject 指定类型读取
designer_layer_asset: ue.DataLayerAsset = ue.LoadObject(ue.DataLayerAsset, DESIGNER_LAYER_PATH)
UDataLayerSubsystem 继承 UWorldSubsystem
获取DataLayer子系统
data_layer_subsystem: ue.DataLayerSubsystem = ue.SubsystemBlueprintLibrary.GetWorldSubsystem(editor_world, ue.DataLayerSubsystem.Class())
获取资源实例
data_layer_instance: ue.DataLayerInstance = data_layer_subsystem.GetDataLayerInstanceFromAsset(designer_layer_asset)
获取DataLayerEditor子系统
data_layer_editor_subsystem: ue.DataLayerEditorSubsystem = ue.EditorSubsystemBlueprintLibrary.GetEditorSubsystem(ue.DataLayerEditorSubsystem.Class())
创建资源实例
data_layer_creation_params: ue.DataLayerCreationParameters = ue.DataLayerCreationParameters()
data_layer_creation_params.DataLayerAsset = designer_layer_asset
data_layer_instance: ue.DataLayerInstance = data_layer_editor_subsystem.CreateDataLayerInstance(data_layer_creation_params)
弹窗
ue.EditorDialogLibrary.ShowMessage(TEXT("布怪"), TEXT("该场景不支持使用数据层"), ue.EAppMsgType.Ok)
编辑弹窗
detail_view_option = ue.EditorDialogLibraryObjectDetailsViewOptions()
detail_view_option.MinHeight = 1
detail_view_option.MinWidth = 1
detail_view_option.bAllowSearch = False
detail_view_option.bShowObjectName = False

@uclass()
class SUGameplayLayerNameSetting(ue.Object):
	GameplayLayerName = uproperty(str, CPF.EditAnywhere, DisplayName=TEXT("玩法数据层名称："))

layer_settings: SUGameplayLayerNameSetting = ue.NewObject(SUGameplayLayerNameSetting.Class())

is_confirm: bool = ue.EditorDialogLibrary.ShowObjectDetailsView(TEXT("布怪-创建玩法关卡数据层"), layer_settings, detail_view_option)

if is_confirm:
  print(layer_settings.GameplayLayerName)

