def gen_str(n, alp, pref):
    if len(pref) < n:
        ans = []
        for a in alp:
            ans += gen_str(n, alp, pref + a)
        return ans
    else:
        return [pref]

def test_sort(scheme):
    alp = ['a', 'b', 'c']
    tests = gen_str(8, alp, '')
    for this_test in tests:
        if use_scheme(scheme, this_test) != ''.join(sorted(this_test)):
            print("WRONG TEST:", this_test)
            return
    print("OK")




def make_scheme():
    scheme = []
    fin = open("system.txt", "r")
    n = int(fin.readline())
    for i in range(n):
        line = fin.readline().rstrip()
        initial, final, dot = line.split()
        if initial == "Eps":
            initial = ''        
        if final == "Eps":
            final = ''
        scheme.append((initial, final, dot == '.'))
    fin.close()
    return scheme


def use_substitution(string, subs):
    i = string.find(subs[0])
    if i == -1:
        return -1  # this substitution is impossible
    else:
        return string.replace(subs[0], subs[1], 1)  # this substitution is possible
        

def use_scheme(scheme, string):
    i = 0
    while i < len(scheme): # while we have posible substitution
        while i < len(scheme) and use_substitution(string, scheme[i]) == -1:
            i += 1  # find possible substitution
        if i < len(scheme):
            string = use_substitution(string, scheme[i])
            if scheme[i][2]:
                break # it's final substitution
            i = 0
    return(string)


def main():
    while True:
        command = input()
        if command == "sys":
            # created new scheme
            scheme = make_scheme()
            print("Success")
        elif command == "trans":
            print("input: ", end='')
            inp = input()            
            print("aswer:", use_scheme(scheme, inp))
        elif command == "test":
            # testing the correctness of the sorting
            test_sort(scheme)
        else:
            break
main()