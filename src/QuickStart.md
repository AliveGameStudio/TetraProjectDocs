# 开始制作MOD

---------
<a name="Tools"></a>

## 必要工具
1. WPS
1. WPS的VBA组件

> **提示**：WPS可以去WPS的官网下载，VBA组件在网上不容易找到，可以加QQ群下载：652279837

> 或者使用Excel，这样就不需要再下载VBA

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
<a name="EnterDevBranch"></a>

## 快速入门
1. **下载并安装**[必要工具](#Tools)
1. **进入Steam的开发分支**:steam客户端列表中，右键游戏-属性-测试-输入TetraProjectDevelopAlpha-选择developalpha
1. **复制模版资源包**：将[模版资源包](#TemplatePackage)复制到[MOD资源包位置](#UserModFolder)（也就是readme.txt所在目录）
1. **资源包改名**：删掉复制过来的Builtin/PackageInfo.json，然后把资源包文件夹改一个你想要的名字，比如「阿伟MOD」。
1. **打开游戏数据库**：用WPS打开资源包里的Database/Database.xls，这里面集合了所有游戏数据。
1. **查看并学习**：打开Card表，你可以看到现有的所有卡牌，按ALT+4再切到游戏里，你会印出那张卡
> 如果你使用Alt+4切到游戏里没有印出这张卡，检查一下是否安装WPS的VBA组件，或者检查WPS是否开启了宏
1. **开始制作一张卡**：随便复制一张现有的卡牌，然后改个ID，改一下功能，就做出了一张新的卡。
1. **删掉多余的数据**：当你做完你的MOD，记得删掉Builtin的内容和表格，只保留你做过的内容（Database.xls里的ExcelConfig表格最好别删）
1. **上传MOD到创意工坊**：进入游戏-暂停菜单-创意工坊-自制文件夹-选择你的MOD-输入MOD的简介-点上传

---------

## 快捷键

> 需要先[进入Steam的开发分支](#EnterDevBranch)

### 在Database.xls里的快捷键
> 在某个表按下下列快捷键再切到游戏里

快捷键|功能
---|---
在Card表按Alt+4|印卡
在Character表里按Alt+4|刷怪
在Stage表里按Alt+4|跳关
在Tester表里按Alt+4|设置当前测试用的流派
在Stage表里按Alt+1|打开对应Stage的地图文件。比如StageMap/1.tmx
Alt+2|在某个头表是`xxxxPlotId`的单元格按Alt+2，可以快速打开这个剧情脚本。（比如Character表的interactionPlotId）
Alt+5|在引用的单元格按Alt+5可以快速跳转到引用的项（引用的单元格指的是那些会自动从数字ID变成中文的单元格，比如Cardset的cardId0）
		



### 在游戏里的快捷键
> 需要先[进入Steam的开发分支](#EnterDevBranch)

快捷键|功能
---|---
F5|刷新修改的资源（修改表格不用，一般用于修改模型、关卡、特效之类的）
F4|重复上次的Database指令操作（比如印卡）
`+e|满能量、体力、钱
`+X|下一关
ctrl+alt+shift+r|删档重来（和标题界面的「新游戏」类似，不会删除系统存档，比如音量设定、通关次数、游戏时间……）
`+ctrl+alt+shift+r|完全删档重来
`+L|解锁卡牌图鉴全部卡牌
`+s|即时存档
`+t|开启关闭加速。加速开启后，按t加速
K+中键点击单位|杀掉鼠标点击的单位
K+中键点击手牌|销毁鼠标点击的手牌
D+在手牌中键|打开卡牌的Database.xls
在卡牌图鉴中`+中键|生成点击的卡牌到手上
在卡牌图鉴中D+中键|打开对应卡牌的Database.xls

