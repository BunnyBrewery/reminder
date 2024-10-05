#!/bin/bash

# docker run --name reminder-fastapi -d  remider_fastapi_image

docker run -d \
  --name reminder-fastapi \
  --network reminder_network \
  remider_fastapi_image
