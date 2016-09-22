#coding:utf-8
import pyttsx
engine = pyttsx.init()
# engine.say('Greetings!')
# engine.say('How are you today?')
h = "你好"
print h
h = h.decode("utf-8")
# engine.say(unicode(h))
# engine.say(u""+h)
# engine.say(u'你好')
# engine.say(u'种子') ;
# engine.say(u'种子') ;
# engine.say(u'种子') ;
# engine.say(u'种子') ;
# engine.say(u'种花生') ;
engine.say(u'重来') ;
engine.say(u'重量') ;

text = '''
1、儿子：“爸爸，天上为什么有那么多星星呢。”爸爸：“因为以前呀，天上只有三颗星，后来有一天，这三星炸了，就满天都是小星星了。”'


'2、姐夫向老爸诉苦道：“您女儿侦察能力实在是太强了，用尽各种方法藏私房钱，都被她找到啦！”'+
'只见老爸默默的点了根烟说：“放弃吧！这点是随她妈！”'+
'听了俩人的对话，我终于忍不住大声吼道：“你俩下次没钱，别再请我出来吃饭了，这样坑我单身真的好吗？！”'+

'3、女儿辛勤创作了一幅画，我不小心当废纸扔了。五岁的小家伙哭成了泪人，各种劝都无济于事。'+
'于是我掏出50块钱，在女儿眼前来回晃悠。'+
'她一脸鄙视：“我又不是你老婆，不要以为女人都会见钱眼开！”'+
'我被孩子的凛然正气深深地震撼了，最后用两张50平息了这场风波。'+

'4、老妈第一次收到老爸买的花，感动的一塌糊涂，告诉我说明天得给你爸零花钱减半，居然知道买花讨女人欢心了。'+

'5、老婆爱打麻将，有次输钱了在家大吼：再也不打了，再打就剁手。'+
'旁边看电视的儿子头也不回的就说：就你那麻将瘾，千手观音都能让你剁成维纳斯'
'''
text = text.decode("utf-8")
engine.say(unicode(text))
# engine.say(unicode(text,'unicode-escape'))

# engine.say(u'5、老婆爱打麻将，有次输钱了在家大吼：再也不打了，再打就剁手。旁边看电视的儿子头也不回的就说：就你那麻将瘾，千手观音都能让你剁成维纳斯')

engine.runAndWait()