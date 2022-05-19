class Hat():

    def __init__(self,**kwargs):
        self.hat={}
        self.contents=[]
        self.kwargs=kwargs
        self.emp=[]
        for i,j in self.kwargs.items():
            self.hat[i] = j
            for k in range(0,j):
                self.contents.append(i)

    def draw(self,no_balls):
        import random
        if no_balls > (len(self.contents)+len(self.emp)) :
            draw=self.contents
        elif no_balls > len(self.contents) and no_balls < (len(self.contents)+len(self.emp)):
            for i in self.emp:
                self.contents.append(i)
            self.emp=[]
            draw=random.sample(self.contents,no_balls)
        elif no_balls <= len(self.contents):
            draw=random.sample(self.contents,no_balls)
            for i in draw:
                self.emp.append(i)
                self.contents.remove(i)
        return draw


#####################
# experiment function
#hat,expected_balls,num_balls_drawn,num_experiments

def experiment(**kwargs):
    exp={}
    for i,j in kwargs.items():
        exp[i]=j
        
    expected_balls=exp['expected_balls']
    key=expected_balls.keys()
    prob=0
    
    num_experiments=exp['num_experiments']
    hat=exp['hat']
    num_balls_drawn=exp['num_balls_drawn']
        
    for i in range(0,num_experiments):
        truth_teller=[]
        li=hat.draw(num_balls_drawn)
        for i in key:
            if li.count(i)>=expected_balls[i]:
                truth_teller.append(True)
            else:
                truth_teller.append(False)
        if truth_teller.count(False)==0:
            prob=prob+1
    ans=prob/num_experiments

    return ans

hat = Hat(blue=3,red=2,green=6)
probability = experiment(hat=hat, expected_balls={"blue":2,"green":1}, num_balls_drawn=4, num_experiments=1000)
actual = probability
expected = 0.272
print(actual)

    
            
        
        
        
        
        

    
        

    

    




    



    

        

        
