# 开始制作MOD

---------
<a name="Tools"></a>

## 前期准备

<a name="EnterDevBranch"></a>
### 进入Steam的开发分支

steam客户端列表中，右键游戏-属性-测试-输入TetraProjectDevelopAlpha-选择developalpha

---------

<a name="UserModFolder"></a>
## MOD资源包说明
- **MOD资源包位置**：在`我的文档/TetraProject/Packages`在这个地方新建你的自制MOD资源包
- **目录结构**：这个地方可以新建多个MOD资源包，比如你的目录结构可以是：
```
我的文档/
	TetraProject/
		Packages/
			杰哥的MOD/
				Database/
					Database.xlsx
				CharacterModel/
					1.ase
				Music/
					1.ogg		
			阿伟的卡绘/
				CharacterModel/
					1.ase
				CardArt/
					1.png
```



<a name="TemplatePackage"></a>

## 模板资源包
如果你不知道如何新建MOD资源包，游戏提供了一个内置资源包名叫`Builtin`可以作为模版

你可以在`<游戏安装目录>\TetraProject_Data\StreamingAssets\Packages\Builtin`下面找到它（如果没有找到这个资源包，需要先[进入Steam的开发分支](#EnterDevBranch)）。

每个MOD资源包都使用了和「Builtin」相同的目录结构，你可以把内置资源包当成一个大型MOD来参考。

---------
> 使用快捷键需要先[进入Steam的开发分支](../QuickStart/#EnterDevBranch)

## 快速入门
1. **复制模版资源包**：将[模版资源包](#TemplatePackage)复制到[MOD资源包位置](#UserModFolder)（也就是readme.txt所在目录）
1. **资源包改名**：删掉复制过来的Builtin/PackageInfo.json，然后把资源包文件夹改一个你想要的名字，比如「阿伟MOD」。
1. **打开游戏数据库**：用`<游戏安装目录>/DbEditor/AgsDbEditor.exe`打开资源包里的Database/Database.xlsx，这里面集合了所有游戏数据。
1. **查看并学习**：打开Card表，你可以看到现有的所有卡牌，按ALT+4再切到游戏里，你会印出那张卡
1. **开始制作一张卡**：随便复制一张现有的卡牌，然后改个ID，改一下功能，就做出了一张新的卡。
1. **上传MOD到创意工坊**：进入游戏-暂停菜单-创意工坊-自制文件夹-选择你的MOD-输入MOD的简介-点上传

-----------------
## 下一节：[学习快捷键](../Hotkey)