from django.shortcuts import render, redirect
import random

# Create your views here.
def index(request):
  #return HttpResponse("Hola, todo bien");
    return render(request, 'index.html');

def procesar(request):
  if 'calculo' in request.session:
    if request.method == "POST":
      
      if request.POST["opcion"] == "farm":
        log = random.randint(10,20)
        request.session['calculo'] += log
        print('calculo')
        request.session['out'].append({"desc": f"has sumado {log} en farm", "color": "text-success"})
        request.session.save()

      if request.POST["opcion"] == "cave":
        log = random.randint(5,10)
        request.session['calculo'] += log

        request.session['out'].append({"desc": f"has sumado {log} en cave", "color": "text-success"})
        request.session.save()

      if request.POST["opcion"] == "house":
        log = random.randint(2,5) 
        request.session['calculo'] += log
        request.session['out'].append({"desc": f"has sumado {log} en home", "color": "text-success"})
        request.session.save()
        
        # request.session['out'].append({"desc": f"has sumado {log} en casino", "color": "text-success"})
        # request.session.save()

      if request.POST["opcion"] == "casino":
        log = random.randint(-50,50)
        request.session['calculo'] += log
        if log > 0:
          request.session['out'].append({"desc": f"has sumado {log} en casino", "color": "text-success"})
          request.session.save()
        else: 
          request.session['out'].append({"desc": f"has perdido {log} en casino", "color": "text-danger"})
          request.session.save()


    # request.session['calculo']=request.session['calculo'] + 5

  else:
    request.session['calculo']= 0
    request.session['out']=[]

  return redirect("/")      
      
def reset(request):
      request.session['calculo']=0
      request.session['out']=[]
      return redirect("/")   
