import random
x = 1
otvet = ['ты дебил','все верно ты завтра умрешь','три коня']
shar = ['|(**)|','(00)','(^-^)']
quest = ['я жду вопрос','что тебя интересует?','мне лень пиши']
while x==1:
    print(f"|({shar[random.randint(0,2)]})|")
    print('гадалка кек')
    print(quest[random.randint(0,2)])
    if (input('чоо: ')) == 'gg':
        print('game over')
        x = 0
    else:
        print(otvet[random.randint(0,2)])




