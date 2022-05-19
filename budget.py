class category():
    def __init__(self):
        self.ledger=[]
        self.deposit_=0
        self.withdraw_=0
        
        
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
        print("Your balance is: ",self.deposit_-self.withdraw_)
        

    def transfer(self,amount,category,a):
        if self.deposit_ < amount:
            ans = False
        else:
            withdraw={}
            deposit={}
            deposit['amount']=amount
            deposit['description']="Transfer from "+a[0]
            withdraw['amount']=amount*-1
            withdraw['description']="Transfer to "+a[1]
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

    def __str__(self,name):
        
        a=len(name)
        top=30-a
        top=round(top/2)
        print(((top-1)*"*")+name.capitalize()+("*"*top))
        for i in self.ledger:
            amt=i['amount']
            if len((str(round(amt)))+".00")<=7:
                print(i['description']+(" "*(22-len(i['description']))) + (" "*(7-len(str(round(amt))+".00")))+"%.2f"%(amt))
            else:
                print(i['description'][0:22]+(" "*(22-len(i['description']))) + str(round(amt))[0:4]+".00")
                
        print("Total: "+str(self.deposit_-self.withdraw_))



def create_spend_chart(li):
    total=0
    with_d=[]
    percent=[]
    markers=[]

    
    for i in li:
        total=total+eval(i.lower()).withdraw_
        with_d.append(eval(i.lower()).withdraw_)
    for i in with_d:
        per=(i/total)*100
        per=round(per/10)
        percent.append(per)
    for i in percent:
        markers.append((' '*(11-i))+('o'*i))
    g=len(markers)
    if len(markers)<4:
        a=4-len(markers)
        for i in range(0,a):
            markers.append(str(' ')*11)
    print("Percentage Spent by Categories")
            
    for i in range(0,11):
        p=100-(i*10)
        if len(str(p))==2:
            p=" "+str(p)
        if len(str(p))==1:
            p="  "+str(p)
            
        print(str(p) +" |"+" "+markers[0][i]+" "+markers[1][i]+" "+markers[2][i]+" "+markers[3][i])
        
    print("     "+"-"*(g*2))
    longest=0
    for i in li:
        if len(i)>longest:
            longest=len(i)

    if len(li)<4:
        a=4-len(li)
        for i in range(0,a):
            li.append(str(' ')*longest)

    for i in li:
        index=li.index(i)
        if len(i)<longest:
            li[index]=i+(' '*(longest-len(i)))
            
    
    
    for i in range(0,longest):
        print("      "+li[0][i]+" "+li[1][i]+" "+li[2][i]+" "+li[3][i])
    
        

    



































        
        
        
        
        
            
        
        
        
