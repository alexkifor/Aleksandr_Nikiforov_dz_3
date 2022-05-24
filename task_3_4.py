def thesaurus_adv(*args):
    out = {}
    for elem in args:
        name, surname = elem.split()
        if not out.get(surname[0]):
            out[surname[0]] = {name[0]: [elem]}
        elif not out[surname[0]].get(name[0]):
            (out[surname[0]])[name[0]] = [elem]
        else:
            (out[surname[0]])[name[0]].append(elem)
    return out

print(thesaurus_adv('Петр Алексеев', 'Илья Иванов', 'Иван Сергеев', 'Инна Серова', 'Анна Савельева'))
