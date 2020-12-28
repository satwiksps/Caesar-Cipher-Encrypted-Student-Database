dic = {}
# ENTERED PASSWORD WILL SHIFT THE LETTERS OR DIGITS BY THE VALUE OF PASSWORD 
#SUPPOSE PASSWORD IS 2 AND STRING IS SATWIK THE ENCRYPTION WILL BE UCVYKM
#SUPPOSE PASSWORD IS 13 AND NUMBER IS 1911 THE ENCRYPTION WILL BE 3133
shift=int(input("Set up a numeric password(any digit) :"))
while True  :
    named = input("Enter student's name to add in the database (A:Add more data  Q:Quit  S:Search  P:Print encrypted Dictionary ) :  ")
    
    if named == "Q" or named == "q" :
        break
    if named == "P" or named == "p" :
        print(dic)
    if named == "S" or named == "s" :
        shift2=int(input("Enter your password"  ))
        if shift2!=shift:
            while True:
                print("INCORRECT PASSWORD PLEASE CHECK AND RETYPE")
                shift2=int(input("Enter your password"))
                if shift2==shift:
                    break
        name=input("Enter name to search for :") 
        cipher1=''
        for char in name:
            if char==' ':
                cipher1+=char
            elif char.isupper():
                cipher1+=chr((ord(char)+shift2-65)%26+65)
            elif char.isdigit():
                cipher1+=chr((ord(char)+shift-48)%10+48)
            else:
                cipher1+=chr((ord(char)+shift2-97)%26+97)
                
        for student in dic:
            if student==cipher1:
                for x in dic[student]:
                    ciphere=''
                    for char in x:
                        if char==' ':
                            ciphere+=char
                        elif char.isupper():
                            ciphere+=chr((ord(char)-shift2-65)%26+65)
                        elif char.isdigit():
                            ciphere+=chr((ord(char)-shift-48)%10+48)
                        else:
                            ciphere+=chr((ord(char)-shift2-97)%26+97)
                    if x==dic[student][0]:
                        print("CLASS-->",end=" ")
                        
                    if x==dic[student][1]:
                        print("SEC-->",end=" ")
                        
                    if x==dic[student][2]:
                        print("THEORY MARK-->",end=" ")
                        
                    if x==dic[student][3]:
                        print("PRACTICAL MARK-->",end=" ")
                        
                    print(ciphere)
            else:
                print('No entry with that name was found.')
            
            
        
    elif named!="p" and named!="P":
        #CAESAR CIPHER ENCRYPTION FOR NAME 
        cipher=""
        for char in named:
            if char==' ':
                cipher=cipher+char
            elif char.isupper():
                cipher=cipher+chr((ord(char)+shift-65)%26+65)
            else:
                cipher=cipher+chr((ord(char)+shift-97)%26+97)
       #CAESAR CIPHER ENCRYPTION FOR THEORY MARKS
        mark1 = input("Enter marks secured in theory = ")
        cipherm1=''
        for char in mark1:
            if char==' ':
                cipherm1+=char
            elif char.isupper():
                cipherm1=cipherm1+chr((ord(char)+shift-65)%26+65)
            elif char.isdigit():
                cipherm1+=chr((ord(char)+shift-48)%10+48)
            else:
                cipherm1=cipherm1+chr((ord(char)+shift-97)%26+97)        
        #CAESAR CIPHER ENCRYPTION FOR PRACTICAL MARKS 
        mark2 = input("Enter marks secured in practical = ")
        cipherm2=''
        for char in mark2:
            if char==' ':
                cipherm2=cipherm2+char
            elif char.isupper():
                cipherm2=cipherm2+chr((ord(char)+shift-65)%26+65)
            elif char.isdigit():
                cipherm2+=chr((ord(char)+shift-48)%10+48)
            else:
                cipherm2=cipherm2+chr((ord(char)+shift-97)%26+97)     
        #CAESAR CIPHER ENCRYPTION FOR SEC 
        sec=input("Enter Section  : ")
        ciphersec=''
        for char in sec:
            if char==' ':
                ciphersec=ciphersec+char
            elif char.isupper():
                ciphersec=ciphersec+chr((ord(char)+shift-65)%26+65)
            else:
                ciphersec=ciphersec+chr((ord(char)+shift-97)%26+97)
        #CAESAR CIPHER ENCRYPTION FOR CLASS 
        clas=input("Enter Class  : ")
        cipherclass=''
        for char in clas:
            if char==' ':
                cipherclass=cipherclass+char
            elif char.isupper():
                cipherclass=cipherclass+chr((ord(char)+shift-65)%26+65)
            elif char.isdigit():
                cipherclass+=chr((ord(char)+shift-48)%10+48)
            else:
                cipherclass=cipherclass+chr((ord(char)+shift-97)%26+97)
                
        
        dic[cipher] = [cipherclass,ciphersec,cipherm1,cipherm2]

