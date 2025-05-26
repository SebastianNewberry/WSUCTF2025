#!/bin/bash

set -e

# Initialize database if not already initialized
if [ ! -s "$PGDATA/PG_VERSION" ]; then
  echo "Initializing PostgreSQL..."
  su postgres -c "/usr/lib/postgresql/17/bin/initdb -D $PGDATA"
fi

echo "Starting PostgreSQL..."
su postgres -c "/usr/lib/postgresql/17/bin/pg_ctl -D $PGDATA -l /var/log/postgresql.log start"

# Wait for PostgreSQL to start
echo "Waiting for PostgreSQL..."
until su postgres -c "/usr/lib/postgresql/17/bin/pg_isready -q"; do
  echo "Still waiting..."
  sleep 1
done

# Run init SQL if it exists
if [ -f /init.sql ]; then
  echo "Running init.sql..."
  su postgres -c "psql -U postgres -f /init.sql"
fi

# Start Apache in foreground
echo "Starting Apache..."
apachectl -D FOREGROUND
