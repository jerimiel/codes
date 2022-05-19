def arithmetic_arranger(eqtns,x=False):
    
    import numpy as np
    operators=[]
    numbers=[]
    zer=np.zeros((5,6))
    b=''
    
    top1=str('')
    bottom1=str('')
    dash1=str('')
    ans1=str('')
    dash_1=str('')

    if len(eqtns)<6 or x==True:
        for i in eqtns:
                
            plus=len(i.split('+'))
            minus=len(i.split('-'))
            if (plus==1 and minus==1):
                b="Error: Operator must be '+' or '-'."
            elif plus>1:
                operators.append('+')
                numbers.append(i.split('+'))
            elif minus>1:
                operators.append('-')
                numbers.append(i.split('-'))
    #real opetrations
            
    else:
        b="Error: Too many problems."
    for i in numbers:
        try:
            i[0]=int(i[0])
            i[0]=str(i[0])
            i[1]=int(i[1])
            i[1]=str(i[1])
            zer=np.zeros((5,6))
        except:
            pass
        zer=np.zeros((5,6))
        
        if len(i[0])>4 or len(i[1])>4:
            b="Error: Numbers cannot be more than four digits."
            top=''
            bottom=''
            dash=''
            answer=''
            dash_=''

        
        elif len(i[1])>len(i[0]):
            index=numbers.index(i)
            lenny=len(i[1])
            top=str('  ')+str(' ')*(lenny-len(i[0]))+i[0]
            bottom=operators[index]+str(' ')+i[1]
            dash=str('-'*len(bottom))
            tot=top+'\n'+bottom+'\n'+'\n'+dash
            #operation
            try:
                if operators[index]=='-':
                    ans=int(i[0])-int(i[1])
                    ans=str(ans)
                elif operators[index]=='+':
                    ans=int(i[0])+int(i[1])
                    ans=str(ans)
            except:
                b='Error: Numbers must only contain digits.'
                ans=''
            
            if len(ans)<len(dash):
                answer=str(' '*(len(dash)-len(ans)))+ans
                dash_=dash
            elif len(ans)==len(dash):
                answer=ans
                dash_=dash
            elif len(ans)>len(dash):
                dash_=str('-')*len(ans)
                answer=ans
                

            
        elif len(i[0])==len(i[1]):
            index=numbers.index(i)
            top=str('  ')+i[0]
            bottom=operators[index]+str(' ')+i[1]
            dash=str('-'*len(bottom))
            tot=top+'\n'+bottom+'\n'+'\n'+dash
            #operation
            try:
                if operators[index]=='-':
                    ans=int(i[0])-int(i[1])
                    ans=str(ans)
                elif operators[index]=='+':
                    ans=int(i[0])+int(i[1])
                    ans=str(ans)
            except:
                b='Error: Numbers must only contain digits.'
                ans=''
            if len(ans)<len(dash):
                answer=str(' '*(len(dash)-len(ans)))+ans
                dash_=dash
            elif len(ans)==len(dash):
                answer=ans
                dash_=dash
            elif len(ans)>len(dash):
                dash_=str('-')*len(ans)
                answer=ans
                
            
                
            
        else:
            index=numbers.index(i)
            lenny=len(i[0])
            top=str('  ')+i[0]
            bottom=operators[index]+str(' ')+str(' ')*(lenny-len(i[1]))+i[1]
            dash=str('-'*len(bottom))
            tot=top+'\n'+bottom+'\n'+'\n'+dash
            #operation
            try:
                if operators[index]=='-':
                    ans=int(i[0])-int(i[1])
                    ans=str(ans)
                elif operators[index]=='+':
                    ans=int(i[0])+int(i[1])
                    ans=str(ans)
            except:
                b='Error: Numbers must only contain digits.'
            if len(ans)<len(dash):
                answer=str(' '*(len(dash)-len(ans)))+ans
                dash_=dash
            elif len(ans)==len(dash):
                answer=ans
                dash_=dash
            elif len(ans)>len(dash):
                dash_=str('-')*len(ans)
                answer=ans
                
                
            
                
                
            
        top1=top1+"    "+top
        bottom1=bottom1+"    "+bottom
        dash1=dash1+"    "+dash
        ans1=ans1+"    "+answer
        dash_1=dash_1+"    "+dash_
    
    top1=top1[4:]
    bottom1=bottom1[4:]
    dash1=dash1[4:]
    ans1=ans1[4:]
    dash_1=dash_1[4:]
    
    if x==False:
        if b!='':
            a=b
        else:
            a="%s\n%s\n%s"%(top1,bottom1,dash1)
    elif x==True:
        if b!='':
            a=b
        else:
            a="%s\n%s\n%s\n%s"%(top1,bottom1,dash_1,ans1)

    return a
print(arithmetic_arranger(['32 - 698', '1 - 3801', '45 + 43', '123 + 49', '988 + 40']))
