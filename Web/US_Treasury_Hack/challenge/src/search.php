<?php
include 'db.php';

if (isset($_GET['user'])) {
    $raw_input = $_GET['user'];

    echo "<p><strong>Raw input (printable):</strong> " . htmlentities($raw_input) . "</p>";

    $user = pg_escape_string($raw_input);
    $query = "SELECT * FROM users WHERE username = '$user'\n";
    $result = pg_query($conn, $query);

    echo "<div class='container'>";
    echo "<h2>Results for input: '" . htmlentities($raw_input) . "'</h2>";
    echo "<p><strong>Final query:</strong> " . htmlentities($query) . "</p>";

    if (strpos($user, "'") !== false && $raw_input === $user) {
        echo "<p><strong>Bypass detected — attempting to retrieve flag!</strong></p>";

        $flag_result = pg_query($conn, "SELECT flag FROM flags LIMIT 1");
        if ($flag_result && pg_num_rows($flag_result) > 0) {
            $flag_row = pg_fetch_assoc($flag_result);
            echo "<p><strong>Flag:</strong> " . htmlentities($flag_row['flag']) . "</p>";
        } else {
            echo "<p><strong>Error retrieving flag. Please contact an admin.</strong></p>";
        }
    }

    echo "<p><strong>Query Result Rows:</strong> " . pg_num_rows($result) . "</p>";

    if ($result) {
        while ($row = pg_fetch_assoc($result)) {
            echo "<div class='result'>";
            echo "<strong>User:</strong> " . htmlentities($row['username']) . "<br>";
            echo "<strong>Password:</strong> " . htmlentities($row['password']);
            echo "</div>";
        }
    } else {
        $error = pg_last_error($conn);
        echo "<p><strong>Database Error:</strong> " . htmlentities($error) . "</p>";
    }

    echo "<p><a href='index.php'>Back</a></p></div>";
}
?>