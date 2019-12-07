
<a name="effectCode"></a>
##effectCode
指令|作用
----|----
Buff:XXX|XXX特效将作为Buff特效，特效会播放直到Buff被移除。，如果没写，默认使用UseCard
EffectDelay1.5|这个特效将延迟1.5秒才生成
Anim:XXX|角色播放一个名叫XXX的动画，如果没写，默认使用Anim:UseCard
DelayableAnim:XXX|角色播放一个名叫XXX的动画，它可以被其它地方延迟
Projectile:XXX|角色发射一个名叫XXX的特效
FlickerRed:|角色模型闪红
Shake:|角色模型振动
Sound:XXX|播放XXX声音
其它所有CardCommand的指令|所有{#CardCommand}都可以使用，不过推荐只使用那些不影响游戏性的指令，不然出现BUG的话不好排除
