FROM debian:bullseye

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        mariadb-server \
        mariadb-client \
        supervisor \
        gcc \
        libc-dev \
        default-libmysqlclient-dev \
    && rm -rf /var/lib/apt/lists/*

RUN apt-get update && \
    apt-get install -y curl gnupg && \
    curl -sL https://deb.nodesource.com/setup_21.x | bash - && \
    apt-get install -y nodejs

RUN npm install -g npm@latest

WORKDIR /app

COPY package.json package-lock.json /app/
RUN npm install

COPY src/ /app/src/

EXPOSE 3000

COPY --chown=root entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]

