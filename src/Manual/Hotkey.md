# 快捷键

> 使用快捷键需要先[进入Steam的开发分支](../QuickStart/#EnterDevBranch)

## 在Database.xls里的快捷键
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
		



## 在游戏里的快捷键

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
`+t|开启关闭加速
K+中键点击单位|杀掉鼠标点击的单位
K+中键点击手牌|销毁鼠标点击的手牌
D+在手牌中键|打开卡牌的Database.xls
在卡牌图鉴中`+中键|生成点击的卡牌到手上
在卡牌图鉴中D+中键|打开对应卡牌的Database.xls


## 下一节：[API参考](../../API/Database/)
