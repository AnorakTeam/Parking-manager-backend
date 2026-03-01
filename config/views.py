from django.http import HttpResponse

def api_root(request):
    return HttpResponse(
        """
        <html>
            <head>
                <title>Parking Manager API</title>
            </head>
            <body>
                <h1>Parking Manager API</h1>
                <p>And... Hello world, sure.</p>
            </body>
        </html>
        """
    )