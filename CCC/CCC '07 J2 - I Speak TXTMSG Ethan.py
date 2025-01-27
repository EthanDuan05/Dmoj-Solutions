txt_diction = {'CU': 'see you',
               ':-)': "I'm happy",
               ':-(': "I'm unhappy",
               ';-)': 'wink',
               ':-P': 'stick out my tongue',
               '(~.~)': 'sleepy',
               'TA': 'totally awesome',
               'CCC': 'Canadian Computing Competition',
               'CUZ': 'because',
               'TY': 'thank-you',
               "YW": "you're welcome",
               'TTYL': 'talk to you later'}


flag = True
while flag:
    k = input()
    if k == 'TTYL':
        print(txt_diction.get(k))
        flag = False
    else:
        if k in txt_diction:
            print(txt_diction.get(k))
        elif k not in txt_diction:
            print(k)