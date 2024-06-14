-- calculate the weighted average for all students

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
