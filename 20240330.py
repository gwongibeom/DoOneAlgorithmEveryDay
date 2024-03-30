# 2083 Bronze 4
isNotDone = True
checkedMens = []

def CheckJuniorSenior():
  global isNotDone
  men = input().split(" ")

  if(men[0] == "#"): 
    isNotDone = False
    return

  if(int(men[1]) > 17):
    checkedMens.append(men[0]+" "+"Senior")
  elif(int(men[2]) >= 80):
    checkedMens.append(men[0]+" "+"Senior")
  else: 
    checkedMens.append(men[0]+" "+"Junior")

while isNotDone:
  CheckJuniorSenior()


for i in range(len(checkedMens)):
  print(checkedMens[i])