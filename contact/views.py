from django.shortcuts import redirect, render, HttpResponse
from .forms import ContactForm
from django.urls import reverse
from django.core.mail import EmailMessage
# Create your views here.


def contacto(request):
    #print(f"Tipo de peticion : {request.method}")
    contact_Form = ContactForm()
    #mensaje = "Su formulario fue enviado correctamente"
    if request.method == "POST":
        contact_Form = ContactForm(data=request.POST)
        if contact_Form.is_valid:
            name = request.POST.get("name", "")
            email = request.POST.get("email", "")
            content = request.POST.get("content", "")
            email = EmailMessage(
                "La Caffetiera de Ricardo: Nuevo mensaje",
                "De {} <{}> \n\n Escribió:\n\n{}".format(name, email, content),
                "no-contestar@inbox.mailtrap.io",
                ["dasilvaricardog@gmail.com"],
                reply_to=[email]

            )
            # return render(request, 'contact/enviado.html', {'mensaje': mensaje, 'form': ContactForm()})
            # SUponiendo que todo ha salido OK, utilizamos REverse para que sea el mismo Django que se encarge de redireccionarme las URLS
            # enviamos el correo y redireccionamos
            try:
                email.send()
                # Todo ha ido bien
                return redirect(reverse('contact') + "?ok")
            except:
                # ha ocurrido un problema
                return redirect(reverse('contact') + "?Fail")

    return render(request, 'contact/contact.html', {'form': contact_Form})
