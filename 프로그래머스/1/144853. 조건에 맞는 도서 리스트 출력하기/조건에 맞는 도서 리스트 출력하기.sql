select book_id, to_char(published_date,'YYYY-MM-DD')
from book
where to_char(published_date, 'YYYY') like '2021' and category = '인문'
order by published_date asc;