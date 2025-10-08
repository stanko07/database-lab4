from flask import Blueprint, jsonify
from datetime import datetime

health_bp = Blueprint('health', __name__)


@health_bp.route('/health', methods=['GET'])
def health_check():
    """
    Health check endpoint
    ---
    tags:
      - Health
    responses:
      200:
        description: Server is running
        schema:
          type: object
          properties:
            status:
              type: string
              example: healthy
            timestamp:
              type: string
              example: "2025-10-08T19:30:00"
            message:
              type: string
              example: Server is running successfully
    """
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'message': 'Server is running successfully'
    }), 200


@health_bp.route('/', methods=['GET'])
def root():
    """
    Root endpoint
    ---
    tags:
      - Health
    responses:
      200:
        description: Welcome message
        schema:
          type: object
          properties:
            message:
              type: string
              example: Welcome to Flask API
            swagger_url:
              type: string
              example: /apidocs/
    """
    return jsonify({
        'message': 'Welcome to Flask API',
        'swagger_url': '/apidocs/',
        'health_check': '/health'
    }), 200
