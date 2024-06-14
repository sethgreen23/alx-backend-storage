-- calculate the weighted average for all students

-- Write a SQL script that creates a stored procedure 
-- ComputeAverageWeightedScoreForUser that computes and
-- store the average weighted score for a student.

-- Computes and store the average score for a student

DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUser
(IN user_id INT)
BEGIN
	-- declare variables
	DECLARE weighted_average FLOAT DEFAULT 0;
	DECLARE hole_score INT DEFAULT 0;
	DECLARE sum_weights INT DEFAULT 0;

	-- compute weighted average
	SELECT SUM(projects.weight * corrections.score) INTO hole_score 
	FROM projects INNER JOIN corrections 
	WHERE projects.id = corrections.project_id 
	AND corrections.user_id = user_id;
	
	-- compute sum of weights
	SELECT SUM(projects.weight) INTO sum_weights 
	FROM projects INNER JOIN corrections 
	WHERE projects.id = corrections.project_id 
	AND corrections.user_id = user_id;
	
	-- compute weighted average
	IF sum_weights  = 0 THEN
		SET weighted_average = 0;
	ELSE
		SET weighted_average = hole_score / sum_weights;
	END IF;

	-- update table
	UPDATE users 
	SET average_score = weighted_average
	WHERE users.id = user_id;
END $$
DELIMITER ;



DELIMITER $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
	DECLARE done INT DEFAULT FALSE;
	DECLARE student_id INT;
	DECLARE cur CURSOR FOR SELECT id FROM users;
	DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

	OPEN cur;

	REPEAT 
		FETCH cur INTO student_id;
		CALL ComputeAverageWeightedScoreForUser(student_id);
	UNTIL done END REPEAT;
	CLOSE cur;
END$$

DELIMITER ;
