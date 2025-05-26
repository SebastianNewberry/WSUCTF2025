<?php
$conn = pg_connect("host=localhost dbname=vulnerable_db user=ctf password=ctfpass options='--client_encoding=BIG5'");

pg_query($conn, "SET client_encoding TO 'BIG5';");

if (!$conn) {
    die("Database connection failed.");
}
?>
