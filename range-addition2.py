def maxCount(m,n,ops):
  min_row=m
  min_col=n
  for i in range(len(ops)):
    min_row=min(min_row, ops[i][0])
    min_col=min(min_col, ops[i][1])
  return min_row*min_col

m=3
n=3
ops=[[2,2],[3,3]]

print(maxCount(m,n,ops))
