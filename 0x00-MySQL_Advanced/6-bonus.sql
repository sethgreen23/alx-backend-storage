-- add a new correction for a student

DELIMITER $$
CREATE PROCEDURE AddBonus
(IN user_id INT, IN project_name VARCHAR(255), IN score INT)
BEGIN
DECLARE project_count INT;

SELECT COUNT(*) INTO project_count
FROM projects
WHERE name = project_name;
IF project_count < 1 THEN
	INSERT INTO projects (name) VALUES (project_name);
END IF;
INSERT INTO corrections(user_id, project_id, score) VALUES (user_id, (SELECT id FROM projects WHERE name = project_name), score);
END $$
DELIMITER ;
