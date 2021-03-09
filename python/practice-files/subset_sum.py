global N, total , answer
answer=0
def gen_subs(w):
  s=[0]*N
  for i in range(0,N):
    c_w=w[i]
    if c_w<=total:
      s[i]=1
      check_sum(w,s,c_w,i)
      s[i]=0

def check_sum(w,s,c_w,curr):
  if c_w==total:
    global answer
    answer+=1
    print(s)
    return
  for i in range(curr+1,N):
    if c_w+w[i]>total:
      return
    elif c_w+w[i]<=total:
      s[i]=1
      check_sum(w,s,c_w+w[i],i)
      s[i]=0
    

if __name__=='__main__':
  w=[10, 7, 5, 18, 12, 20, 15]
  N=len(w)
  total=35

  gen_subs(w)
  print(answer)
