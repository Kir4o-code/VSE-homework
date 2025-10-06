words = ["level", "python", "radar", "java", "civic", "kotlin", "refer"]
palindromes=[]
x=[]
y=[]

for word in words:
   i=int(len(word)/2)
   j=len(word)
   if(j%2==1):
    x=word[0:i+1] 
    y=word[i:j]
   else:
    x=word[0:i] 
    y=word[i:j]
   print(x)
   print(y)
   if x==y[::-1]:
      palindromes.append(word)

print(f"The palindromes are {palindromes}.")