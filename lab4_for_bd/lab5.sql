USE new_company;

DROP TRIGGER IF EXISTS projects_update;
DROP TRIGGER IF EXISTS projects_delete;
DROP TRIGGER IF EXISTS contact_person_name;


DELIMITER //
CREATE TRIGGER projects_update
BEFORE UPDATE ON projects
FOR EACH ROW
BEGIN
    SIGNAL SQLSTATE '45000'
    SET MESSAGE_TEXT = 'Оновлення даних у таблиці projects заборонено.';
END;
//
DELIMITER ;

DELIMITER //
CREATE TRIGGER projects_delete
BEFORE DELETE ON projects
FOR EACH ROW
BEGIN
    SIGNAL SQLSTATE '45000'
    SET MESSAGE_TEXT = 'Видалення рядків з таблиці projects заборонено.';
END;
//
DELIMITER ;


DELIMITER //
CREATE TRIGGER contact_person_name
BEFORE INSERT ON contact_person
FOR EACH ROW
BEGIN
    IF NEW.name NOT IN ('Svitlana', 'Petro', 'Olha', 'Taras') THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Недопустиме ім`я. Дозволені лише: Svitlana, Petro, Olha, Taras.';
    END IF;
END;
//
DELIMITER ;
