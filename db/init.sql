CREATE TABLE IF NOT EXISTS items (
  id INT AUTO_INCREMENT PRIMARY KEY,
  description VARCHAR(255)
);

INSERT INTO items (description) VALUES
('Práctica 1. Fecha de entrega: 22/03. Estado: Entregada'),
('Práctica 2. Fecha de entrega: 29/03. Estado: Entregada');

CREATE TABLE IF NOT EXISTS members (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100),
  initials CHAR(3)
);

INSERT INTO members (name, initials) VALUES
('Ezequiel Bengoechea', 'EB'),
('Gustavo Inturias',    'GI'),
('Jesica Maero',        'JM'),
('Ulises Serri',        'US');
