from time import time as t

chi_pow = {16:"兆", 8:"亿", 4:"万", 3:"千", 2:"百", 1:"十", 0:""}
pows = list(chi_pow.keys())
chars = list(chi_pow.values())
chars.reverse()

chi_digi = ["零", "一", "二", "三", "四", "五", "六", "七", "八", "九"]

def next_lowest_power(num):
    curr = len(str(num)) - 1
    #print(curr)
    index = 0

    while curr < pows[index]:
        #print(index, pows[index])
        index += 1

    nlp = pows[index]

    return nlp
    


def change(num):
    if len(str(num)) == 0:
        return

    s = str(num)
    l = len(s)
    p = l - 1

    if p in pows:
        res = ""

        res += (chi_digi[int(s[0])] + chi_pow[p])
        p -= 1

        if res[-1] == "零":
            return res[:-1]
        else:
            return res
    
    else:
        nlp = next_lowest_power(num)
        print(nlp)

        n1 = s[:-nlp]
        n2 = s[-nlp:]

        print(n1, n2)

        #return change(n1) + change(n2)
        return change(n1) + chi_pow[nlp] + change(n2)


if __name__ == "__main__":
    r = change(12345678)
    print(r)