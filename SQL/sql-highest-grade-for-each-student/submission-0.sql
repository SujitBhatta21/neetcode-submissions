-- Write your query below
SELECT student_id, exam_id, score
FROM (
    SELECT student_id, exam_id, score,
    RANK() OVER (PARTITION BY student_id ORDER BY score DESC, exam_id) as RK
    FROM exam_results
)
WHERE RK=1

