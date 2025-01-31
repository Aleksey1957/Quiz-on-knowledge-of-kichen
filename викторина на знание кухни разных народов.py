print(
    'Это викторина на знание кухни разных народов. Ответь на вопросы и узнай, насколько хорошо ты разбираешься в еде!')

score = 0

true_answer1 = 'татары'
true_answer2 = 'франция'
true_answer3 = 'мексика'
true_answer4 = 'гёдза'
true_answer5 = 'беларусь'

question1 = input('Кто придумал эчпочмак?')
question2 = input('Луковый суп — это блюдо какой кухни?')
question3 = input('Где родина начос?')
question4 = input('Как называются китайские пельмени?')
question5 = input('В национальную кухню какой страны входят драники?')

if question1.lower() == true_answer1:
    score = score + 1

if question2.lower() == true_answer2:
    score = score + 1

if question3.lower() == true_answer3:
    score = score + 1

if question4.lower() == true_answer4:
    score = score + 1

if question5.lower() == true_answer5:
    score = score + 1

if score >= 3:
    print('Вы набрали много баллов! Вас можно считать экспертом')
else:
    print('Вы набрали не очень много баллов. Расширяйте свой кругозор, вам есть, куда стремиться')

