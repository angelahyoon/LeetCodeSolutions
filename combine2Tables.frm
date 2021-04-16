# Combine Two Tables MySQL query
SELECT p.FirstName as FirstName, p.LastName as LastName, a.City as City, a.State as State
FROM Person AS p
LEFT JOIN Address AS a
    ON p.PersonId = a.PersonId