
<a name="Card表"></a>
##Card表
表头|值类型|名字|描述
----|----|----|----
id|string|id|卡牌的id
displayName|string|名字|卡牌的名字
energyReq|int|能量需求|用卡需要多少能量，俗称卡牌费用
range|float|射程|卡牌可以作用到多远的地方
spreadRadius|float|扩散半径|卡牌的AOE范围
price|int|价格|在原石加工器里的价格
remapCode|string|重映射代码|如果手动在description里写描述，会有一个问题：数值写死，当改变数值的时候，需要同时改变description和code，这时remapCode就起了作用
tagCode|string|标签|设定卡牌类型，比如子弹类、拳类、装备类，详细见[Card-tagCode](/../API/Database/#Card-tagCode)
aimTypeCode|string|瞄准类型|设定卡牌只能瞄准哪些单位
perferredTargetTypeCode|string|首选目标        ///|设定卡牌首先瞄准哪些单位，一般用于AI<br>1.用竖线 \| 隔开**多个条件**<br>`比如给AI做一张给队友加血的卡："lowHpP|tmt" 会得到 [最小HP的队友]`<br>2.用分号 ; 隔开**多个目标**，AI会按顺序查找，直到找到有效目标<br>`比如给AI做一张给队友加血的卡，如果没有队友就给自己加，"lowHpP|tmt;self" 会得到 [最小HP的队友, 自己]`<br>3.当没有目标时，AI将不行动<br>更多指令见[SearchCharacters](/../API/SearchXXX/#SearchCharacters)。
code|string|代码|参考CardCommand表
在使用卡片时执行的指令
effectCode|string|特效|对应Effect文件夹。你可以直接写ID，也可以写一些其它参数，见[effectCode](/../API/effectCode/#effectCode)
description|string|描述|留白的话，系统就会根据代码进行自动描述
backgroundId|string|卡背ID|对应CardBackground文件夹

<a name="Card-tagCode"></a>
###Card-tagCode: 标签
 **标签**
 
+ 标签可以自定义，自定义之后你用它来过滤卡牌
 > 比如：给一张卡的标签设定为子弹，另一张卡的作用是使用手上所有子弹类的卡
+ 你可以设定多个标签，标签用;分号隔开
 > 比如：`PosiBuff;CombatOnly`
+ 不过也有一些系统标签，下面这些是系统标签
 
标签|作用
---|---
PosiBuff|正面Buff
Debuff|负面Buff
Equipment|装备卡
CombatOnly|这张卡只能在战斗中使用
Prop|道具卡
Hidden|会在Buff中隐藏
Interactable|这张卡被添加为Buff之后，角色就是可交互的

<a name="Character表"></a>
##Character表
表头|值类型|名字|描述
----|----|----|----
description|string|描述|1.会在角色选择界面显示 2.会在被卡牌引用时显示
hp|float|hp|角色初始生命值
energy|float|能量|角色初始能量
stamina|float|体力|角色初始体力
maxHandCardCount|int|手牌数上限|超过上限后无法抽卡
startTurnDrawHandCardCount|int|开始回合抽卡数|每回合开始时，抽几张卡
initialHandCardCount|int|初始手牌数量|这个字段所以一般给怪物使用。因为怪物是先攻击再抽卡，如果初始手牌数写0，那第一次到怪物的回合的时候，因为没有手牌，怪物会什么都不做渡过这一回合。
dropFilterCode|int|掉落物过滤器代码|注意：用这个可能之前你可能需要先了解一下[SearchCards](/../API/SearchXXX/#SearchCards)。它是SearchCards里参数，用于定义掉落物的列表。
selfCardTagCode|string|自身代码标签|见selfCardCode
selfCardCode|string|自身代码|事实上，角色的脚本是用卡牌来实现的。也就是说，写了selfCardCode表头，就相当于是对这个角色使用了一张代码是selfCardCode的卡。如果selfCardTagCode写了Equipment，那这张卡就是装备卡，会永远装备在角色身上。你可以在这个装备里写各种事件，比如当死亡会爆炸、当受到伤害会掉落物品之类的。
initialRunCardId0,initialRunCardId1 ... initialRunCardId3|string|初始执行卡牌ID|和selfCardCode差不多，就是开始的时候对自己使用一张卡。
modelId|string|模型ID
moveSpeed|float|移动速度
cardId0,cardId1,cardId2 ... cardId7|string|初始卡牌ID|最开始的时候牌库里的卡牌
teammateCharacterId[0~3]|string|队友ID
fieldCode|string|字段代码|这个表有很多字段（表头），如果全部列出来可能会让这个表变得很长难以编辑，所以那些不常用的字段可以写在fieldCode里面，详细见[Character-fieldCode](/../API/Database/#Character-fieldCode)

<a name="Character-fieldCode"></a>
###Character-fieldCode: 字段代码
表头|值类型|描述
----|----|----
introPlotId|string|开场剧情ID，对应Plot文件夹
outroPlotId|string|结局剧情ID，对应Plot文件夹
forceMakeOtherCharacterPoolsAvailable|bool|强制开启所有角色的卡牌池、关卡池|比如选择测试员时，卡池中会出现所有角色的卡牌、所有角色的关卡。
illustrationId|string|插图ID，在角色选择界面显示，对应Illustration文件夹
unlockByGameEndedCharacterId|string|这个角色解锁需要先通关另一个角色
