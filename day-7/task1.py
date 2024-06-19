project_m = [3,5,2,14,5,3,7,9,4,6,9,4,19,2,5,3]
# stack = []
supervisor = []
top = 0
for i in range(len(project_m)-1):
  cnt = 0
  for j in range(i+1,len(project_m)):
    if project_m[i]<project_m[j]:
      cnt+=1
      supervisor.append(project_m[j])
      break
  if cnt ==0 :
    supervisor.append(-1)
supervisor.append(-1)

print(supervisor) 

#using the stack implementing the problem

'''
inp = [3,5,2,14,5,3,7,9,4,6,9,4,19,2,5,3]
out = [-1] * len(inp)
stack = []
for i in range(len(inp)-1,-1,-1):
  while stack and stack[-1] <=inp[i]:
    stack.pop()
  if stack:
    out[i] = stack[-1]
  else:
    out[i] = -1
  stack.append(inp[i])
print(out)'''