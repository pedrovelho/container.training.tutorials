# Use a full image version
FROM python:3.9.2-slim as base

# Create a builder container
FROM base as builder

# System deps:
RUN apt-get update && apt-get install -y python3-dev python3-pip
RUN pip3 install --prefix=/runtime --force-reinstall redis flask pytest

# Use the base container and only copy the runtime + the app
FROM base as runtime
COPY --from=builder /runtime /usr/local
COPY ./main.py /app/
COPY keystore_rest_server /app/keystore_rest_server/

WORKDIR /app

# Set env and metadata
EXPOSE 5000
MAINTAINER pedro.velho@ryax.tech

CMD python3 ./main.py