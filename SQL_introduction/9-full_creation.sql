-- creating a table and inserting rows to it
CREATE TABLE IF NOT EXISTS second (
  id INT,
  name VARCHAR(256),
  score INT
);
INSERT INTO second (id, name, score)
VALUES
	(1, 'John', 10),
    (2, 'Alex', 3),
    (3, 'Bob', 14),
    (4, 'George', 8);