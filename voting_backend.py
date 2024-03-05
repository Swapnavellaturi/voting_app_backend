from flask import Flask, request, jsonify
from flask_cors import CORS
import psycopg2
import psycopg2.extras
import os
import logging

app = Flask(__name__)
CORS(app)

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = app.logger

# Use individual environment variables for each component
DB_NAME = os.getenv('DB_NAME', 'database')
DB_USER = os.getenv('DB_USER', 'postgres')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'password')
DB_HOST = os.getenv('DB_HOST', 'databas.us-east-1.rds.amazonaws.com')
DB_PORT = os.getenv('DB_PORT', '5432')

DATABASE_URL = f"dbname='{DB_NAME}' user='{DB_USER}' password='{DB_PASSWORD}' host='{DB_HOST}' port='{DB_PORT}'"

# PostgreSQL default database for initial connection
DEFAULT_DB = 'postgres'

def create_database():
    """Create the target database if it does not already exist."""
    try:
        # Connect to the default database
        conn = psycopg2.connect(dbname=DEFAULT_DB, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT)
        conn.autocommit = True
        cursor = conn.cursor()
        cursor.execute(f"SELECT 1 FROM pg_database WHERE datname='{DB_NAME}'")
        if cursor.fetchone() is None:
            cursor.execute(f"CREATE DATABASE {DB_NAME}")
            logger.info(f"Database {DB_NAME} created successfully.")
        cursor.close()
        conn.close()
    except Exception as e:
        logger.error(f"Failed to create database {DB_NAME}: {e}")

def get_db_connection():
    conn = psycopg2.connect(DATABASE_URL)
    return conn

def initialize_database():
    logger.info('Database initializing')
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS votes (
                id SERIAL PRIMARY KEY,
                option VARCHAR(255) NOT NULL
            );
        ''')
        conn.commit()
        cursor.close()
        conn.close()
        logger.info('Database initialized or already set up.')
    except Exception as e:
        logger.error(f"Error initializing database: {e}")

create_database()
initialize_database()

@app.route('/votes', methods=['GET'])
def get_votes():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cursor.execute('SELECT option, COUNT(*) as votes FROM votes GROUP BY option;')
        votes = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify([{'option': row['option'], 'votes': row['votes']} for row in votes])
    except Exception as e:
        logger.error(f"Error fetching vote counts: {e}")
        return jsonify({'error': 'Error fetching vote counts'}), 500

@app.route('/vote', methods=['POST'])
def cast_vote():
    vote_data = request.json
    if 'option' not in vote_data:
        return jsonify({'error': 'Missing vote option'}), 400
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO votes (option) VALUES (%s)', (vote_data['option'],))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({'success': True, 'message': f"Vote for {vote_data['option']} cast successfully"}), 201
    except Exception as e:
        logger.error(f"Error casting vote: {e}")
        return jsonify({'error': 'Error casting vote'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
