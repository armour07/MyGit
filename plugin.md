插件 MyPlugin

文件夹结构

- Plugins
    - Resources （资源相关）
    - Source
      - MyPlugin
        - Private
          - *.cpp
        - Public
          - *.h
        - MyPlugin.Build.cs
    - MyPlugin.uplugin


打印屏幕
GEngine->AddOnScreenDebugMessage(-1, 5.f, FColor::Red, FString("Hello World"))

打印日志
FString str = FString(TEXT("Yes"));
UE_LOG(LogTemp, Warning, TEXT("Hello World %s"), *str);
参数1：LogTemp -> 提供给宏的类别名称 -> CoreGlobals.h
参数2：Fatal，Error，Warning，Display，Log，Verbose，VeryVerbose


FName 新资源命名使用
FName name1 = FName(TEXT("ThisIsMyTestFName"));
FName name2 = FName(TEXT("ThisIsMyTestFName"));
float CompareFloat = name1.Compare(name2); // 对比
FRotator RotPelvis = Mesh->MeshGetInstance(this)->GetBoneRotation(FName(TEXT("pelvis")));

FText 本地化相关，面向用户文本都用该类
FText::GetEmpty() or FText() or FText   // 空文本
FText::Format(LOCTEXT("A", "B {0}"), 1);

FString 可以搜索、修改并且与其他字符串比较
FString str = FString(TEXT("This is my test FString"));
FString str = FString::Printf(TEXT("%02d:%02d"), 1, 2);

Printf 格式化文本

```
FName -> FString    str = name.ToString();
FName -> FText      txt = FText::FromName(name);
FString -> FName    name = FName(*str)
FString -> FText    txt = FText::FromString(str);
FText -> FString    str = txt.ToString();
FText -> FName      txt -> str -> name
FString -> int32    i = FCString::Atoi(*str);
FString -> float    f = FCString::Atof(*str);
Fstring -> char     *str
int32 -> FString    str = FString::FromInt(i);
float -> FString    str = FString::SanitizeFloat(f);

```
编码：ASCII(1B)、Unicode（2B）、UTF-8(动态)

使用 nullptr 而不是 NULL

```cpp
// TArray 数组
TArray<int32> IntArray;
IntArray.Init(10, 5);   // == [10, 10, 10, 10, 10]
TArray<FString> StrArray;
StrArray.Add(TEXT("Hello"));    // 复制或者移动进数组
StrArray.Emplae(TEXT("World")); // 使用参数的新实例
// StrArray == ["Hello", "World"]
FString Arr[] = {TEXT("of"), TEXT("Tomorrow")};
StrArray.Append(Arr, ARROY_COUNT(Arr));
// StrArray == ["Hello", "World", "of", "Tomorrow"]
StrArray.AddUnique(TEXT("!")); // 只能填充新元素
StrArray.AddUnique(TEXT("!")); // 重复无法添加
StrArray.SetNum(10);

FString JoinedStr;
for (auto& Str :StrArray)
{
    JoinedStr += Str;
    JoinedStr += TEXT(" ");
}
// JoinedStr == "Hello World of Tomorrow !"
for (int32 Index = 0; Index != StrArray.Num(); ++Index)
{
    JoinedStr += StrArray[Index];
    JoinedStr += TEXT(" ");
}
// 只读
for(auto It = StrArray.CreateConstIterator(); It; ++It)
{
    JoinedStr += *It;
    JoinedStr += TEXT(" ");
}
// 可读写
for(auto It = StrArray.CreateIterator(); It; ++It)
{
    JoinedStr += *It;
    JoinedStr += TEXT(" ");
}
StrArray.Sort();    // 排序
StrArray.Sort([](const FString& A, const FString& B)
{
    return A.Len() < B.Len();
});
// Sort、HeapSort、StableSort
```

```cpp
// TMaps
TMaps<int32, FString> FruitMap;
FruitMap.Add(5, TEXT("Banana"));
FruitMap.Add(2, TEXT("Grapefruit"));
for(auto& Elem :FruitMap)
{
    FPlatformMisc::LocalProint(*FString::Printf(TEXT("(%d, %s)"), Elem.Key, *Elem.Value));
}
for(auto It = FruitMap.CreateConstIterator(); It; ++It)
{
    FPlatformMisc::LocalProint(*FString::Printf(TEXT("(%d, %s)"), It.Key, *It.Value));
}
```

const
```cpp
void SomeMutatingOperation(FThing& OutResult, const TArray<Int32>& InArray)
{
    // InArray在此处不会被修改，但OutResult可能会被修改
}

void FThing::SomeNonMutatingOperation() const
{
    // 此代码不会修改调用它时所在的FThing
}

TArray<FString> StringArray;
for (const FString& : StringArray)
{
    // 此循环的主体不会修改StringArray
}

void AddSomeThings(const int32 Count);

    void AddSomeThings(const int32 Count)
    {
        const int32 CountPlusOne = Count + 1;
        // 在函数主体内，Count和CountPlusOne都不能更改
    }
```


基本模板类
TSharedRef<>

智能引用，拥有与 C++ 引用相似的特性，但实现方式仍为对原生指针的拓展
非空，构造时需传入有效对象
参与引用计数，拥有所有权
TSharedPtr<>

智能指针，拥有与 C++ 指针相似的特性，实现方式为对原生指针的拓展。
参与引用计数，拥有所有权

获取菜单
LevelEditor.MainMenu 表示最上方的菜单
UToolMenu* Menu = UToolMenus::Get()->ExtendMenu("LevelEditor.MainMenu.Window");
UToolMenu* ToolbarMenu = UToolMenus::Get()->ExtendMenu("LevelEditor.LevelEditorToolBar.PlayToolBar");

拓展自定义菜单栏按钮
```cpp
UToolMenu* Menu = UToolMenus::Get()->ExtendMenu("LevelEditor.MainMenu");
FToolMenuSection& Section = Menu->FindOrAddSection(NAME_None);
FToolMenuEntry& Entry = Section.AddSubMenu(
  "Plugin",                                             // Name
  LOCTEXT("PluginName", "Plugin"),                      // Display Name
  LOCTEXT("PluginDescription", "Plugin Description"),   // Descriptions
  FNewToolMenuChoice()                                  // Contents: default
);
Entry.InsertPosition = FToolMenuInsert("Help", EToolMenuInsertType::Before);
```
拓展自定义菜单栏下的菜单按钮
```cpp
UToolMenu* Menu = UToolMenus::Get()->ExtendMenu("LevelEditor.MainMenu.Plugin");
FToolMenuSection& Section = Menu->FindOrAddSection(NAME_None);
Section.AddMenuEntryWithCommandList(
  FMyCommands::Get().PluginAction,     // Command
  PluginCommands                       // CommandList
);
```


.Build.cs
PrivateDependencyModuleNames
"ToolMenus",    用到菜单相关需要加入这个！！