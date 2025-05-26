<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>PostgreSQL Injection Challenge</title>
    <style>
        body { font-family: Arial, sans-serif; background: #f0f0f0; padding: 2em; }
        .container { max-width: 600px; margin: auto; background: white; padding: 2em; border-radius: 10px; box-shadow: 0 0 10px rgba(0,0,0,0.1); }
        input[type=text] { width: 80%; padding: 0.5em; margin-bottom: 1em; }
        button { padding: 0.5em 1em; }
        .result { background: #e0ffe0; margin-top: 1em; padding: 1em; border-radius: 5px; }
    </style>
</head>
<body>
<div class="container">
    <h1>Find User Info</h1>
    <p>Try searching for a username:</p>
    <form method="get" action="search.php">
        <input type="text" name="user" placeholder="Enter username..." />
        <button type="submit">Search</button>
    </form>
</div>
</body>
</html>
