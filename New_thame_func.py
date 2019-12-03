def new_func_search_text_in_progress(s1, s2):

    result = 0
    s2_to = s2

    for i in s1:
        if i in s2_to:
            s2_to = s2_to.replace(i, '', 1)
            result += 1

    r1 = int(result / len(s1) * 100)
    r2 = int(result / len(s2) * 100)

    return '{}%'.format(r1 if r1 < r2 else r2)


s1 = 'hellow'

s2 = input('_').lower()
print(new_func_search_text_in_progress(s1, s2))