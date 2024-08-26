def upperCase(word):
    result=[]
    for char in word:
        if 'a'<=char<='z':
            result.append(chr(ord(char)-32))
        else:
            result.append(char)

    return ''.join(result)            

def reverse(word):
    reversedResult=""
    for char in word:
        reversedResult=char+reversedResult
    return    reversedResult


def capitalize(word):
    if 'a'<=word[0]<='z':
        firstletter=chr(ord(word[0])-32)
    else:
        firstletter=word[0]
    return firstletter+word[1:]



def formatStr(word,operation):
    test=word
    for i in operation:
        if i=="upperCase":
            test=upperCase(word)
        if i=="reverse" :
            test=reverse(test)
        if i== "capitalize":
            test=capitalize(test)
    return test

print(formatStr("hello world",['upperCase','reverse']))          

