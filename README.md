# SAP Assignment

This project contains source code of a RESTful service and a simple Web for users to upload *Dockerfile*. It includes two parts:

- `backend/` - A Flask App to serve RESTful APIs.
- `frontend/` - A React Web App for users to interact with.

## Directory Structure

    .
    ├── README.md
    ├── backend                 # Backend code
    │   ├── app.py              # Flask app
    │   └── requirements.txt    # Python dependencie list
    ├── frontend                # Frontend code
    │   └── ...
    ├── helloworld.dockerfile   # Dockerfile for testing
    └── uploaded_dockerfiles    # Directory to store files uploaded by users

## Backend

The backend is built on top of [Flask](https://flask.palletsprojects.com/en/3.0.x/) - a web framework written in Python

### Backend - Prerequisites

- Docker Enginer
- Python >= 3.8

### Backend - Getting started

1. Create a Python virtual environment:

    ```sh
    cd backend
    python3 -m venv venv
    source venv/bin/activate
    ```

2. Install dependencies:

    ```sh
    pip3 install -r requirements.txt
    ```

3. Start in development mode:

    ```sh
    python3 app.py
    ```

## Frontend

The frontend is built on top of [react-admin](https://github.com/marmelab/react-admin) - a [React](https://react.dev/)-based open source admin framework

### Frontend - Prerequisites

- Node.js >= 18.16

### Frontend - Getting started

1. Install dependencies:

    ```sh
    cd frontend
    npm install
    ```

2. Start in development mode:

    ```sh
    npm run dev
    ```

3. Build for production:

    ```sh
    npm run build
    ```
