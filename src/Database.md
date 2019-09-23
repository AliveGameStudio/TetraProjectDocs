# 游戏数值表-Database.xls



## Character表头
表头|值类型|名字|作用
---|---|---|---
id|string|id|id
displayName|string|名字|名字
modelId|string|模型ID|对应CharacterModel文件夹
description|string|角色描述|1.会在角色选择界面显示 2.会在被卡牌引用时显示
//comment|string|注释|你可以随便写些什么方便自己查看（双斜杠//开头的表头不会被游戏读取
minimapModelId|string|小地图的模型|这个模型会在小地图显示，对应MinimapModel/Character文件夹
tagCode|string|标签代码|用来标记这个角色的特性。用分号;隔开，[详细见下文](#Character/tagCode)
fieldCode|string|字段代码|这个表有很多字段（表头），如果全部列出来可能会让这个表变得很长难以编辑，所以那些不常用的字段可以写在fieldCode里面，[详细见下文](#Character/fieldCode)
energy|float|能量|角色的初始能量
stamina|float|体力|角色的初始体力
moveSpeed|float|移动速度|角色的初始体力
initialHandCardCount|int|初始手牌数量|这个字段所以一般给怪物使用。因为怪物是先攻击再抽卡，如果初始手牌数写0，那第一次到怪物的回合的时候，因为没有手牌，怪物会什么都不做渡过这一回合。
startTurnDrawHandCardCount|int|开始回合时抽卡数|每回合开始时，抽几张卡
//usedInCharactersetId|||不用管
hp|float||角色的初始HP
selfCardTagCode|string|自身代码标签|见selfCardCode
selfCardCode|string|自身代码|事实上，角色的脚本是用卡牌来实现的。也就是说，写了selfCardCode表头，就相当于是对这个角色使用了一张代码是selfCardCode的卡。如果selfCardTagCode写了Equipment，那这张卡就是装备卡，会永远装备在角色身上。你可以在这个装备里写各种事件，比如当死亡会爆炸、当受到伤害会掉落物品之类的。
interactionPlotId|string|交互脚本ID|如果selfCardTagCode写了Interactable，那就可以在这里写它的交互脚本ID，对应Plot文件夹里的文件内容。注意：Plot文件夹不使用文件名作为ID，ID在它的文件内容里定义
dropFilterCode|string|掉落物过滤器代码|注意：用这个可能之前你可能需要先了解一下[SearchCards指令](#SearchCards)。它是SearchCards里参数，用于定义掉落物的列表。详细见SearchCards指令，在CardCommand表里
initialRunCardId[0~3]|string|初始执行卡牌ID|和selfCardCode差不多，就是开始的时候对自己使用一张卡。
cardId[0~7]|string|初始卡牌ID|最开始的时候牌库里的卡牌


<a name="Character/fieldCode"></a>
## Character/fieldCode
Character有很多字段（表头），如果全部列出来可能会让这个表变得很长难以编辑，所以那些不常用的字段可以写在fieldCode里面，
不常用的字段有这些:

表头|值类型|作用
---|---|---
introPlotId|string|开场剧情ID，对应Plot文件夹
outroPlotId|string|结局剧情ID，对应Plot文件夹
illustrationId|string|插图ID，在角色选择界面显示，对应Illustration文件夹
teammateCharacterId[0~3]|string|队友ID
notAllowSharedPool|bool|值为true的话表示不允许使用在Cardset里标记为Shared的卡池
wip|bool|值为true的话表示这个角色正在制作中
unlockByGameEndedCharacterId|string|这个角色只有在指定角色通关了才能解锁
forceMakeOtherCharacterPoolsAvailable|bool|强制开启所有角色的卡池


<a name="Character/tagCode"></a>
## Character/tagCode
标签|作用
---|---
Main|主角，会出现在角色选择界面
EnvObject|环境物体
Obstacle|障碍物，阻挡通行，也阻挡射程
Targetable|可瞄准，即使是障碍物，也可以被瞄准
AllowBeTargetedEvenTeammate|即使是队友也可以被瞄准
NotCombatable|不能战斗
NotAllowCombatUI|不显示战斗UI，比如血条之类的
NotAllowBuffUI|不显示Buff的UI
NotAllowTakeImpulse|不会被击退
NotAllowAimBySingleOnly|不会被SingleOnly的卡瞄准
Trap|陷阱（可以踩上去
NotAllowBeHarmed|不会再受伤



