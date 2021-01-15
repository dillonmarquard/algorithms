# Dillon Marquard
# Decoder
def toInt(word):
    num = ""
    for c in word:
        num += str(ord(c)-65)
    return num
testcase = input("Enter a word to encode:")
testcase = testcase.upper() # encode
data = toInt(testcase) # test number
cdata = [] # queue
for x in data:
    cdata.append(x) # split into numbers
queue = [cdata]
count = 0
while True: # ends if goes through entire queue with no new combination
    temp = queue.pop(0)
    for i in range(len(temp)-1):
        if temp[i] != "0" and int(temp[i]+temp[i+1]) < 26: # 26 letters in the alphabet
            n = temp[i]+temp[i+1] # modify code and combine two characters if the number it creates is less than 26
            temp1 = temp.copy()
            temp1.pop(i+1)
            temp1[i] = n
            if temp1 not in queue: # only add unique elements
                queue.append(temp1)
                count = 0 # reset count after adding new code to queue
    queue.append(temp)
    count += 1 # increment count
    if count > len(queue):
        break

possiblewords = []
for code in queue:
    word = ""
    for char in code:
        word = word + chr(int(char)+65)
    print(word,code)
    possiblewords.append(word)

print("is",testcase,"in possiblewords?",testcase in possiblewords)

