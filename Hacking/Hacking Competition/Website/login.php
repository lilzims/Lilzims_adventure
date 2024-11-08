<?php
$username = $_POST["username"];
$password = $_POST["password"];
$conn = new mysqli("mysql", "hackuser", "hackpassword", "matrix_db");

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

$sql = "SELECT * FROM users WHERE username='$username' AND password='$password'";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    echo "Access Granted: <br>Flag: cahsi-{admin_access_granted}";
} else {
    echo "Access Denied";
}

$conn->close();
?>
