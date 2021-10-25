import pyttsx3

engine = pyttsx3.init()     # инициализация движка

# зададим свойства
engine.setProperty('rate', 400)     # скорость речи
engine.setProperty('volume', 0.9)   # громкость (0-1)


pastry = {'наполеон': [['масло', 'мука', 'сахар'], 7, 1000],
          'медовик': [['мука', 'масло', 'сахар'], 4, 1025],
          'киевский': [['сахар', 'мука', 'масло'], 5, 985]}
engine.say('''Если вы хотите посмотреть описание, введите 1
Посмотреть цену - введите 2
Посмотреть количество - введите 3
Посмотреть всю информация - введите 4
Если хотите приобрести торт, введите 5
Для выхода из программы введите 0''')
engine.runAndWait()

while True:
        choice = int(input('Сделайте ваш выбор! '))
        if choice == 0:
            break
        else:
            cake = input('Какой торт вас интересует? ')
            for k, v in pastry.items():
                if cake == k:
                    if choice == 1:
                        engine.say(f'Торт {cake} состоит из {v[0]}')
                        engine.runAndWait()
                    elif choice == 2:
                        engine.say(f'Торт {cake} стоит {v[1]} рублей')
                        engine.runAndWait()
                    elif choice == 3:
                        engine.say(f'Торта {cake} осталось {v[2]} грамм')
                        engine.runAndWait()
                    elif choice == 4:
                        engine.say(f'Торт {cake} состоит из {v[0]}')
                        engine.say(f'Торт {cake} стоит {v[1]}')
                        engine.say(f'Торта {cake} осталось {v[2]} грамм')
                        engine.runAndWait()
                    elif choice == 5:
                        engine.say('Какое количество торта вы хотите приобрести? ')
                        engine.runAndWait()
                        amount = int(input('Какое количество торта вы хотите приобрести? '))
                        if amount <= v[2]:
                            total = amount * v[1] / 100
                            engine.say(f'К оплате {total}')
                            engine.runAndWait()
                            engine.say(f'Торта осталось {v[2] - amount} грамм')
                            engine.runAndWait()
                            v[2] = v[2] - amount
                        else:
                            engine.say(f'Торта всего  {v[2]} грамм')
                            engine.runAndWait()

