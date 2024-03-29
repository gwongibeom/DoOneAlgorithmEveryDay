# 1264 Bronze 4

vowels = ['a', 'e', 'i', 'o', 'u']
numberOfVowelsArr=[]
isNotDone = True

def CheckVowels():
  global isNotDone
  numberOfVowels = 0
  tempInput = input().lower()

  if(tempInput == "#"):
    isNotDone = False
    return

  for i in range(len(tempInput)):
    for j in range(len(vowels)):
      if(tempInput[i] == vowels[j]):
        numberOfVowels += 1
  numberOfVowelsArr.append(numberOfVowels)


while isNotDone == True : 
  CheckVowels()

for i in range(len(numberOfVowelsArr)):
  print(numberOfVowelsArr[i])

