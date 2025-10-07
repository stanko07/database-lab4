from waitress import serve
from app import create_app

app = create_app()

if __name__ == '__main__':
    print("Starting production server on http://0.0.0.0:5000")
    print("Swagger UI available at http://YOUR_IP:5000/apidocs/")
    serve(app, host='0.0.0.0', port=5000, threads=4)
