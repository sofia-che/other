# The following script was written by Sofia Chepovetskaya

import nltk

cfg0 = nltk.CFG.fromstring("""
  S -> NP VP
  NP -> N | N | N DetP
  DetP -> DetP ConjP | Det N
  ConjP -> Conj N
  VP -> VP VP | AdvP NP | Conj VP | V PP
  AdvP -> Adv NegP
  NegP -> Neg V A
  PP -> P NP
  N -> 'океан' | 'бассейна' | 'энергией' | 'ныряльщиков' | 'пловцов'
  Det -> 'своих'
  Conj -> 'и' | 'поэтому'
  V -> 'следите' | '∅'
  Adv -> 'никак'
  Neg -> 'не'
  A -> 'безопаснее' 
  P -> 'за'
""")
cfg1 = nltk.CFG.fromstring("""
   S -> NP VP
   NP -> N | Num N | Det NP | A N
   VP -> DetP VP | V V | NegP PP
   DetP -> Det VP
   NegP -> Neg V
   PP -> PP PP | P NP | Adv PP | P NP
   N -> 'персонаж' | 'раза' | 'течения'
   Num -> 'первого'
   A -> 'сильного' 
   V -> 'будет' | 'нырять' | 'умрёт'
   Det -> 'такого' | 'который'
   Neg -> 'не'
   P -> 'с' | 'от'
   Adv -> 'даже'
""")
cfg2 = nltk.CFG.fromstring("""
    S -> NP VP
    NP -> Det NP | A N
    VP -> V VP | V NP
    Det -> 'этот'
    A -> 'бойкий' | 'морское'
    N -> 'тип' | 'чудище'
    V -> 'пытался' | 'поймать'
""")
cfg3 = nltk.CFG.fromstring("""
    S -> NP VP
    NP -> N | Det N
    VP -> NegP PP
    NegP -> Neg V
    PP -> P NP
    N -> 'чудище' | 'логова'
    Det -> 'своего'
    Neg -> 'не'
    V -> 'выходило'
    P -> 'из'
""")
cfg4 = nltk.CFG.fromstring("""
    S -> NP VP
    NP -> N | A N
    VP -> VP VP | V V | Conj VP | V VP | VP PP | V N
    PP -> P NP
    N -> 'оно' | 'почкованием' | 'силой'
    A -> 'страшной'
    V -> 'пыталось' | 'уплыть' | 'продолжить' | 'размножаться'
    Conj -> 'чтобы'
    P -> 'со'
""")
cfg5 = nltk.CFG.fromstring("""
    S -> NP VP
    NP -> Det NP | A N | NP PP | A N
    PP -> PP NP | P N | P N
    VP -> VP VP | V VP | VP PP | V N | Conj VP | DetP VP | V A
    DetP -> Det N
    Det -> 'наш' | 'эти'
    A -> 'отважный' | 'водных' | 'безуспешными'
    N -> 'герой' | 'океан' | 'поисках' | 'братьев' | 'разуму' | 'попытки'
    P -> 'в' | 'по'
    V -> 'продолжил' | 'исследовать' | 'оказались'
    Conj -> 'однако'
""")
cfg6 = nltk.CFG.fromstring("""
    S -> NP VP
    NP -> N NP | A N | N PP
    PP -> PP PP | P N | P NumP
    NumP -> Num N
    VP -> VP VP | V N | ConjP VP | V NP 
    ConjP -> Conj V
    N -> 'власти' | 'царства' | 'дистанцию' | 'существами' | 'метров' | 'карантин'
    A -> 'океанического'
    P -> 'между' | 'в'
    Num -> 'пять'
    V -> 'объявили' | 'соблюдать' | 'приказали'
    Conj -> 'и'
""")
cfg7 = nltk.CFG.fromstring("""
    S -> NP VP
    NP -> A N | A N
    VP -> VP VP | NegP AdvP | Conj VP | NP VP | NegP VP | V AdvP
    NegP -> Neg V | Neg V
    AdvP -> Adv PP | Adv NumP
    PP -> P N
    NumP -> Num N
    A -> 'указанные' | 'страшный'
    N -> 'правила' | 'вирус' | 'дне' | 'минут'
    Conj -> 'где'
    V -> 'жить' | 'действуют' | 'может'
    Neg -> 'не' | 'не'
    Adv -> 'только' | 'дольше'
    P -> 'на'
    Num -> 'двух'
""")
cfg8 = nltk.CFG.fromstring("""
    S -> NP VP
    NP -> N | A N
    VP -> VP VP | V PP | V AdvP | V PP
    PP -> PP NP | P N | P N
    AdvP -> Adv VP
    N -> 'герой' | 'событий' | 'эпицентр' | 'дно'
    A -> 'морских'
    V -> 'попавший' | 'начал' | 'погружаться'
    P -> 'в' | 'на'
    Adv -> 'стремительно'
""")
cfg9 = nltk.CFG.fromstring("""
    S -> NP VP
    NP -> N | NP NP | A N | Conj NP | A N
    VP -> VP CP | V N | N VP | V NP 
    CP -> Conj AdvP
    AdvP -> Adv VP
    N -> 'он' | 'кот' | 'собака' | 'одиночество' | 'его'
    A -> 'любвеобильный' | 'преданная'
    Conj -> 'и' | 'хотя'
    V -> 'чувствовал' | 'ждали'
    Adv -> 'дома'
""")
cfg10 = nltk.CFG.fromstring("""
    S -> NP VP
    NP -> N | N NP | A N
    VP -> NegP VP | CP VP | V PP | Conj VP | V PP
    NegP -> Neg V
    CP -> Conj VP
    PP -> P NP | PP PP | P N | P N
    N -> 'он' | 'чувством' | 'тоски' | 'дно' | 'акваланга'
    A -> 'всепоглощающей'
    V -> 'справиться' | 'опустился' | 'знал'
    Conj -> 'поэтому' | 'как'
    Neg -> 'не'
    P -> 'с' | 'на' | 'без'
""")
cfg11 = nltk.CFG.fromstring("""
    S -> NP VP
    NP -> N | A N | A N
    VP -> VP VP | V AdvP | Det VP | VP ConjP | V PP 
    AdvP -> Adv NP | Adv V
    ConjP -> Conj AdvP
    PP -> PP NP | P N
    N -> 'герой' | 'чудовище' | 'взглядом' | 'него'
    A -> 'лохнесское' | 'добрым'
    V -> 'встретил' | 'смотрело' | 'улыбалось'
    Det -> 'которое'
    Adv -> 'там' | 'безмятежно'
    Conj -> 'и'
    P -> 'на'
""")
cfg12 = nltk.CFG.fromstring("""
    S -> NP VP
    NP -> A NP | N NP | A N | N N
    VP -> VP VP | V PP | AdvP VP | N VP | AdvP ConjP | V PP
    PP -> P NP | P NumP
    AdvP -> Conj Adv | V Adv
    ConjP -> Conj VP
    NumP -> Num N
    A -> 'одинокий' | 'морского'
    N -> 'исследователь' | 'дна' | 'объятиях' | 'чудовища' | 'они' | 'день'
    V -> 'утонул' | 'умерли' | 'зажили'
    P -> 'в' | 'в'
    Conj -> 'а' | 'и'
    Adv -> 'потом' | 'счастливо'
    Num -> 'один'
""")

