# 开始制作MOD

---------
<a name="Tools"></a>

## 前期准备
### 必要工具
1. WPS
1. WPS的VBA组件

> **提示**：WPS可以去WPS的官网下载，VBA组件在网上不容易找到，可以加QQ群下载：652279837

> 或者使用Excel，这样就不需要再下载VBA

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
			阿蔡MOD/
				Database/
					Database.xls
				CharacterModel/
					1.ase
				Music/
					1.mp3		
			阿伟的卡绘/
				CharacterModel/
					1.ase
				CardArt/
					1.png
```



<a name="TemplatePackage"></a>

## 模板资源包
如果你不知道如何新建MOD资源包，游戏提供了一个内置资源包名叫`Builtin`可以作为模版

你可以在游戏安装目录的`TetraProject_Data\StreamingAssets\Packages\Builtin`下面找到它（如果没有找到这个资源包，需要先[进入Steam的开发分支](#EnterDevBranch)）。

每个MOD资源包都使用了和「Builtin」相同的目录结构，你可以把内置资源包当成一个大型MOD来参考。

---------
> 使用快捷键需要先[进入Steam的开发分支](../QuickStart/#EnterDevBranch)

## 快速入门
1. **下载并安装**[必要工具](#Tools)
1. **复制模版资源包**：将[模版资源包](#TemplatePackage)复制到[MOD资源包位置](#UserModFolder)（也就是readme.txt所在目录）
1. **资源包改名**：删掉复制过来的Builtin/PackageInfo.json，然后把资源包文件夹改一个你想要的名字，比如「阿伟MOD」。
1. **打开游戏数据库**：用WPS打开资源包里的Database/Database.xls，这里面集合了所有游戏数据。
1. **查看并学习**：打开Card表，你可以看到现有的所有卡牌，按ALT+4再切到游戏里，你会印出那张卡
> 如果你使用Alt+4切到游戏里没有印出这张卡，检查一下是否安装WPS的VBA组件，或者检查WPS是否开启了宏
1. **开始制作一张卡**：随便复制一张现有的卡牌，然后改个ID，改一下功能，就做出了一张新的卡。
1. **删掉多余的数据**：当你做完你的MOD，记得删掉Builtin的内容和表格，只保留你做过的内容
1. **上传MOD到创意工坊**：进入游戏-暂停菜单-创意工坊-自制文件夹-选择你的MOD-输入MOD的简介-点上传

-----------------
## 下一节：[学习快捷键](../Hotkey)