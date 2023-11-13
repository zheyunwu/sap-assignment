# SAP Assignment

This project contains two parts:

- A frontend Web App for users to list Docker images and build Docker images by uploading *Dockerfile*
- A backend App to serve RESTful APIs

![Architecture](./architecture.png)

## Directory Structure

    .
    ├── README.md
    ├── backend                  # Backend code
    │   ├── app.py               # Flask app
    │   ├── test_app.py          # Unit tests
    │   └── requirements.txt     # Python dependencies list
    ├── frontend                 # Frontend code
    │   └── ...
    ├─ uploaded_dockerfiles      # Directory to store files uploaded by users
    │   └── ...
    └─── helloworld.dockerfile   # A Dockerfile for testing

## Backend

The backend is built on top of [Flask](https://flask.palletsprojects.com/en/3.0.x/) - a web framework based on Python.

Backend API endpoints:

| Method   | URL                                | Description                                  | Request Payload Example                  |
| -------- | ---------------------------------- | -------------------------------------------- | ---------------------------------------- |
| `GET`    | `/`                                | Just for health check.                       |                                          |
| `GET`    | `/api/images`                      | Retrieve all images.                         |                                          |
| `POST`   | `/api/images`                      | Create a new image by uploading a Dockerfile.| {"tag_name": "image:latest", "dockerfile": file} |

### Backend - Prerequisites

- Docker Engine
- Python >= 3.8

### Backend - Getting started

1. Create a Python virtual environment (for the first time):

    ```sh
    cd backend
    python3 -m venv venv
    ```

2. Enter Python virtual environment:

    ```sh
    cd backend
    source venv/bin/activate
    ```

3. Install dependencies:

    ```sh
    pip install -r requirements.txt
    ```

4. Start in development mode:

    ```sh
    python app.py
    ```

### Backend - Unit Tests

1. Enter Python virtual environment:

    ```sh
    cd backend
    source venv/bin/activate
    ```

2. Run test:

    ```sh
    python -m pytest test_app.py
    ```

## Frontend

The frontend is built on top of [react-admin](https://github.com/marmelab/react-admin) - an open source framework for creating B2B apps based on [React](https://react.dev/).

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
