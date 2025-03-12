-- solutiion to problem https://www.hackerrank.com/challenges/weather-observation-station-20/

WITH ranked_rows AS (
    SELECT 
        s.*,
        ROW_NUMBER() OVER (ORDER BY s.LAT_N) AS row_index, 
        ROUND(s.LAT_N, 4) AS LAN
    FROM STATION AS s
),
max_row AS (
    SELECT MAX(row_index) AS max_v FROM ranked_rows
)
SELECT r.LAN
FROM ranked_rows r
JOIN max_row m ON 1 = 1
WHERE 
    r.row_index = 
    CASE
        WHEN (m.max_v + 1) % 2 = 0 THEN (m.max_v + 1) / 2  -- for odd counts
        ELSE m.max_v / 2  -- for even counts
    END;
