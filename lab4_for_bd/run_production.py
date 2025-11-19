import os
from waitress import serve
from app import create_app
import socket
os.environ["FLASK_ENV"] = "production"

app = create_app()

if __name__ == '__main__':
    hostname = socket.gethostname()
    print("=" * 60)
    print("🚀 Starting Production Server")
    print("=" * 60)
    print(f"Server: http://0.0.0.0:5000")
    print(f"Hostname: {hostname}")
    print()
    print("📚 API Documentation:")
    print("   Swagger UI: http://YOUR_EC2_IP:5000/apidocs/")
    print("   Example: http://13.62.51.37:5000/apidocs/")
    print()
    print("🔍 Health Check:")
    print("   http://YOUR_EC2_IP:5000/health")
    print("   http://YOUR_EC2_IP:5000/")
    print()
    print("⚙️  Server Configuration:")
    print("   Host: 0.0.0.0 (all interfaces)")
    print("   Port: 5000")
    print("   Threads: 4")
    print("=" * 60)
    print("✅ Server is ready to accept connections!")
    print("=" * 60)
    
    serve(app, host='0.0.0.0', port=5000, threads=4)
