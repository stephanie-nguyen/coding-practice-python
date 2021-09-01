'''
Given a string sentence, loop through string and add line break after every 10 characters.
'''

def word_wrap(sentence,line_length):
  lines=[]
  for i in range(0, len(sentence), line_length):
    lines.append(sentence[i:i+line_length]+ "\n")
  return "".join(lines)

sentence="The quick brown fox jumps over the lazy dog"
line_length=10
print(word_wrap(sentence,line_length))
