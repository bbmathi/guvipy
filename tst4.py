n=input()    
if (n>='a' and n<='z')or (n>='A' and n<='Z'):
    if n=="a" or n=="e" or n=="i" or n=="o" or n=="u":
        print("vowel")
    else:
        print("consonant")
else:
    print("invalid")
