# str1 = input("Enter the string : ")
# str2 = input("Enter the string : ")

# if sorted(str1) == sorted(str2):
#     print("Anagram")
# else:
#     print("Not anagram")    


#without using the built in function

str1 = input("Enter the string 1 : ")
str2 = input("Enter the string 2 : ")

count1 = 0
count2 = 0

for ch in str1:
    count1 += 1

for ch in str2:
    count2 += 1
   
if count1 != count2:
    print("not Anagram")
else:          
    
    for i in str1:
    
        result = 1
    
        c1 = 0
        c2 = 0
    
        for ch in str1:
            if ch == i:
                c1 += 1
      
        for ch in str2:
            if ch == i:
                c2 += 1
           
        if c1 != c2:
            result = 0
            break
    
    if result == 1:
        print("Anagram")    
    else:
        print("Not anagram")    
     

                         
        