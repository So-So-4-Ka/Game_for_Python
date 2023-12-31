﻿# Вы можете расположить сценарий своей игры в этом файле.
init:
# Определение персонажей игры. 
    $ jesus = Character("Разработчики", color="#FFE600")
    $ gg = Character("[viname]", color="#c8ffc8")  
    $ p_math = Character('Преподаватель по Математики', color="#33CCCC") 
    $ o_w = Character('Александра', color="#CD0074") 
    $ o_m1 = Character('Данил', color="#8BA100")
    $ o_m2 = Character('Вова', color="#A62800")
    $ o_m3 = Character('Максим', color="#FFB273")
    $ woman = Character('Девушка', color="#FF0000")
    $ day_e = 3  
    # харизма
    $ harisma = 0  
    # моральное состояние
    $ moral = 4  
    # начальные знания
    $ begin_study = 2  
    # наличие долгов
    $ dolg = 0  
    $ ch = 0 
    $ con = 0
    $ quashtions = 0

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:

label start:

    scene room with dissolve

    jesus   "Вот и закончилась учёба, но хорошо ли... Совсем скоро начнётся сессия. Где все студенты пройдут суровое испытание, после которого немногие выживут." 
    jesus   "Наш главный герой обычный студент. Учится на платной основе и ему дорога эта учёба." 
    jesus   "Но..." 
    
    jesus   "Сможет ли он закрыть сессию и перевестись на бюджет или его ждёт завал и отчисление?{w} Всё зависит от вашего выбора"
    
    jesus   "Каждый ваш выбор, будет влиять на дальнейшую игру и как вы сдадите сессию." 
    
    jesus   "Забыл сказать, что у вас есть ещё параметры, о которых не нужно забывать.\n Харизма = [harisma],  Моральное состояние = [moral], \n Начальные знания  = [begin_study],  Наличие долгов = [dolg], \n"
    jesus   "Самое главное: умей раставлять приоритеты и желаю удачи" 
    $ viname = renpy.input("Введите имя:")
    gg      "Ох, ну и денёк выдался. Ну чтож, через [day_e] дня сессия, даже страшно стало."  
    gg      "Конечно, я учусь на платной основе и будет обидно, если меня отчислят. Хочется закрыть все предметы вовремя и отправится домой к родителям."  
    gg      "Так, сегодня начну подготовку, чем раньше начну, тем больше материала осилю" 
    "*бп-бп*"
    gg      "Так, мне пришло голосовое сообщение от Владимира. Надо посмотреть"
    "Сообщение от Вовы: [viname], я знаю,  что ты только с пар пришёл, но послушай меня. Сегодня с Максимом мы решили пойти в кафешку, говорят там суп-дня - это \"Рассольник\". Вообщем залетай к нам, не только поедим"
    "Хм, звучит замачиво, надо сходить. Ещё давно не виделись, так скучаю по его песням на гитаре и дебильным шуткам. Это отличная возможность расслабится."
    "Однако...Если я пойду с Володей в кафешку, то пропущу этот день."
    
     
    menu: 
        "Остаться подготовится или пойти отдохнуть?" 
         
        "Подготовка": 
            jump study   
         
        "Отдых": 
            jump chill
 
label chill:
    scene cafe with dissolve
    pause(1)
    
    $ moral += 3 

    gg       "Хотя...{w} Я же не надолго, главное меру знать."   
    o_m2     "Привет. Какже долго не пересекались. Давай, присаживайся!"
    "Долго???{w} Прошло всего неделя, если не считать моменты, когда на па-ре виделись."
    "Вдруг подходит [o_m3], с разъярённым лицом и говорит."
    o_m3    "Ты на минут 5 опоздал, я уже успел чай заказать и выпить, поэто-му с тебя чай."
    "Это я виноват, что он чай заказал пока меня не было"
    "Прошло несколько часов. Я забыл о своих проблемах, о обязанностях, ведь сегодня могу себе позволить."
    "Но...{w} Неожиданно нахлынуло беспокойствие."
    "Нужно хотябы немного времени потратить на подготовку. Засиживыться не стоит, или..."

    menu: 
        "Остаться или уйти домой"  
        "Остаться": 
            "Давно не виделся с друзьями. Хочется с ними провести много времени. К чёрту свои тревоги!"
            jump day_2 
         
        "Уйти":
            scene night with dissolve
            "Так, что-то я засиделся, пора идти. Нужно подготовится хотябы немного." 
            jump go_to_home
  
label study:   
    $ begin_study += 2  
    $ moral -= 2
    scene room with dissolve
     
    if day_e == 2:  
        "Я же могу к Володе завалиться и вместе с ним приготовится, а там и Максим подкатит."
        "Как раз они предлагали мне данный выбор."
        jump study_friends 
    elif day_e == 1:  
        " Не стоит. Не нужно отвлекаться на какую-то ерунду. Нужно напрячься. Совсем скоро важный день, от которого будет зависеть моя судьба."
        jump last_day 
    elif day_e == 3:
        gg      "Пожалуй нет. Надо уметь расставлять приоритеты" 
        "[viname] откинул свои мысли и пошёл готовиться дальше." 
        "Нужно правильно потратить время. Распределить его мудро"
        jump day_2   

