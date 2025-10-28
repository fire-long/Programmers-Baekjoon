-- 코드를 작성해주세요
SELECT ROUND(AVG(LENGTH), 2) AS AVERAGE_LENGTH
 FROM (
    SELECT ID
         , FISH_TYPE
         , CASE WHEN IFNULL(LENGTH, 0) <= 10 THEN 10
                ELSE LENGTH
                END AS LENGTH
     FROM FISH_INFO
) A;

