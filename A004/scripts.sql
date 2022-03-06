create table clientes (id serial not null,
nome VARCHAR(250) not null,
idade INTEGER,
primary key (id));

--https://www.kaggle.com/dhruvildave/billboard-the-hot-100-songs

create table public."Billboard" (
	"date" date null,
	"rank" int4 null,
	song varchar(300) null,
	artist varchar(300) null,
	"last-week" float8 null,
	"peak-rank" int4 null,
	"weeks-on-board" int4 null
);

SELECT
	t1."date"
	,t1."rank"
	,t1.song
	,t1.artist
	,t1."last-week"
	,t1."peak-rank"
	,t1."weeks-on-board"
FROM  public."Billboard" AS t1
LIMIT 100;


SELECT
	distinct 
	t1.artist
	,t1.song
FROM  public."Billboard" AS t1
order by t1.artist
	,t1.song;

SELECT
	t1.artist
	,COUNT(*) as qtd_artist
FROM  public."Billboard" AS t1
group by t1.artist
order by t1.artist

SELECT
	t1.song
	,COUNT(*) as qtd_song
FROM  public."Billboard" AS t1
group by t1.song
order by t1.song

----------------------------------
--CTE

with cte_artist as(
	SELECT
		t1.artist
		,COUNT(*) as qtd_artist
	FROM  public."Billboard" AS t1
	group by t1.artist
	order by t1.artist
),

cte_song as(
	SELECT
		t1.song
		,COUNT(*) as qtd_song
	FROM  public."Billboard" AS t1
	group by t1.song
	order by t1.song
)

SELECT
	distinct 
     t1.artist
	,t2.qtd_artist
	,t1.song
	,t3.qtd_song
FROM  public."Billboard" AS t1
left join cte_artist as t2 on (t1.artist = t2.artist)
left join cte_song as t3 on (t1.song = t3.song)
order by 
	t1.artist
	,t1.song;

----------------------------------
--Window Function

with cte_billboard as(
    SELECT distinct 
     t1.artist
	,t1.song
 	,row_number() over(order by artist, song) as "row_number"
 	,row_number() over(partition by artist order by artist, song) as "row_number_artist" 	
    FROM  public."Billboard" AS t1
    ORDER BY t1.artist
	        ,t1.song
)

SELECT * 
FROM cte_billboard
where "row_number_artist"  = 1;

----------------------------------


with cte_billboard as(
    SELECT distinct 
     t1.artist
	,t1.song
    FROM  public."Billboard" AS t1
    ORDER BY t1.artist
	        ,t1.song
)


select *
 	,row_number() over(order by artist, song) as "row_number"
 	,row_number() over(partition by artist order by artist, song) as "row_number_artist" 	
	,rank() over(partition by artist order by artist, song) as "rank"
	,lag(song, 1) over(partition by artist order by artist, song) as "lag_song"
	,lead(song, 1) over(partition by artist order by artist, song) as "lead_song"
	,first_value(song) over(partition by artist order by artist, song) as "first_song"
	,last_value(song) over(partition by artist order by artist, song range between unbounded preceding and unbounded following) as "last_song"	
from cte_billboard

----------------------------------

WITH T(StyleID, ID, Nome)
    AS (
        SELECT 1,1, 'Rhuan' UNION ALL
        SELECT 1,1, 'Andre' UNION ALL
        SELECT 1,2, 'Ana'   UNION ALL
        SELECT 1,2, 'Maria' UNION ALL
        SELECT 1,3, 'Leticia' UNION ALL
        SELECT 1,3, 'Lari' UNION ALL
        SELECT 1,4, 'Edson' UNION ALL
        SELECT 1,4, 'Marcos' UNION ALL
        SELECT 1,5, 'Rhuan' UNION ALL
        SELECT 1,5, 'Lari' UNION ALL
        SELECT 1,6, 'Daisy' UNION ALL
        SELECT 1,6, 'João'                        
    )

SELECT *,
        ROW_NUMBER() OVER(PARTITION BY StyleID ORDER BY ID) AS "ROW_NUMBER",
        RANK() OVER(PARTITION BY StyleID ORDER BY ID)       AS "RANK",
        DENSE_RANK() OVER(PARTITION BY StyleID ORDER BY ID) AS "DENSE_RANK",
        PERCENT_RANK() OVER(PARTITION BY StyleID ORDER BY ID) AS "PERCENT_RANK",
        CUME_DIST() OVER(PARTITION BY StyleID ORDER BY ID) AS "CUME_DIST",
        CUME_DIST() OVER(PARTITION BY StyleID ORDER BY ID DESC) AS "CUME_DIST_DESC",
        FIRST_VALUE(Nome) OVER(PARTITION BY StyleID ORDER BY ID) AS "FIRST_VALUE",
        LAST_VALUE(Nome) OVER(PARTITION BY StyleID ORDER BY ID) AS "LAST_VALUE",
        NTH_VALUE(Nome, 5) OVER(PARTITION BY StyleID ORDER BY ID) AS "NTH_VALUE",
        NTILE(5) OVER(PARTITION BY StyleID ORDER BY ID) AS "NTILE",
        LAG(Nome, 1) OVER(PARTITION BY StyleID ORDER BY ID) AS "LAG",
        LEAD(Nome, 1) OVER(PARTITION BY StyleID ORDER BY ID) AS "LEAD"
FROM T;

------------------------------
CREATE TABLE tb_web_site as (
	with cte_dedup_artist as (
		SELECT
			t1."date"
			,t1."rank"
			,t1.artist
			,row_number() over(partition by artist order by artist, song) as "dedup"
		FROM  public."Billboard" AS t1
		ORDER BY t1.artist, t1."date"
	)
	SELECT 	"date"
			,"rank"
			,artist
	FROM cte_dedup_artist
	WHERE dedup = 1
);

SELECT * FROM tb_web_site

CREATE TABLE tb_artist as (
	SELECT
		t1."date"
		,t1."rank"
		,t1.artist
		,t1.song
	FROM  public."Billboard" AS t1
	WHERE t1.artist = 'AC/DC'
	ORDER BY t1.artist, t1."date"
)

CREATE view vw_artist as (
	SELECT
		t1."date"
		,t1."rank"
		,t1.artist
		,t1.song
	FROM  public."Billboard" AS t1
	WHERE t1.artist = 'AC/DC'
	ORDER BY t1.artist, t1."date"
)

INSERT into tb_artist (
	SELECT ...
)

CREATE view vw_... as (
	with cte_...
	...
)