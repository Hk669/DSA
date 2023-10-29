-- Table Salary
-- +-------------+----------+
-- | Column Name | Type     |
-- +-------------+----------+
-- | id          | int      |
-- | name        | varchar  |
-- | sex         | ENUM     /
-- | salary      | int      |
-- +-------------+----------+
-- id is the primary key (column with unique values) for this table.
-- The sex column is ENUM (category) value of type ('m', 'f').
-- The table contains information about an employee.

-- Write a solution to swap all 'f' and 'm' values (i.e., change all 'f' values to 'm' and vice versa) 
-- with a single update statement and no intermediate temporary tables.

UPDATE Salary
SET sex = CASE
    WHEN sex = 'f' THEN 'm'
    WHEN sex = 'm' THEN 'f'
    ELSE sex
END;