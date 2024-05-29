-- Active: 1715043174887@@127.0.0.1@3306@
DROP DATABASE IF EXISTS ganaderia_db;

CREATE DATABASE ganaderia_db DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

USE ganaderia_db;

CREATE TABLE permissions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    UNIQUE KEY (name)
);

INSERT INTO permissions (name)
 VALUES 
 ('admin'),
  ('trabajador')

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    name VARCHAR(255),
    last_name VARCHAR(255),
    password VARCHAR(255),
    email VARCHAR(255),
    permissions_id INT NOT NULL,
    UNIQUE KEY (email),
    FOREIGN KEY (permissions_id) REFERENCES permissions (id)
);

CREATE TABLE TrabajadorNomina(
    id INT AUTO_INCREMENT PRIMARY KEY,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    user_id INT NOT NULL,
    nomina DECIMAL(10,2),
    otros_gastos DECIMAL(10,2),
    total_nomina DECIMAL(10,2),
    FOREIGN KEY (user_id) REFERENCES users (id)
);

CREATE TABLE TrabajadorTareasRealizar(
    id INT AUTO_INCREMENT PRIMARY KEY,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    user_id INT NOT NULL,
    tareas_realizar VARCHAR(255),
    status ENUM('pendiente', 'realizada', 'cancelada') DEFAULT 'pendiente',
    FOREIGN KEY (user_id) REFERENCES users (id)
);

CREATE TABLE TrabajadorHorasTrabajadas(
    id INT AUTO_INCREMENT PRIMARY KEY,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    user_id INT NOT NULL,
    horas_trabajadas INT NOT NULL,
    dias_trabajados VARCHAR(255),
    FOREIGN KEY (user_id) REFERENCES users (id)
);


DROP TABLE IF EXISTS TrabajadorAsistencia;
CREATE TABLE TrabajadorAsistencia(
    id INT AUTO_INCREMENT PRIMARY KEY,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    user_id INT NOT NULL,
    asistencia ENUM('si', 'no') NOT NULL DEFAULT 'si',
    FOREIGN KEY (user_id) REFERENCES users (id)
);

