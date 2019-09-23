# 游戏数值表-Database.xls



## Character表
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
dropFilterCode|string|掉落物过滤器代码|注意：用这个可能之前你可能需要先了解一下[SearchCards指令](#CardCommand/SearchCards)。它是SearchCards里参数，用于定义掉落物的列表。详细见SearchCards指令，在CardCommand表里
initialRunCardId[0~3]|string|初始执行卡牌ID|和selfCardCode差不多，就是开始的时候对自己使用一张卡。
cardId[0~7]|string|初始卡牌ID|最开始的时候牌库里的卡牌


<a name="Character/fieldCode"></a>
### Character/fieldCode
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
### Character/tagCode
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


----------


## Card表
表头|值类型|名字|作用
---|---|---|---
id|string|id|卡牌的id
displayName|string|名字|卡牌的名字
price|int|价格|在原石加工器里的价格
energyReq|int|能量需求|用卡需要多少能量，俗称卡牌费用
range|float|射程|卡牌可以作用到多远的地方
spreadRadius|float|扩散半径|卡牌的AOE范围
aimTypeCode|string|瞄准类型|设定卡牌可以瞄准哪些单位
perferredTargetTypeCode|string|首选目标类型|设定首先瞄准哪些单位，[见下文](#Card/perferredTargetTypeCode)。
tagCode|string|标签|设定卡牌类型，比如子弹类、拳类、装备类，[见下文](#Card/tagCode)。
description|string|描述|留白的话，系统就会根据代码进行自动描述
code|string|代码|参考CardCommand表
remapCode|string|重映射代码|如果手动在description里写描述，会有一个问题：数值写死，当改变数值的时候，需要同时改变description和code，这时remapCode就起了作用
backgroundId|string|卡背ID|对应CardBackground文件夹
effectCode|string|特效|对应Effect文件夹。你可以直接写ID，也可以写一些其它参数，[见下文](#Card/effectCode)。


<a name="Card/tagCode"></a>
### Card/tagCode

标签可以自定义，自定义之后你用它来过滤卡牌，比如：给一张卡的标签设定为子弹，另一张卡的作用是使用手上所有子弹类的卡

你可以设定多个标签，标签用;分号隔开
>比如：`PosiBuff;CombatOnly`

不过也有一些系统标签，下面这些是系统标签

标签|作用
---|---
Equipment|装备卡
Prop|道具卡
PosiBuff|正面Buff
Debuff|负面Buff
CombatOnly|这张卡只能在战斗中使用
Hidden|会在Buff中隐藏
Interactable|这张卡被添加为Buff之后，角色就是可交互的


<a name="Card/perferredTargetTypeCode"></a>
### Card/perferredTargetTypeCode

首选目标类型决定了卡牌首先瞄准哪些单位。

你可以设定多种类型，当系统没有找到第一种单位的时候，就会寻找第二种，依次类推，类型用分号隔开
>比如`died;lowHpP;self`会依次寻找`死亡的单位、血最少的单位、自己`

类型|作用
---|---
emy|敌人，设定了emy之后就不能瞄准自己人了
self|自己，设定了self之后就不能瞄准敌人了
died|死掉的单位
lowHpP|HP最少的单位
hasBuff:XXX|拥有ID为XXX的Buff的单位
tmt|队友
player|玩家
tag:XXX|拥有XXX标签的单位

<a name="Card/effectCode"></a>
### Card/effectCode

你可以直接在effectCode里写特效的id，它将对应Effect文件夹里的资源。

你也可以写一些别的东西，比如播放音效、定义一个

指令|作用
---|---
Buff:XXX|XXX特效将作为Buff特效，特效会播放直到Buff被移除。
EffectDelay:1.5|这个特效将延迟1.5秒才生成
Anim:XXX|角色播放一个名叫XXX的动画
DelayableAnim:XXX|角色播放一个名叫XXX的动画，它可以被其它地方延迟
FlickerRed:|角色模型闪红
Shake:|角色模型振动
其它所有CardCommand的指令|所有CardCommand的指令都可以使用，不过推荐只使用那些不影响游戏性的指令，不然出现BUG的话不好排除


----------


## CardCommand表
表头|值类型|名字|作用
---|---|---|---
id|string|id|指令的id
description|string|描述|指令的描述
quoteDescription|string|引用描述|当在description里加入了`{qte:XXX}`的时候，就会出现一张名叫XXX的小卡，描述显示这里面写的
effectCode|string|特效代码|[参考这里](#Card/effectCode)
remapCode|string|重映射代码|当这个指令被执行的时候，会执行remapCode来代替。[参考这里](#CardCommand/remapCode)



<a name="CardCommand/remapCode"></a>
### CardCommand/remapCode

当这个指令被执行的时候，会执行remapCode来代替。

**例子**

*CardCommand表*

id|description|remapCode
---|---|---
TakeFireDamage|受到火焰{0}伤害|TakeDamage:$0;AddBuff:17,1;

*Card表*

id|displayName|code
---|---|---
1001|火焰子弹|tgt.TakeFireDamage:2


<a name="CardCommand/SearchCards"></a>
### CardCommand/SearchCards指令
卡牌过滤器

例子：

> `SearchCards:{list:Hand;list:Deck;tag:Bullet}`的意思是`取得手牌和牌库里标签是Bullet的卡牌`


指令|功能
---|---
<autogen:Character.SearchCards>
list:Db|取得全部数据库
list:Prop|取得道具
list:Hand|取得手牌
list:Deck|取得牌库
list:Discarded|取得弃牌堆
list:Buff|取得Buff
list:pool,XXX|取得XXX卡池，卡池在Cardset里的tagCode定义
distinct:|过滤重复的项
id:XXX|只留下id为XXX的项
anyid:XXX,YYY,ZZZ,...|只留下id为XXX或者YYY或者ZZZ的项
notid:XXX|只留下id不为XXX的项
tag:XXX|只留下标签包含XXX的项
anyTag:XXX,YYY,ZZZ,...|只留下标签包含XXX或者YYY或者ZZZ的项
notTag:XXX|只留下标签不包含XXX的项
random:|将列表随机化
take:3|只取得列表的前3项
skip:3|跳过列表的前3项
</autogen>
