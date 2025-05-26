FROM ubuntu:22.04

RUN apt-get update && \
    apt-get install -y socat && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

RUN useradd -m -s /bin/bash ctfuser

RUN mkdir -p /srv/app /srv/flag

COPY vuln /srv/app/run
COPY flag.txt /srv/flag/flag.txt

RUN chmod 755 /srv/app/run && \
    chmod 444 /srv/flag/flag.txt && \
    chown root:root /srv/app/run /srv/flag/flag.txt

USER ctfuser


EXPOSE 1337


CMD ["socat", "TCP-LISTEN:1337,reuseaddr,fork", "EXEC:/srv/app/run,stderr"]
