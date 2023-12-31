import os, docker, threading
from flask import Flask, request, jsonify
from flask_cors import CORS
from markupsafe import escape

# Flask app
app = Flask(__name__)
CORS(app)

# Docker client
docker_client = docker.from_env()

@app.route("/")
def home():
    response = {"message": "Hello, World!"}
    return jsonify(response), 200

@app.route("/images", methods=["GET"])
def listDockerfile():
    """ API: List all docker images

    Returns:
        response (flask.Response): Response object
    """

    # 1 Query docker images from docker client
    dockerfiles = []
    images = docker_client.images.list()
    for image in images:
        for tag in image.tags:
            dockerfiles.append({
                'id': image.short_id,
                'tag': tag,
                'size': image.attrs['Size'],
                'created': image.attrs['Created'],
            })

    # 2 Return response
    response = {
        "items": dockerfiles,
        "total": len(dockerfiles)
    }
    return jsonify(response), 200

@app.route("/images", methods=["POST"])
def postDockerfile():
    """ API: Create a Docker image through dockerfile

    Returns:
        response (flask.Response): Response object
    """

    # 1 Get request payload
    tag_name = request.form.get('tag_name', None)
    dockerfile = request.files.get('dockerfile', None)  # file

    # 2 Validate payload
    if not dockerfile or not tag_name:
        return { "message": "Missing parameter" }, 400

    tag_name = str(escape(tag_name)).strip()

    # 3 Save file to disk
    path = "../uploaded_dockerfiles"

    # create path to store files if not exist
    if not os.path.exists(path):
        os.makedirs(path)
    dockerfile.save(f"{path}/{tag_name}.Dockerfile")

    # 4 Build docker image in background
    thread = threading.Thread(target=build_docker_image, args=(path, tag_name))
    thread.start()

    # 5 Return response
    response = {
        "id": "-1",
        "message": "Dockerfile accepted"
    }
    return response, 202

def build_docker_image(path, tag_name):
    """ Build docker image

    Args:
        path (str): Path to dockerfile
        tag_name (str): Tag name of docker image
    """

    try:
        image, logs = docker_client.images.build(path=path, tag=tag_name, dockerfile=f"{tag_name}.Dockerfile", rm=True)
        print("Build completed", image, logs)
    except docker.errors.BuildError as e:
        print("Build failed", e)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
