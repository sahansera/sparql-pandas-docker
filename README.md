# Dockerizing Pandas and SPARQL

### Introduction
Often times it's a pain in the neck to install a bunch of Python dependencies to get some script running. This Dockerfile is to create an image with a bunch of dependencies using a `requirements.txt` and ultimately create containers out of it.

#### Folder Struture
```
/
├── docker/
│   ├── requirements.txt - Python dependencies to be installed (Pandas has been installed by default)
│   └── Dockerfile
├── scripts/ (this folder is mounted when the container is running; let's you do live changes)
│   ├── run.py - Ideally this could be any script you'll want to run
│   └── 
└── docker-compose.yml
```

### Prerequisites
Download and Install [Docker Desktop](https://www.docker.com/products/docker-desktop)
In addition, you will be needing [Docker Compose](https://docs.docker.com/compose/)

### Running
```
docker-compose up
```

That's it folks!
