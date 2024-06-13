-- create trigger that reset the attribute valid_email only whe the email has changed

DELIMITER $$

CREATE TRIGGER reset_valid_email
AFTER UPDATE ON users
FOR EACH ROW
BEGIN
	IF NEW.email <> OLD.email THEN
		UPDATE users
		SET valid_email = 0
		WHERE email = NEW.email;
	END IF;
END $$
DELIMITER ;