text = 'Океан никак не ∅ безопаснее бассейна, поэтому следите за энергией своих ныряльщиков и пловцов.  Персонаж, ' \
       'который будет нырять, не умрёт с первого раза даже от такого сильного течения.  Этот бойкий тип пытался ' \
       'поймать морское чудище.  Чудище не выходило из своего логова.  Оно пыталось уплыть, чтобы продолжить ' \
       'размножаться почкованием со страшной силой.  Наш отважный герой продолжил исследовать океан в поисках водных ' \
       'братьев по разуму, однако эти попытки оказались безуспешными.  Власти океанического царства объявили карантин ' \
       'и приказали соблюдать дистанцию между существами в пять метров.  Указанные правила не действуют только на дне, ' \
       'где страшный вирус не может жить дольше двух минут.  Герой, попавший в эпицентр морских событий, ' \
       'начал стремительно погружаться на дно.  Он чувствовал одиночество, хотя дома его ждали любвеобильный кот и ' \
       'преданная собака.  Он не знал, как справиться с чувством всепоглощающей тоски, поэтому опустился на дно без ' \
       'акваланга.  Герой встретил там лохнесское чудовище, которое смотрело на него добрым взглядом и безмятежно ' \
       'улыбалось.  Одинокий исследователь морского дна утонул в объятиях чудовища, а потом они зажили счастливо и ' \
       'умерли в один день.'

gram_list = [cfg0, cfg1, cfg2, cfg3, cfg4, cfg5, cfg6, cfg7, cfg8, cfg9, cfg10, cfg11, cfg12]