label go_to_home: 
    $ begin_study += 1 
    $ moral -= 1 
    scene night with dissolve
    "Но всё-же хорошо, что посидели хорошо. Даже раслабился немного."
     
    jump day_2

# День 2 
label day_2: 
    "[viname] лёг спать. В надежде, что следующий день будет продуктивнее."
    $ day_e = day_e - 1
    scene room with dissolve
    "Данная статистика:  \nХаризма = [harisma],  Моральное состояние = [moral], \n Начальные знания  = [begin_study],  Наличие долгов = [dolg], \n"
    gg  "Так, до сессии осталось [day_e] дня. Нужно подготовится к предметам, иначе будет плохо." 
    "[viname] пошёл на кухню и приготовил себе нежные и хрустящие тосты с вишнёвым джемом.{w} А как это пахло всё, вы не представляете." 
    "После плотного завтрака, [viname] начал составлять свой сегодняшний план." 
    gg  "Хотя зачем я это делаю, сессия совсем скоро. Можно и без планов обойтись, остаться дома и готовиться дальше." 
    "Неожиданно приходит смс от подруги - [o_w]: \n'Првет, мы так давно не виделись. Ты погружён в свою учёбу, времени нет, у меня тоже проблемы. Поэтому я предлагаю сделать следующее: сегодня выступает твой любимый стендапер, можем сходить на него.'" 
    gg  "Ого, я и совсем про неё забыл. Около 3 месяца не виделись и не разговаривали." 
    gg  "Однако я даже нифига не готов к сесси, и лучше потратить день на зубрёжку." 
     
    menu: 
        "Остаться подготовится или пойти погулять с подругой?" 
         
        "Подготовка": 
            jump study   
         
        "Пойти на выступление": 
            jump Stand_Up 

label Stand_Up:

    $ moral += 3 
    $ harisma += 2



    gg  "Не так часто удаётся выходит куда-то в свет. Кстати, сегодня приезжа-ет мой любимый стендапер."
    gg  "Могу и рыбку съесть, и в лодку сесть."
    gg  "Пожалуй стоит сходить со своей подругой."
    scene zal with dissolve
    "Прошло время, я уже приехал на автобусе. Вижу, что она уже замучалась ждать."
    o_w "Привет. Ты что-то долго шёл, ну чтоже, пойдём посмотрим"
    #тут видео должно запуститься, но эта хуйня не работает
    $ renpy.movie_cutscene('Jack_Bombing.webm') 
    ## функция сверху, вот она подзалупная хуйня
    scene standup with dissolve
    #тут видео должно запуститься, но  не работает
    #$ renpy.movie_custscene('game/video/stand_up.ogv')
    gg  "Хорошо сходили. Всегда обожал этого комика. Такой харизматичный и шутит отлично"
    jump day_3 

label study_friends:  
    $ begin_study += 1 
    $ moral += 1 
    scene room with dissolve
    gg "Так даже веселее"
    jump day_3  
      
# День 3  
label day_3: 
    "[viname] лёг спать. В надежде, что следующий день будет продуктивнее."
    $ day_e = day_e - 1; 
    "Данная статистика:  \nХаризма = [harisma],  Моральное состояние = [moral], \n Начальные знания  = [begin_study],  Наличие долгов = [dolg], \n"  
    scene room with dissolve
    menu:  
        "Остался [day_e] день, время решать, что делать будем." 

        "Отдых": 
            jump chill_to_play_games  

        "Подготовка":  
            jump study

label chill_to_play_games:   
    $ moral +=3  
     
    gg  "Хорошо поиграл, пора к завтрашнему дню подготовиться или нет?"
    jump last_day

label last_day: 
    "Последний день" 
    scene room with dissolve
    menu:  
        "Что после игры будешь делать?." 

        "Сделать шпору": 
            jump cheat 

        "Честно":  
            jump chestno 

label cheat:
    scene room 
    $ ch += 1  
    gg "Ну на всякий случай надо сделать"

    jump sessiya
     
label chestno: 
    scene room  
    $ begin_study += 1 
    $ moral -=1  
    gg "Зато честно подготовлюсь. Но возможно пожалею об этом."
     
    jump sessiya 

# Дальше идёт сессия 
 
