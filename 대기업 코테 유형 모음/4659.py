while True:
    isOk = [False, True, True]
    str = input()
    if str == 'end':
        break
        
    continuity2 = ''
    continuity3 = ['ja', 0]
    for i in str:
        if i in ['a', 'e', 'i', 'o', 'u']:
            isOk[0] = True
            if continuity3[0] == 'ja':
                continuity3 = ['mo', 1]
            else:
                continuity3[1]+=1
                if continuity3[1] == 3:
                    isOk[1] = False;
                    break;
        else:
            if continuity3[0] == 'mo':
                continuity3 = ['ja', 1]
            else:
                continuity3[1]+=1
                if continuity3[1] == 3:
                    isOk[1] = False;
                    break;
        
        if i == continuity2:
            if i == 'e' or i == 'o':
                continue
            else:
                isOk[2] = False;
                break;
        else:
            continuity2=i
    
    if(False in isOk):
        print('<'+str+'> is not acceptable.')
    else:
        print('<'+str+'> is acceptable.')
        