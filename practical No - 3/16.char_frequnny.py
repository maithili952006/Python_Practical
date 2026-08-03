string = input("Enter the string : ")

printed = ""

for ch in string:
    count = 0
    
    found = 0
    
    for i in printed:
        if ch == i:
            found = 1
            break
        
    if found == 0:
        for i in string:
            if ch == i:
                count = count + 1

        print(ch,"=",count)
        printed = printed + ch


