def importe_total_carro(request):
    total=0  
    session= request.session['carro'] 
    if request.user.is_authenticated:
       for key, value in session.items():
           total=total+(float(value["precio"])* value["cantidad"])
        
    return {"importe_total_carro":total}