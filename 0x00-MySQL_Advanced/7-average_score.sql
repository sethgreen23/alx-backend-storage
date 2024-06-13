-- Computes and store the average score for a student

DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser
(IN user_id INT)
BEGIN
	DECLARE average FLOAT;
	SET average = (SELECT SUM(score) / COUNT(*) FROM corrections WHERE user_id = user_id);
	UPDATE users SET average_score = average WHERE id = user_id;
END $$
DELIMITER ;
