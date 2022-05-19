class Hat():
    
    def __init__(self,**kwargs):
        import copy
        self.hat={}
        self.contents=[]
        self.kwargs=kwargs
        self.emp=[]
        for i,j in self.kwargs.items():
            self.hat[i] = j
            for k in range(0,j):
                self.contents.append(i)
        self.deep=copy.deepcopy(self.contents)

    def draw(self,no_balls):
        
        import random
        random.seed=95
        import copy
        draw=[]
        if no_balls<=len(self.deep):
            draw=random.sample(self.deep,no_balls)
            for i in draw: 
                self.contents.remove(i)
        else:
            draw=self.deep   
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
        hat.contents=hat.contents+li 
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
print(len(hat.contents))
probability = experiment(hat=hat, expected_balls={"blue":2,"green":1}, num_balls_drawn=4, num_experiments=1000)
print(len(hat.contents))
actual = probability
expected = 0.272
print(actual)
    
            
        
        
        
        
        

    
        

    

    




    



    

        

        
