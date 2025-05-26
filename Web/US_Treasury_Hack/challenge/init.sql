CREATE USER ctf WITH PASSWORD 'ctfpass';

CREATE DATABASE vulnerable_db
  WITH OWNER = ctf
  ENCODING = 'EUC_TW'
  TEMPLATE = template0
  LC_CTYPE = 'C'
  LC_COLLATE = 'C';

\c vulnerable_db

SET client_encoding = 'BIG5';

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT NOT NULL,
    password TEXT NOT NULL
);

INSERT INTO users (username, password) VALUES
('admin', 'supersecret'),
('guest', 'guest');

CREATE TABLE flags (
    id SERIAL PRIMARY KEY,
    flag TEXT NOT NULL
);

GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO ctf;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO ctf;

INSERT INTO flags (flag) VALUES ('WSUCTF{Next_t1me_use_pr3pared_st4t3ments_plz}');
