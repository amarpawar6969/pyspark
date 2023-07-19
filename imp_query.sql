SET SERVEROUTPUT ON;

DECLARE
    MY_NAME VARCHAR(50) := '&ENTER_NAME';
    A NUMBER;
BEGIN
    SELECT 
        INSTR(MY_NAME, ' ') INTO A
    FROM DUAL;
    
    dbms_output.put_line('SPACE AT:' || A);
END;

-- =============================================================================

WITH A AS
(SELECT 'AMAR RAVINDRA PAWAR' AS NNAME FROM DUAL)

SELECT 
    SUBSTR(NNAME,1, INSTR(NNAME,' ')-1) AS F_NAME,
    SUBSTR(NNAME,INSTR(NNAME,' ')+1, (LENGTH(SUBSTR(NNAME,INSTR(NNAME,' ')))- LENGTH(SUBSTR(NNAME,INSTR(NNAME,' ',1,2))))) AS M_NAME,
    SUBSTR(NNAME,INSTR(NNAME,' ',1,2)+1) AS L_NAME
FROM A;


-- =============================================================================

WITH A AS
(SELECT 'AMAR PAWAR' AS NNAME FROM DUAL)

SELECT 
    SUBSTR(NNAME,1, INSTR(NNAME,' ')-1) AS F_NAME,
    SUBSTR(NNAME,INSTR(NNAME,' ')+1) L_NAME
FROM A;

-- =============================================================================

WITH N(A,B) AS
(SELECT 1 AS A, 2 AS B FROM DUAL
UNION ALL
SELECT A*B, B+1 FROM N
WHERE B < 6)

SELECT N.*, ROWNUM FACT FROM N;

-- =============================================================================
SELECT TO_CHAR(TO_DATE(3652, 'J'), 'JSP') FROM DUAL;

-- =============================================================================
-- DIFF BETWEEN HIGHEST SALARY AND SECOND HIGHEST SALARY
WITH A AS
(
SELECT DEPARTMENT, MAX(SALARY) SALARY FROM EMPLOYEE
GROUP BY DEPARTMENT
),

B AS
(SELECT DEPARTMENT, SALARY FROM(
SELECT DEPARTMENT,SALARY, DENSE_RANK() OVER(PARTITION BY DEPARTMENT ORDER BY SALARY DESC) RN FROM EMPLOYEE)
WHERE RN = 2
)

SELECT DISTINCT A.DEPARTMENT, A.SALARY - B.SALARY AS DIFF FROM A INNER JOIN B
ON A.DEPARTMENT = B.DEPARTMENT;

-- =============================================================================
select * from employee;

update employee set joining_year =
case 
    when state = 'Maharashtra' then  '2020'
    when state = 'Punjab' then  '2021'
    when state = 'Gujrat' then  '2022'
    when state = 'Tamilnadu' then  '2023'
    else 'pending'
end;

update employee set status =
case 
    when state = 'Maharashtra' then  'working'
    when state = 'Punjab' then  'terminated'
    when state = 'Gujrat' then  'hold'
    when state = 'Tamilnadu' then  'working'
    else 'not yet satrted'
end;





