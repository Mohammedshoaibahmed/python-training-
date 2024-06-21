g={1:[(1,2,0),(1,3,0)],
  2:[(2,1,0),(2,7,0)],
3:[(3,1,0),(3,6,0),(3,5,0)],
4:[(4,7,0),(4,8,0)],
5:[(5,3,0),(5,7,0)],
6:[(6,3,0),(6,8,0)],
7:[(7,2,0),(7,5,0),(7,4,0)],
8:[(8,4,0),(8,6,0)]}
vd={}
vd=vd.fromkeys(g,False)
# def dfs(g, vd, node):
#     if not vd[node]:
#         vd[node] = True
#         for edge in g[node]:
#             next_node = edge[1]
#             if not vd[next_node]:
#                 dfs(g, vd, next_node)
#         print(node,end=' ')
def dfs_1(g,vd,s,stack):
    if vd[s]==False:
        stack.append(s)
        vd[s]=True
    else:
        return
    for i in g[s]:
        dfs_1(g,vd,i[1],stack)
    print(stack.pop(),end=' ') 
stack=[]
dfs_1(g, vd, 1,stack)
