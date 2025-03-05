''' 
 Dense_rank() will add rank
 when same score happen, it will give same rank
 OVER => Window Function, assign rank range
'''
SELECT score, DENSE_RANK() OVER (ORDER BY score DESC) AS 'rank'
FROM Scores
ORDER BY score DESC;
