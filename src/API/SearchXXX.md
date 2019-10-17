
<a name="SearchCharacters"></a>
##SearchCharacters
查找单位，会返回一个列表，里面包含了查找单位的结果
>如果没写list:XXX，那默认会使用list:ins
 
指令|描述
----|----
list:ins|取得场上所有的单位
list:db|取得数据库里的单位
list:pool,XXX|取得XXX单位池，单位池在Characterset里的tagCode定义
emy:|只留下敌人
vis:|只留下可见的
liv:|只留下活着的
cls:|只留下最近的
tmt:|只留下队友（不包括自己）
team:|只留下同队的单位
lowHpP:|将列表按HP从小到大百分比排列
lowStaP:|将列表按体力从小到大百分比排列
died:|只留下死掉的
self:|只留下自己
player:|只留下玩家可控制的
mainPlayer:|只留下主角（也就是角色选择界面出现的那些角色）
teamId:XXX|只留下队伍ID是XXX的单位，（系统内置的有：玩家Player，怪物Monster，中立Neutral）
enemyTeamId:XXX|只留下敌人队伍ID是XXX的单位
hasBuff:XXX|只留下拥有Buff是XXX的单位
hasMostBuff:XXX|只留下拥有Buff是XXX的单位，并按buff数量从大到小排序
hasLeastBuff:XXX|只留下拥有Buff是XXX的单位，并按buff数量从小到大排序
除了以上参数，也包括了这些参数[FilterList](/../API/SearchXXX/#FilterList)

<a name="SearchCards"></a>
##SearchCards
查找卡牌
> 例子：
> `SearchCards:{list:Hand;list:Deck;tag:Bullet}`的意思是`取得手牌和牌库里标签是Bullet的卡牌`
 
指令|描述
----|----
list:Db|取得全部数据库
list:Prop|取得道具
list:Hand|取得手牌
list:Deck|取得牌库
list:Discarded|取得弃牌堆
list:Buff|取得Buff
list:pool,XXX|取得XXX卡池，卡池在Cardset里的tagCode定义
energyReq:3|留下能量需要为3的卡牌
除了以上参数，也包括了这些参数[FilterList](/../API/SearchXXX/#FilterList)

<a name="FilterList"></a>
##FilterList
通用过滤器：被多个地方使用，比如[SearchCards](/../API/SearchXXX/#SearchCards)/[SearchCharacters](/../API/SearchXXX/#SearchCharacters)
 
指令|描述
----|----
distinct:XXX|过滤重复id的元素
distincttag:XXX|tag里包含XXX的单位只会在列表里出现一次
id:XXX|只留下id为XXX的项
anyid:XXX,YYY,ZZZ,...|只留下id为XXX或者YYY或者ZZZ的项
notid:XXX|只留下id不为XXX的项
tag:XXX|只留下标签包含XXX的项
anyTag:XXX,YYY,ZZZ,...|只留下标签包含XXX或者YYY或者ZZZ的项
notTag:XXX|只留下标签不包含XXX的项
random:|将列表随机化
take:3|只取得列表的前3项
skip:3|跳过列表的前3项
