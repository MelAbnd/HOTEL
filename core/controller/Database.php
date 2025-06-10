<?php

class Database {
    private $user = "root";        // Usuario de la base de datos
    private $pass = "";            // Contraseña de la base de datos
    private $host = "localhost";   // Servidor de la base de datos
    private $ddbb = "hotel_s1"; // Nombre de la base de datos

    public static $db;
    public static $con;

    // Constructor
    function __construct() {
        // Inicialización, ya no es necesario hacer nada aquí para la conexión
    }

    // Método para conectar usando MySQLi
    function connect() {
        // Intentamos establecer la conexión con la base de datos
        $con = new mysqli($this->host, $this->user, $this->pass, $this->ddbb);

        // Verificar si ocurrió un error en la conexión
        if ($con->connect_error) {
            die("Connection failed: " . $con->connect_error);
        }

        // Desactivar el modo SQL para evitar problemas con las consultas
        $con->query("SET sql_mode=''");
        return $con;
    }

    // Método para conectar usando PDO
    function connect1() {
        try {
            // Usamos PDO para la conexión
            $db = new PDO("mysql:host=$this->host;dbname=$this->ddbb", $this->user, $this->pass);
            // Configuramos la codificación
            $db->exec("SET NAMES utf8");
            return $db;
        } catch (PDOException $e) {
            // Capturamos cualquier excepción de PDO
            echo "Connection failed: " . $e->getMessage();
        }
    }

    // Método estático para obtener la conexión
    public static function getCon() {
        if (self::$con == null && self::$db == null) {
            self::$db = new Database();
            self::$con = self::$db->connect(); // Usamos MySQLi aquí, puedes cambiar a PDO si prefieres
        }
        return self::$con;
    }
}

?>
