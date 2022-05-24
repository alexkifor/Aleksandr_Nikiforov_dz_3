import random

nouns = ['автомобиль', 'лес', 'огонь', 'город', 'дом']
abverbs = ['сегодня', 'вчера', 'завтра', 'позавчера', 'ночью']
abjectivs = ['веселый', 'яркий', 'зеленый', 'утопичный', 'мягкий']

def get_jokes(num, repeats = True):
    jokes = []
    if repeats == False:
        if num > 5:
            print('Ваш запрос не может быть выполнен')
        else:
            for i in range(num):
                noun = random.choice(nouns)
                nouns.remove(noun)
                abverb = random.choice(abverbs)
                abverbs.remove(abverb)
                abjectiv = random.choice(abjectivs)
                abjectivs.remove(abjectiv)
                jokes.append(f'{noun} {abverb} {abjectiv}')
            return (jokes)
    else:
        if num > 125:
            print('Превышено максимальное количество шуток')
        else:
            for i in range(num):
                noun = random.choice(nouns)
                abverb = random.choice(abverbs)
                abjectiv = random.choice(abjectivs)
                jokes. append(f'{noun} {abverb} {abjectiv}')
            return(jokes)

print(get_jokes(4, repeats=False))
print(get_jokes(8, repeats=False))
print(get_jokes(5, repeats=True))
print(get_jokes(126, repeats=True))






