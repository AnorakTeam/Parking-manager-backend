from django.http import HttpResponse


def api_root(request):
    return HttpResponse(
        """
        <html>
            <head><title>Parking Manager API</title></head>
            <body>
                <h1>Parking Manager API</h1>
                <p>Single-user mode (no authentication).</p>
            </body>
        </html>
        """
    )