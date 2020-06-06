bind = "0.0.0.0:8080"

def wsgi_app(environ, start_response):
    body = [bytes(i + '\n', 'ascii') for i in environ['QUERY_STRING'].split('&')]

    status = '200 OK'
    headers = [('Content-Type', 'text/plain')]

    start_response(status, headers)
    return body