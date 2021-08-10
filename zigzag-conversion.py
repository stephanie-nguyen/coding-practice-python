'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
'''

def convert(s, numRows):
    arrays = [[] for x in range(numRows)]
    
    cur = 0
    forward = True
    for x in s:
        if forward == True and cur<numRows:
            arrays[cur].append(x)
            
            if cur == numRows - 1 and numRows != 1:
                forward= False
            else:
                cur = cur + 1
        elif cur > 0:
            cur = cur - 1
            arrays[cur].append(x)
            
            if cur == 0:
                forward= True
                cur = cur + 1
                
    arrays = ''.join([''.join(arrays[x]) for x in range(len(arrays))])
    
    return arrays

s='paypalishiring'
numRows=3
print(convert(s,numRows))
