# Flask Voting Application Backend

A simple, Flask-based backend for a voting application that demonstrates basic CRUD operations with a PostgreSQL database. It supports casting votes and viewing vote counts, serving as the backend for a corresponding frontend voting interface.

## Getting Started

These instructions will help you get the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.6 or higher
- pip and virtualenv
- An Ubuntu server (e.g., AWS EC2 instance)

### Installation

Follow these steps to set up your development environment:

1. **Clone the Repository**

    Clone this repository to your local machine or server:

    ```bash
    git clone https://github.com/Swapnavellaturi/voting_app_backend.git
    ```

2. **Navigate to the Cloned Directory**

    Change your current directory to the cloned repository:

    ```bash
    cd voting_app_backend
    ```

3. **Export Environment Variables**

    Set the necessary environment variables for your PostgreSQL database connection. Replace the placeholder values with your actual database configuration:

    ```bash
    export DB_NAME='your_database_name'
    export DB_USER='your_database_user'
    export DB_PASSWORD='your_database_password'
    export DB_HOST='your_database_host'
    export DB_PORT='5432'
    ```

4. **Run the Setup Script**

    Execute the `setup_and_run.sh` script to install dependencies, set up the environment, and start the Flask application:

    ```bash
    chmod +x setup_and_run.sh
    ./setup_and_run.sh
    ```

    The Flask application will now be running and accessible at `http://your_server_ip:5000`.

### Usage

- **Casting a Vote:** To cast a vote, send a POST request to `/vote` with a JSON payload specifying the `option`.
- **Viewing Vote Counts:** Retrieve the current vote counts by sending a GET request to `/votes`.

## Deployment

For production environments, it is recommended to serve the Flask application using a more robust WSGI server like Gunicorn and to place it behind a reverse proxy such as Nginx. This setup helps manage load, security, and other concerns more effectively than the built-in Flask server.

### Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.
