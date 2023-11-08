import os, docker
from flask import Flask, request, jsonify
from flask_cors import CORS
from markupsafe import escape

app = Flask(__name__)
CORS(app)

# Docker client
client = docker.from_env()

@app.route("/")
def home():
    response = {"message": "Hello, World!"}
    return jsonify(response), 200

@app.route("/dockerfiles", methods=["GET"])
def listDockerfile():
    # get docker images from docker client
    dockerfiles = []
    images = client.images.list()
    for image in images:
        print(image)
        dockerfiles.append({
            'id': image.id,
            'tags': image.tags,
            'size': image.attrs['Size'],
            'created': image.attrs['Created'],
        })

    response = {
        "items": dockerfiles,
        "total": len(dockerfiles)
    }
    return jsonify(response), 200

@app.route("/dockerfiles", methods=["POST"])
def postDockerfile():

    # Get request payload
    tag_name = request.form.get('tag_name', None)
    dockerfile = request.files.get('dockerfile', None)  # file

    # Validate input
    if not dockerfile or not tag_name:
        return { "message": "Missing parameter" }, 400
    
    tag_name = str(escape(tag_name)).strip()

    # create path to store files if not exist
    # the path to store files
    path = "./uploaded_dockerfiles"
    if not os.path.exists(path):
        os.makedirs(path)

    # save file
    dockerfile.save(f"{path}/{tag_name}.Dockerfile")
    item = {
        "id": "1",
        "tag_name": tag_name
    }

    return item, 202



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)