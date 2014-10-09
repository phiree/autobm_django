__author__ = 'Administrator'

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        print(self.name+'_'+str(self.age))
if __name__=='__main__':
    p1={'name':'phiree'}
    p2={'name':'james'}

    p1.update(p2)
    print(p1)