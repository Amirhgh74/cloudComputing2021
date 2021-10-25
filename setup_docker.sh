#!/bin/bash

sudo docker build -t python_client .

xhost +local:root
sudo docker run -it \
		--env="DISPLAY"\
		--env="QT_X11_NO_MITSHM=1"\
		--volume="/tmp/.X11-unix:/tmp/.X11-unix:rw"\
    		-v ~/.aws/credentials:/root/.aws/credentials:ro \
    		python_client
    		
xhost -local:root
