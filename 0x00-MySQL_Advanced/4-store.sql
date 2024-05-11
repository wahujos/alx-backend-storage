-- Write a SQL script that creates a trigger that decreases
-- the quantity of an item after adding a new order.
-- Quantity in the table items can be negative.
DELIMETER $$
CREATE TRIGGER decreases_the_quantity_of_item
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE items
    SET quantity = quantity - NEW.quantity_ordered
    WHERE item.id = NEW.item.id
END
$$
DELIMETER ;
