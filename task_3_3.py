def thesaurus(*names):
    out = {}
    for name in names:
        key = name[0]
        if key not in out:
            out.setdefault(key, name)
        else:
            out_1 = {}
            out_1.setdefault(key, name)
            for key, val in out_1.items():
                if out.get(key):
                    out[key] = [out[key], val]
    return out
print(thesaurus('Мария', 'Игорь', 'Ирина', 'Елена', 'Евгений'))
