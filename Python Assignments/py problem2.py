from itertools import permutations
def valid_para(com):
        balance = 0
        for c in com:
            if c == "(":
                balance += 1
            elif c == ")":
                balance -= 1
            if balance < 0:
                return False
        return balance == 0
def gen_parenthesis(n):    
    combo = set(permutations("(" * n + ")" * n))
    parenthesis = ["".join(com) for com in combo if valid_para(com)]
    return parenthesis

n = 3
if -1 <= n <= 8:
    print(gen_parenthesis(n))

else:
    print("invalid input")
