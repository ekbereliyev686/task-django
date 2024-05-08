from django.shortcuts import render


def index(request):
    answer=''
    context={'data':''}
    if  request.method=='POST':
        first=request.POST['first']
        last=request.POST['last']
        money=request.POST['money']
        if first=='azn' and last=='usd':
            context={
                'data':int(money)*1.7
            }
        else:
            context={
                'data':money
            }

    return render(request,"index.html",context=context)

def test(request):
    
    duzgun=0
    sehf=0
    
    if  request.method=='POST':
        birinci=request.POST['sual1']
        ikinci=request.POST['sual2']
        if birinci=='a':
            duzgun+=1
            
        else:
            sehf+=1
        
        if ikinci=='b':
            duzgun+=1
            
        else:
            sehf+=1
    

    context={
        'duzgun':duzgun,
        'sehf':sehf,
        'bal':duzgun*20
    }
   
    
    return render (request,'test.html',context)
    


def calculator(request):
    context={'cavab':''}
    if request.method=="POST":
       operator=request.POST['operator']
       bir=float(request.POST['bir'])
       iki=float(request.POST['iki'])
        
        
       if operator=='+':
          context={'cavab':bir+iki}
        
       elif operator=='-':
          context={'cavab':bir-iki}
            
       elif operator=='/':
          context={'cavab':bir/iki}
            
       elif operator=='*':
        context={'cavab':bir*iki}
        
    
    return render(request,'calculator.html',context)