def letterCombinations(digits: str):
    if len(digits) == 0:
        return []

    D = {"2": "abc", "3": "def", "4": "ghi",
         "5": "jkl", "6": "mno", "7": "pqrs",
         "8": "tuv", "9": "wxyz"}

    output = []
    def backtrack(comb, nxt_digits):
        if len(nxt_digits) == 0:
            output.append(comb)

        else:
            for i in D[nxt_digits[0]]:
                backtrack(comb + i, nxt_digits[1:])


    backtrack('', digits)
    return output

print(letterCombinations("23"))