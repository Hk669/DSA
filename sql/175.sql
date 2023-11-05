--Write a solution to report the first name, last name, city, and state of each person in the Person table.
-- If the address of a personId is not present in the Address table, report null instead.


SELECT firstName, lastName, city, state
FROM Person p
LEFT JOIN Address a ON
        p.personId = a.personId;


-- Input
-- Person =
-- | personId | lastName | firstName |
-- | -------- | -------- | --------- |
-- | 1        | Wang     | Allen     |
-- | 2        | Alice    | Bob       |

-- Address =
-- | addressId | personId | city          | state      |
-- | --------- | -------- | ------------- | ---------- |
-- | 1         | 2        | New York City | New York   |
-- | 2         | 3        | Leetcode      | California |

-- Output
-- | firstName | lastName | city          | state    |
-- | --------- | -------- | ------------- | -------- |
-- | Allen     | Wang     | null          | null     |
-- | Bob       | Alice    | New York City | New York |