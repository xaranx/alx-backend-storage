--
-- Table structure for `users`
--

CREATE TABLE IF NOT EXISTS users (
	id INTEGER NOT NULL AUTO-INCREMENT,
	email VARCHAR(255) NOT NULL UNIQUE,
	name VARCHAR(255),
	PRIMARY KEY(id)
	);
