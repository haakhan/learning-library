SELECT 
    g.name as genre,
    TO_CHAR(c.day_id,'YYYY-MM') as month,
    ROUND(sum(c.actual_price),0) sales
FROM  custsales c, genre g
WHERE g.genre_id = c.genre_id
AND   to_char(c.day_id, 'MON') in ('DEC')
GROUP BY to_char(c.day_id,'YYYY-MM'), c.genre_id, g.name
ORDER BY genre, month;


WITH sales_vs_lastyear as (
    SELECT g.name as genre,
        TO_CHAR(c.day_id,'YYYY-MM') as month,
        ROUND(SUM(c.actual_price),0) sales,
        LAG(ROUND(SUM(c.actual_price),0)) OVER (
                PARTITION BY g.name
                ORDER BY to_char(c.day_id,'YYYY-MM')
               ) as last_year         
    FROM custsales c, genre g
    WHERE g.genre_id = c.genre_id
     AND to_char(c.day_id, 'MON') in ('DEC')
    GROUP BY TO_CHAR(c.day_id,'YYYY-MM'), c.genre_id, g.name
    ORDER BY genre, month
)
SELECT 
    genre, 
    sales as sales,
    last_year as last_year,
    last_year - sales as change
FROM  sales_vs_lastyear
WHERE last_year is not null
ORDER BY round(last_year - sales) DESC;

-- Primary genre is the first one listed
select
    title,
    genres,
    json_value(genres, '$[0]' returning varchar2(100)) as primary_genre
from t_movie m;

-- movie sales by genre (note - a customer select a movie from a genre)
WITH sales_by_genre as (
    SELECT
        g.name as genre,
        m.title,
        round(sum(c.actual_price),0) as sales        
    FROM t_movie m, custsales c, genre g
    WHERE m.movie_id = c.movie_id
    AND c.genre_id = g.genre_id
    GROUP BY g.name, m.title
    ORDER BY 3 DESC
)
SELECT * 
FROM sales_by_genre
WHERE rownum < 20;

-- Rank sales across genres
WITH sales_by_genre as (
    SELECT
        g.name as genre,
        m.title,
        round(sum(c.actual_price),0) as sales        
    FROM t_movie m, custsales c, genre g
    WHERE m.movie_id = c.movie_id
    AND c.genre_id = g.genre_id
    AND g.name in ('Drama','Action','Comedy')
    GROUP BY g.name, m.title
    ORDER BY 3 desc
)
SELECT 
    RANK() OVER(ORDER BY sales DESC) as ranking,
    genre,
    title,
    sales
FROM sales_by_genre
FETCH FIRST 10 ROWS ONLY
;

-- Rank sales by genre/movie combination
WITH sales_grouping as (
    SELECT
        g.name as genre,
        m.title as movie,
        round(sum(c.actual_price),0) as sales
    FROM t_movie m, custsales c, genre g
    WHERE m.movie_id = c.movie_id
      AND c.genre_id = g.genre_id
      AND g.name IN ('Drama','Action','Comedy')
    GROUP BY g.name, m.title
)
SELECT 
    genre,
    movie,
    sales,
    RANK () OVER ( order by sales desc ) as ranking
FROM sales_grouping
FETCH FIRST 20 ROWS ONLY
;

-- Rank sales within genres
WITH sales_grouping as (
    SELECT
        g.name as genre,
        m.title as movie,
        round(sum(c.actual_price),0) as sales
    FROM t_movie m, custsales c, genre g
    WHERE m.movie_id = c.movie_id
      AND c.genre_id = g.genre_id
      AND g.name in ('Drama','Action','Comedy')
    GROUP BY g.name, m.title
),
movie_ranking_by_genre as (
    SELECT 
        genre,
        movie,
        sales,
        RANK () OVER ( PARTITION BY genre ORDER BY sales DESC ) as ranking
    FROM sales_grouping
)
SELECT * 
FROM movie_ranking_by_genre
WHERE ranking <= 5
ORDER BY genre ASC, ranking ASC
;

-- Finally, lets add totals by group
WITH sales_grouping as (
    SELECT
        g.name as genre,
        m.title as movie,
        round(sum(c.actual_price),0) as sales
    FROM t_movie m, custsales c, genre g
    WHERE m.movie_id = c.movie_id
      AND c.genre_id = g.genre_id
      AND g.name IN ('Drama','Action','Comedy')
    GROUP BY g.name, m.title
),
movie_ranking_by_genre as (
    SELECT
        genre,
        movie,
        sales,
        RANK () OVER ( partition by genre order by sales desc ) as ranking
    FROM sales_grouping
)
SELECT genre,
       movie,
       SUM(sales),
       ROUND(RATIO_TO_REPORT (SUM(sales)) OVER (PARTITION BY genre), 2) * 2 as ratio
FROM movie_ranking_by_genre
WHERE ranking <= 5
GROUP BY ROLLUP(genre, movie)
ORDER BY 1 ASC, 3 DESC
;

SELECT
    g.name,
    count(m.genre_id)
    FROM custsales m
    FULL OUTER JOIN genre g ON m.genre_id = g.genre_id
    WHERE to_char(day_id, 'YYYYY') = '2020'
    GROUP BY g.name
    order by 1;
    
    select to_char(day_id, 'YYYY') from custsales;
    
-- RFM
with a as (
SELECT
    m.cust_id,
    c.first_name||' '||c.last_name as cust_name,
    c.country,
    c.gender,
    c.age,
    c.income_level,
    NTILE (5) OVER (ORDER BY SUM(m.actual_price)) AS rfm_monetary
FROM custsales m
    INNER JOIN customer c ON c.cust_id = m.cust_id
GROUP BY m.cust_id,
    c.first_name||' '||c.last_name,
    c.country,
    c.gender,
    c.age,
    c.income_level
ORDER BY m.cust_id,
    c.first_name||' '||c.last_name,
    c.country,
    c.gender,
    c.age,
    c.income_level)
select * 
from a
where rownum < 20;