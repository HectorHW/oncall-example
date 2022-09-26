FROM ubuntu:focal

ENV DEBIAN_FRONTEND noninteractive

RUN --mount=target=/var/lib/apt/lists,type=cache,sharing=locked \
    --mount=target=/var/cache/apt,type=cache,sharing=locked \
    apt update && apt install -y git mysql-client

WORKDIR /opt

RUN git clone -n https://github.com/linkedin/oncall.git --depth 1 && \
    cd oncall && \
    git checkout HEAD db/schema.v0.sql

WORKDIR /opt/oncall
COPY run_migrations.sh .

ENTRYPOINT ["./run_migrations.sh"]   