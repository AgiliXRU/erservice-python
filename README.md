## How to run server

### Install deps *nix
```shell
virtualenv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

### Run fake server
```shell
./start_fake
```

### Run service
```shell
./start
```

### Install deps Windows
```shell
python3 -m venv venv
source venv\Scripts\activate.bat
pip3 install -r requirements.txt
```

### Run fake server
```shell
start_fake.bat
```

### Run service
```shell
start.bat
```

### Run via docker
```shell
docker build -t er-server .
docker run -v "$(pwd):/usr/src/app" -p8000:8000 -it er-server /bin/bash
```


You can see [Tasks.md](/Tasks.md) for further instructions
