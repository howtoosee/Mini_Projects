from time import time as t

chi_pow = {32:"兆兆", 16:"兆", 8:"亿", 4:"万", 3:"千", 2:"百", 1:"十", 0:""}
pows = list(chi_pow.keys())

chi_digi = ["零", "一", "二", "三", "四", "五", "六", "七", "八", "九"]



def next_lowest_power(num):
    curr = len(str(num)) - 1
    index = 0

    while curr < pows[index]:
        #print(index, pows[index])
        index += 1

    nlp = pows[index]

    return nlp



def calc(num):
    if len(str(num)) == 0:
        return

    s = str(num)
    l = len(s)
    p = l - 1

    if p <= 4:
        res = ""

        for i in range(len(s)):
            if s[i] == '0':
                res += "零"
            else:
                res += (chi_digi[int(s[i])] + chi_pow[p])
            p -= 1
        
        if res[-1] == "零":
            return res[:-1]

        else:
            return res
    

    else:
        nlp = next_lowest_power(num)
        #print(nlp)

        n1 = s[:-nlp]
        n2 = s[-nlp:]

        #print(n1, n2)

        return calc(n1) + chi_pow[nlp] + calc(n2)



def change(num):
    res = ""
    if num < 0:
        res = "负"
        num *= -1

    r = calc(num)

    if r[:2] == "一十":
        r = r[1:]
    
    res += r.replace("零零零", "零").replace("零零", "零")

    return res



if __name__ == "__main__":
    start = t()

    r = change(-123456789012345678901234567890)
    
    duration = t()-start

    print(r)
    print("{:.10f}sec".format(duration))