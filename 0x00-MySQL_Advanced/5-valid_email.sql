-- Write a SQL script that creates a trigger that resets
-- the attribute valid_email only when the email has been changed.
-- Context: Nothing related to MySQL, but perfect for user email
-- validation - distribute the logic to the database itself!
DELIMETER $$
CREATE TRIGGER reset_attribute_valide_email
AFTER UPDATE ON users
FOR EACH ROW
BEGIN 
    IF OLD.email <> NEW.email THEN
        SET NEW.valid_email = 0;
    END IF;
END;
$$
DELIMETER ;