from sqlalchemy import create_engine
import pandas as pd

engine = create_engine('postgresql+psycopg2://root:root@localhost/test_db')


sql = '''
SELECT
	t1."date"
	,t1."rank"
	,t1.song
	,t1.artist
	,t1."last-week"
	,t1."peak-rank"
	,t1."weeks-on-board"
FROM  public."Billboard" AS t1
LIMIT 100
'''

df = pd.read_sql_query(sql, engine)


sql2 = '''
INSERT into tb_artist (
	SELECT t1."date"
	,t1."rank"
	,t1.artist
    ,t1.song
FROM public."Billboard" AS t1
WHERE t1.artist like 'Nirvana%'
order by t1.artist, t1.song, t1."date"
);
'''

engine.execute(sql)
