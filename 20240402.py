def solution(s):
    if not s:
        return ""

    sArr = s.lower().split(" ")
    for i in range(len(sArr)):
        tempStringList = list(sArr[i])
        if tempStringList and not tempStringList[0].isnumeric():
            tempStringList[0] = str(tempStringList[0].upper())
            tempString = ''.join(tempStringList)
            sArr[i] = tempString

    answer = (' '.join(sArr))
    return answer
