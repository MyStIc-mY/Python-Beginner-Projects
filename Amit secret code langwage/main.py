messege=input("Enter your messege :")
a=input("Do you want to encode a messege :")

words=messege.split(" ")
nword=[]
if a=="yes":
 for word in words:
    if len(word)<3:
        nword.append(word[::-1])
        
    else:
        new=word[1:] +word[0]
        new1=(f"{ " "}adcncnj{new}jnrjrfn {" "}")
        
        nword.append(new1)
        a=(("").join(nword))
print(a)        
         
b=input("do you want to decode a messege :")
decode_word=[]
wor=a.split(" ")
if b=="yes":
   
   for i in wor:
      if len(i)<3:
         decode_word.append(i[::-1])
      else:
         new2=i[-8]+i[7:-8]   
         decode_word.append(f"{""} {new2} {""}")
         c=((" ").join(decode_word))
print((("").join(decode_word)))
          
         
      
