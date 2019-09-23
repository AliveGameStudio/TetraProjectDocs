# 卡牌指令-CardCommand

大部分指令在CardCommand里通过它的描述都很容易理解，这里只解释一些细节

<a name="SearchCards"></a>
## SearchCards
卡牌过滤器，比如「SearchCards:{list:Hand;tag:Bullet}」的意思是「手牌里标签是Bullet的卡牌」

指令|功能
---|---
list:Db|全数据库
list:Prop|道具
list:Hand|手牌
list:Deck|牌库
list:Discarded|弃牌堆
list:Buff|Buff
list:pool,XXX|XXX卡池，在Cardset里定义

