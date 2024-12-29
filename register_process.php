<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $username = $_POST['username'];
    $email = $_POST['email'];
    $password = $_POST['password'];
    $confirm_password = $_POST['confirm_password'];

    // Vérifiez si les mots de passe correspondent
    if ($password !== $confirm_password) {
        die("Les mots de passe ne correspondent pas.");
    }

    // Hash du mot de passe
    $hashed_password = password_hash($password, PASSWORD_DEFAULT);

    // Connexion à la base de données
    $conn = new mysqli("localhost", "root", "", "ppw");

    // Vérifiez la connexion
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }

    // Insérez l'utilisateur dans la base de données
    $sql = "INSERT INTO users (username, email, password) VALUES ('$username', '$email', '$hashed_password')";

    if ($conn->query($sql) === TRUE) {
        echo "Inscription réussie. Vous pouvez maintenant vous <a href='login.html'>connecter</a>.";
    } else {
        echo "Erreur: " . $sql . "<br>" . $conn->error;
    }

    $conn->close();
}
?>
