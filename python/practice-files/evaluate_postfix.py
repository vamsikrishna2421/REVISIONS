class stack(object):
    def __init__(self):
        self.l=['']*100
        self.top=-1
    def push(self,data):
        self.top+=1
        # print(self.top)
        self.l[self.top]=data
    def pop(self):
        if self.top>=0:
            value=self.l[self.top]
            self.top-=1
            self.l[self.top+1]=''
            # print(self.top)
            return value
        else:
            return None
    def peek(self):
        if self.top>=0:
            return self.l[top]
        else:
            return None
    def display(self):
        if self.top==-1:
            print('empty stack')
            return
        print(' '.join(self.l))

exp='23*54*+9-'
s=stack()
# s.display()
for i in list(exp):
    if i=='+':
        s.push(str(int(s.pop())+int(s.pop())))
    elif i=='-':
        tmp=int(s.pop())
        s.push(str(int(s.pop())-tmp))
    elif i=='*':
        s.push(str(int(s.pop())*int(s.pop())))
    elif i=='/':
        tmp=int(s.pop())
        s.push(str(int(s.pop())/tmp))
    else:
        s.push(i)
    # s.display()
print(s.pop())
