from django.http import HttpResponse

def home(request):
    return HttpResponse("""
        <html>
        <head>
            <title>My First Django Application</title>
        </head>
        <body>
            <h1>Welcome to My First Django Application!</h1>
            <h2>Successfully Deployed on Linux Server</h2>
            <p>Powered by Python and Django.</p>
        </body>
        </html>
    """)
