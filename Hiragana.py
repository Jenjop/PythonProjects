import random,time

#Runs prints input character and waits for guess on romanization
def iterate(charList, i):
    print ('\t' + charList[i][0])
    if input('Input: \n').lower() == charList[i][1]:
        return True
    else:
        print('\t' + charList[i][1] + '\n')
        return False

#Iterates through given list in a random order
def loop(charList):
    tempList = charList[:]
    while len(tempList) > 0:
        j = random.choice(range(len(tempList)))
        correct = iterate(tempList,j)
        if correct:
            print('Correct')
            del tempList[j]
            continue
        else:
            tempList = charList[:]

#Combines multiple lists inside 2D list
def combine(charLists, i, f):    
    combined = [item for sublist in charLists[i:f+1] for item in sublist]
    loop(combined[:])

#Requests input range (index of first and last list to test)
def askRange():
    while True:
        try:
            in1 = int(input('Beginning of Range\n')) -1
            if 0 <= in1 < len(aChars):
                break
        except PermissionError:
            pass
    while True:
        try:
            in2 = int(input('End of Range\n')) -1
            if in1 <= in2 < len(aChars):
                break
        except PermissionError:
            pass
    return [in1,in2]


##chars_c1 = [['あ','a'],['い','i'],['う','u'],['え','e'],['お','o'],['は','ha'],['ひ','hi'],['ふ','hu'],['へ','he'],['ほ','ho']]

#Character rows (based on a chart)
chars_r1 = [['な','na'],['た','ta'],['さ','sa'],['か','ka'],['あ','a']]
chars_r2 = [['に','ni'],['ち','chi'],['し','shi'],['き','ki'],['い','i']]
chars_r3 = [['ぬ','nu'],['つ','tsu'],['す','su'],['く','ku'],['う','u']]
chars_r4 = [['ね','ne'],['て','te'],['せ','se'],['け','ke'],['え','e']]
chars_r5 = [['の','no'],['と','to'],['そ','so'],['こ','ko'],['お','o']]
chars_r6 = [['ん','n'],['わ','wa'],['ら','ra'],['や','ya'],['ま','ma'],['は','ha']]
chars_r7 = [['り','ri'],['み','mi'],['ひ','hi']]
chars_r8 = [['る','ru'],['ゆ','yu'],['む','mu'],['ふ','hu']]
chars_r9 = [['れ','re'],['め','me'],['へ','he']]
chars_r10 = [['を','wo'],['ろ','ro'],['よ','yo'],['も','mo'],['ほ','ho']]
chars_r11 = [['ぱ','pa'],['ば','ba'],['だ','da'],['ざ','za'],['が','ga']]
chars_r12 = [['ぴ','pi'],['び','bi'],['ぢ','di'],['じ','ji'],['ぎ','gi']]
chars_r13 = [['ぷ','pu'],['ぶ','bu'],['づ','dzu'],['ず','zu'],['ぐ','gu']]
chars_r14 = [['ぺ','pe'],['べ','be'],['で','de'],['ぜ','ze'],['げ','ge']]
chars_r15 = [['ぽ','po'],['ぼ','bo'],['ど','do'],['ぞ','zo'],['ご','go']]

#All lists combined
aChars = [chars_r1[:],chars_r2[:],chars_r3[:],chars_r4[:],chars_r5[:],chars_r6[:],chars_r7[:],chars_r8[:],chars_r9[:],chars_r10[:],chars_r11[:],chars_r12[:],chars_r13[:],chars_r14[:],chars_r15[:]]

while True:
    while True:
        in1 = input("L or R\n")#L for learn, R for Review
        if (in1.lower() == "r") | (in1 == "l"):
            break

    if in1.lower() == "r":
        in2, in3 = askRange()
        
        if in2==in3:
            loop(aChars[in2][:])
        else:
            combine(aChars[:],in2,in3)

    elif in1.lower() == "l":
        in2, in3 = askRange()
        if in2==in3:
            loop(aChars[in2][:])
        else:
            combined = aChars[in2][:]
            
            print('\tSet ' + str(in2 + 1))
            loop(aChars[in2][:])
            
            for i in range(in2+1,in3+1):
                print('\tSet ' + str(i + 1))
                loop(aChars[i][:])
                combined += aChars[i][:]
                print('\tReview')
                loop(combined[:])
    cont = input('Continue?') #Input of C, Y, Continue, Yes, or 1 will continue the loop
    cont = (cont.lower() == 'c') | (cont.lower() == 'continue') | (cont.lower() == 'y') | (cont.lower() == 'yes') | (cont == "1")
    if not cont:
        break
                

##print('Complete')
##time.sleep(2)
