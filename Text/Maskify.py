def maskify(s: str) -> str:
    s_li = list(s)
    final = []

    for el in s_li[:-4]:
        if el in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            final.append('#')
        else:
            final.append(el)

    final = final + s_li[-4:]

    return ''.join(final)
