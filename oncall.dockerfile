FROM ubuntu:focal

ENV DEBIAN_FRONTEND noninteractive

RUN --mount=target=/var/lib/apt/lists,type=cache,sharing=locked \
    --mount=target=/var/cache/apt,type=cache,sharing=locked \
    apt-get update && apt-get install -y \
    libsasl2-dev python3-dev libldap2-dev libssl-dev python3-pip python-setuptools git

WORKDIR /opt

RUN git clone https://github.com/linkedin/oncall.git && \
    cd oncall && \
    python3 setup.py develop && \
    pip3 install -e '.[dev]'

COPY config.yaml /opt/oncall/configs/config.yaml

ENTRYPOINT [ "/usr/local/bin/oncall-dev", "/opt/oncall/configs/config.yaml" ]