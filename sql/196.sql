--Write a solution to delete all duplicate emails, keeping only one unique email with the smallest id.

DELETE p1
FROM Person p1, Person p2
WHERE p1.id > p2.id 
    AND
    p1.email = p2.email;

-- Input

-- Person =
-- | id | email            |
-- | -- | ---------------- |
-- | 1  | john@example.com |
-- | 2  | bob@example.com  |
-- | 3  | john@example.com |

-- Output

-- | id | email            |
-- | -- | ---------------- |
-- | 1  | john@example.com |
-- | 2  | bob@example.com  |