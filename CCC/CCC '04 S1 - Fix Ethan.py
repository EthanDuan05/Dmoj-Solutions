N = int(input())

for _ in range(N):
    word_1 = input()
    word_2 = input()
    word_3 = input()

    debug = False

    word_1_prefix = True
    word_1_suffix = True

    word_2_prefix = True
    word_2_suffix = True

    word_3_prefix = True
    word_3_suffix = True

    word_1_pre = word_1[0:N]
    word_1_suf = word_1[-N:]

    word_2_pre = word_2[0:N]
    word_2_suf = word_2[-N:]

    word_3_pre = word_3[0:N]
    word_3_suf = word_3[-N:]

    if debug:
        print(word_1_pre, word_1_suf)
        print(word_2_pre, word_2_suf)
        print(word_3_pre, word_3_suf)

    pre_1 = len(word_1_pre)
    suf_1 = len(word_1_suf)

    pre_2 = len(word_2_pre)
    suf_2 = len(word_2_suf)

    pre_3 = len(word_3_pre)
    suf_3 = len(word_3_suf)

    # word 1 pre
    if len(word_1) < N:
        if word_1 == word_2[0: len(word_1)]:
            word_1_prefix = False
    else:
        if word_1[0: pre_2] == word_2_pre:
            word_1_prefix = False

    if len(word_1) < N:
        if word_1 == word_3[0: len(word_1)]:
            word_1_prefix = False
    else:
        if word_1[0: pre_3] == word_3_pre:
            word_1_prefix = False

    # word 1 suf
    if len(word_1) < N:
        if word_1 == word_2[-len(word_1):]:
            word_1_suffix = False
    else:
        if word_1[-suf_2:] == word_2_suffix:
            word_1_suffix = False

    if len(word_1) < N:
        if word_1 == word_3[-len(word_1):]:
            word_1_suffix = False
    else:
        if word_1[-suf_3] == word_3_suffix:
            word_1_suffix = False

    # word 2 pre
    if len(word_2) < N:
        if word_2 == word_1[0: len(word_2)]:
            word_2_prefix = False
    else:
        if word_2[0:pre_1] == word_1_pre:
            word_2_prefix = False

    if len(word_2) < N:
        if word_2 == word_3[0: len(word_2)]:
            word_2_prefix = False
    else:
        if word_2[0: pre_3] == word_3_pre:
            word_2_prefix = False

    # word 2 suf
    if len(word_2) < N:
        if word_2 == word_1[-len(word_2):]:
            word_2_suffix = False
    else:
        if word_2[-suf_1:] == word_1_suffix:
            word_2_suffix = False

    if len(word_2) < N:
        if word_2 == word_3[-len(word_2):]:
            word_2_suffix = False
    else:
        if word_2[-suf_3:] == word_3_suffix:
            word_2_suffix = False

    # word 3 pre
    if len(word_3) < N:
        if word_3 == word_1[0: len(word_3)]:
            word_3_prefix = False
    else:
        if word_3[0:pre_1] == word_1_pre:
            word_3_prefix = False

    if len(word_3) < N:
        if word_3 == word_2[0: len(word_3)]:
            word_3_prefix = False
    else:
        if word_3[0:pre_2] == word_2_pre:
            word_3_prefix = False

    # word 3 suf
    if len(word_3) < N:
        if word_3 == word_1[-len(word_3):]:
            word_3_suffix = False
    else:
        if word_3[-suf_1:] == word_1_suffix:
            word_3_suffix = False

    if len(word_3) < N:
        if word_3 == word_2[-len(word_3):]:
            word_3_suffix = False
    else:
        if word_3[-suf_2:] == word_2_suffix:
            word_3_suffix = False

    if (word_1_prefix and word_1_suffix) and (word_2_prefix and word_2_suffix) and (word_3_prefix and word_3_suffix):
        print('Yes')
    else:
        print('No')