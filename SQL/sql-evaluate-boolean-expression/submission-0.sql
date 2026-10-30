SELECT left_operand, operator, right_operand, 
    CASE 
        WHEN operator='<' THEN
            CASE WHEN v1.value < v2.value
                THEN 'true' 
                ELSE 'false'
            END
        WHEN operator='>' THEN
            CASE WHEN v1.value > v2.value
                THEN 'true' 
                ELSE 'false'
            END
        WHEN operator='=' THEN
            CASE WHEN v1.value = v2.value
                THEN 'true' 
                ELSE 'false'
            END
    ELSE
        'invalid operator type'
    END as value
FROM expressions
INNER JOIN variables v1 ON left_operand=v1.name
INNER JOIN variables v2 ON right_operand=v2.name
