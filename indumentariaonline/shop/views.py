from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

def index(request):
    html = """
    <html>
        <head>
            <title>Indumentaria Online</title>
        </head>
        <body>
            <h1>¡Bienvenido a nuestro Sitio!</h1>
            <a href="contacto">Ir a contacto</a>

        </body>
    </html>
    """
    return HttpResponse(html)

def contacto(request):
    html = """
        <html>
            <head>
                <title>Indumentaria Online</title>
            </head>
            <body>
                <h2>Contacto</h2>
                <p><strong>Nombre: </strong>Indumentaria Online</p>
                <p><strong>Dirección: </strong>Pasteur 544</p>
                <p><strong>Ciudad: </strong>Departamento 2</p>
            </body>
        </html>
        """
    return HttpResponse(html)

def index_2(request):
    return render(request, "shop/index.html")

def contacto_2(request):
    ctx = {
        "nombre":"Indumentaria Online",
        "direccion":"Pasteur 544",
        "ciudad":"Villa Maria"
    }
    return render(request, "shop/contacto.html", ctx)
