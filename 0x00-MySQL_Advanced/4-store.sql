-- Write a SQL script that creates a trigger that decreases
-- the quantity of an item after adding a new order.
-- Quantity in the table items can be negative.
DELIMITER //
CREATE TRIGGER decrease_quantity_after_order
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE items
    SET quantity = quantity - NEW.number
    WHERE item_id = NEW.item_id;
END;
//
DELIMITER ;
