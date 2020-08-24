encode = {'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.',
          'G':'--.', 'H':'....', 'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..',
          'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-', 'R':'.-.',
          'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-',
          'Y':'-.--', 'Z':'--..', '_':'..--', '.':'---.', ',':'.-.-', '?':'----'}
decode = {}
for x in encode:
    decode[encode[x]] = x

while True:
    try:
        s = input()
        t = ""
        c = ""
        for x in s:
            t += encode[x]
            c += str(len(encode[x]))
        c = c[::-1]
        r = ""
        i = 0
        for x in c:
            l = int(x)
            r += decode[t[i:i+l]]
            i += l
        print(r)
    except EOFError:
        break