label sessiya:
    gg "[viname] лёг спать. Завтра всё решиться и проясниться картина, как вы подготовились."
    gg "Данная статистика:  \nХаризма = [harisma],  Моральное состояние = [moral], \n Начальные знания  = [begin_study],  Наличие долгов = [dolg], \n"    
      
    if moral <=0: 
        $ con +=1 
        jump game_over
    elif ch == 1: 
        gg "Так, сегодня экзамен, надо проверить, всё ли я взял. Шпаргалку спрячу во внутренний корман пиджака. На случай, если я забуду ответы." 
    elif begin_study > 2:  
        gg "Отлично! Хорошо, что я подготовился, пора сдать эту сессию" 
    else: 
        gg "Блин, что делать. Вообще не готов к сессиии. Ну ладно, выкручусь как-нибудь." 
    jesus "Настал день экзамена."
    scene room with dissolve
    menu:
        "Что сдаём сегодня, помнишь?" 
         
        "Математика": 
            jump math
 
label math:
    scene black
    gg  "Время сдавать экзамен по математике."
    scene build with dissolve    
    "За час до начала экзамена, я приехал на экзамен в корпус. Солнце встало."
    scene build_inside with dissolve
    "Я закрыл глаза лишь на мгновенье. Открыв, я с неохотой посмотрел на часы"
    scene black with dissolve
    scene build_inside with fade
    gg  "Прошло уже 30 минут, где [p_math]?"
    " Вдруг я слышу шаги, как кто-то идёт. Это был [p_math]."
    show p_math patient with dissolve
    hide p_math patient with dissolve
    gg  "Здравствуйте, я пришёл сдавать математику."
    scene auditory with dissolve
    if  begin_study > 2:
        show p_math smile with dissolve
        p_math  "Я вижу, как вы подготовились. Ну чтож, прошу пройти в аудиторю, [viname]."
        "С полной увереностью, я зашёл в аудиторию. Чтож, я был уверен в себе."
    elif begin_study <= 2:
        show p_math serious with dissolve
        p_math  "Здравствуй. Вижу, что единственное на что вы надеетесь - это бог. Прошу пройти в аудиторю, [viname]."
        "На бога... Хех, ну надеюсь, что каким-то чудом сдам."
    elif harisma > 0:
        show p_math patient with dissolve
        "Вы начали разговаривать с преподавателем. Размышляете о жизни"
        "Но вдруг..."
        jump game_over
    
    gg "Ну чтож, начнём."

    if ch == 1:
        jump famous 

    jump quashtions

label famous:
    scene auditory
    gg "Поскольку у вас есть шпоргалка, то перед вами встаёт выбор. Хотите использовать её или нет, решать вам."
    menu:
        "Использовать шпоргалку?"

        "Да":
            jump shpora
        "Нет":
            jump quashtions

label quashtions:
    scene auditory

    if begin_study > 2:
        show p_math smile with dissolve
        p_math "Чтож, такой вопрос:"
        menu:
            "x^2 - 2x - 8 = 0. Найди корни"

            "2; 4":
                jump game_over
            "-2; -4":
                jump game_over
            "2; -4":  
                $ quashtions = 1        
                jump game_over
            "-2; 4":
                jump game_over

    elif begin_study <= 2:
        show p_math smile with dissolve
        gg "Ну давай что-нибудь интересное дам:"
        menu:
            "x^2 + 2x + 5 = 0. Найди корни"
                
            "1 +/- 2i":
                jump game_over
            "-2 +/- i":
                jump game_over
            "-1 +/- 2i":
                jump game_over
            "2 +/- i":
                $ quashtions = 1
                jump game_over

label shpora:
    scene auditory
    gg "В кормане есть шпаргалка, я могу её с легкостью применить."
    if begin_study > 2: 
        show p_math smile with dissolve
        p_math "Вижу, что ты знаешь хорошо. Работал на лекциях и практиках, поэтому дам такой пимер."
        menu:
            "x^2 - 2x - 8 = 0. Найди корни"

            "2; -4":  
                $ quashtions = 1        
                jump game_over

            "-2; 4":
                jump game_over

    elif begin_study <= 2:
        show p_math patient with dissolve
        p_math "Ну давай что-нибудь интересное дам:"
        menu:
            "x^2 + 2x + 5 = 0. Найди корни"
                
            "1 +/- 2i":
                jump game_over
            "2 +/- i":
                $ quashtions = 1
                jump game_over


label game_over: 
 
    jesus "Чтож, а вот и результат. Да-да - это конец игры. А теперь следующее"

    if  con == 1:  
        jesus "Игра закончилась по причине того, что моральное состояние упало сильно." 
        jesus "К сожалению наш герой не смог придти на на сессию, ибо у него подкосило моральное состояние и не смог придти на сессию." 
    elif quashtions != 0:
        jesus "Вы с успехом сдали сессию. А вот как сдали, с чьей помощью - это уже не имеет значение."
    elif harisma > 0:
        jesus "Своей болтливостью вы разговорили преподавателя до такой степени, что он поставил вам зачёт, а вы с радостным лицом пошли домой."    
    else:
        jesus "Вы сами виноваты, что не сдали сессию. А чтоже, жаль. Но надеюсь вы запомнили, что главное - это уметь расставлять приоритеты."

return