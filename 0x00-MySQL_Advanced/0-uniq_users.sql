-- question 0 task create a table
-- column id email name
CREATE TABLE IF NOT EXISTS users(
	ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	email VARCHAR(255) UNIQUE,
	name VARCHAR(255)
	);
