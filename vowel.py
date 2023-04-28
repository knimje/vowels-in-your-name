#write a user define function that prints the count of vowels in the name entered by the user 
name=input("enter your name ")
l=["a","e","i","o","u","A","E","I","O","U"]
def vowel(name):
    count=0
    for i in name:
        for j in l:
            if i ==j:
                count+=1
                print(i)
    print(count)
vowel(name)