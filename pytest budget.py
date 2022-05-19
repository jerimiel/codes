class Category():
    def __init__(self,name):
        self.ledger=[]
        self.deposit_=0
        self.withdraw_=0
        self.name=name
        
        
    def deposit(self,amount,description=''):
        deposit={}
        deposit['amount']=amount
        deposit['description']=description
        self.ledger.append(deposit)
        self.deposit_=self.deposit_+amount
        

    def withdraw(self,amount,description=''):
        if self.deposit_ < amount:
            ans=False
        else:
            withdraw={}
            withdraw['amount']=amount*-1
            withdraw['description']=description
            self.withdraw_=self.withdraw_+amount
            self.ledger.append(withdraw)
            ans=True
        return ans
    
            
    def get_balance(self):
        return self.deposit_ - self.withdraw_
        

    def transfer(self,amount,category):
        if self.deposit_ < amount:
            ans = False
        else:
            withdraw={}
            deposit={}
            deposit['amount']=amount
            deposit['description']="Transfer from "+self.name
            withdraw['amount']=amount*-1
            withdraw['description']="Transfer to "+category.name
            category.deposit_=category.deposit_+amount
            self.withdraw_=self.withdraw_+amount
            self.ledger.append(withdraw)
            category.ledger.append(deposit)
            ans = True
        return ans
    

    def check_funds(self,amount):
        if amount > self.deposit_:
            ans=False
        else:
            ans=True
            
        return ans

    def __str__(self):
        
        a=len(self.name)
        top=30-a
        top=round(top/2)
        top=((top)*"*")+self.name.capitalize()+("*"*top)
        heex=''
        for i in self.ledger:
            
            amt=i['amount']
            if len((str(round(amt)))+".00")<=7:
                gee=i['description'][0:23]+(" "*(23-len(i['description']))) + (" "*(7-len(str(round(amt))+".00")))+"%.2f"%(amt)
                
            else:
                gee=i['description'][0:23]+(" "*(23-len(i['description']))) +str(round(amt))[0:4]+".00"

            heex=heex+gee+'\n'
                
        return top+'\n'+heex+"Total: "+str(self.deposit_-self.withdraw_)



def create_spend_chart(li):
    total=0
    with_d=[]
    percent=[]
    markers=[]

    
    for i in li:
        total=total+i.withdraw_
        with_d.append(i.withdraw_)
    for i in with_d:
        per=(i/total)        
        per=int(per*10)
        percent.append(per+1)
    for i in percent:
        markers.append((' '*(11-i))+('o'*i))
    le=len(markers)
    if len(markers)<4:
        a=4-len(markers)
        for i in range(0,a):
            markers.append(str(' ')*(11))
    per="Percentage spent by category"
    d_y=''     
    for i in range(0,11):
        p=100-(i*10)
        if len(str(p))==2:
            p=" "+str(p)
        if len(str(p))==1:
            p="  "+str(p)
            
        yaxis=str(p) +"|"+" "+markers[0][i]+"  "+markers[1][i]+"  "+markers[2][i]+"  "
        d_y=d_y+yaxis+'\n'
    xaxis=("    "+"-"*(10))
    longest=0
    g=[]
    for i in li:
        g.append(i.name)
        if len(i.name)>longest:
            longest=len(i.name)

    if len(li)<4:
        a=4-len(li)
        for i in range(0,a):
            g.append(str(' ')*longest)

    for i in li:
        index=g.index(i.name)
        if len(i.name)<longest:
            g[index]=i.name+(' '*(longest-len(i.name)))
            
    
    title=''
    for i in range(0,longest-1):
        k=("     "+g[0][i]+"  "+g[1][i]+"  "+g[2][i]+"  ")
        title=title+k+'\n'
    i=longest-1
    k=("     "+g[0][i]+"  "+g[1][i]+"  "+g[2][i]+"  ")
    title=title+k
    return per+'\n'+d_y+xaxis+'\n'+title

    
food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
print(food.get_balance())
clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)

#test

food = Category("Food")
entertainment = Category("Entertainment")
business =Category("Business")


        
food.deposit(900, "deposit")
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")
food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)
actual = create_spend_chart([business, food, entertainment])
expected = "Percentage spent by category\n100|          \n 90|          \n 80|          \n 70|    o     \n 60|    o     \n 50|    o     \n 40|    o     \n 30|    o     \n 20|    o  o  \n 10|    o  o  \n  0| o  o  o  \n    ----------\n     B  F  E  \n     u  o  n  \n     s  o  t  \n     i  d  e  \n     n     r  \n     e     t  \n     s     a  \n     s     i  \n           n  \n           m  \n           e  \n           n  \n           t  "
print(actual,expected)
































        
        
        
        
        
            
        
        
        
