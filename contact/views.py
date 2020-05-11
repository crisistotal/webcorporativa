from django.shortcuts import render,redirect
from django.urls import reverse
from .forms import ContactForm
from django.core.mail import EmailMessage
# Create your views here.
def contact(request):
    contact_form = ContactForm()
    # instanciamos un formluiario y vemos el metodo que nos trae desde el html {{request.post}}
    if request.method == "POST":
        contact_form=ContactForm(data=request.POST) #carga los datos del template con el metodo
        if contact_form.is_valid():
            name = request.POST.get('name','')
            email = request.POST.get('email','')
            content = request.POST.get('content','')
            # Enviamos correo y reedireccionamos
            email = EmailMessage(
                "La Caffettiera: Nuevo mensaje de contacto",
                "De {} <{}>\n\nEscribio:\n\n{}".format(name,email,content),
                "No Responder a este mail",
                ["lucasmontoya15@gmail.com"],
                reply_to=[email]

            )

            try:
                email.send()
                return redirect(reverse('contact')+"?ok")
               
            except :
                return redirect(reverse('contact')+"?fail")
            
    return render(request,'contact/contact.html',{'form':contact_form}) 