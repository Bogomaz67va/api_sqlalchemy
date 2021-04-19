from models.AlchemyApi import AlchemyApi

user = AlchemyApi('******', '******', '******')
# user.select_all('executor', 'name', 'id', 'fetchone')
# user.select_sql('album', 'ORDER BY id', 'name', 'year_of_issue', 'fetchone')
# user.show_columns_name('track')
# user.insert('track', 'id, name, duration, id_album', 19, 'name', 3.03, 1)
print("количество исполнителей в каждом жанре;")
user.command_sql("select g.name, count(g.id) from executor e inner join executorgenres eg "
                 "on e.id=eg.id_executor join genres g on eg.id_genres=g.id group by g.name;")
print("количество треков, вошедших в альбомы 2019-2020 годов;")
user.command_sql("select a.name,a.year_of_issue, count(t.id_album) from track t inner join album a "
                 "on t.id_album=a.id group by a.name, a.year_of_issue "
                 "having a.year_of_issue >= '2019-01-31' and a.year_of_issue <= '2020-12-31';")
print("средняя продолжительность треков по каждому альбому;")
user.command_sql("select a.name, avg(t.duration) from track t inner join album a on t.id_album=a.id group by a.name;")
print("все исполнители, которые не выпустили альбомы в 2020 году;")
user.command_sql("select e.name, a.name, a.year_of_issue from executor e inner join executoralbum ea "
                 "on e.id=ea.id_executor join album a "
                 "on a.id=ea.id_album group by e.name, a.name, a.year_of_issue "
                 "having a.year_of_issue <= '2019-12-31';")
print("названия сборников, в которых присутствует конкретный исполнитель (выберите сами);")
user.command_sql("select e.name, a.name from executor e inner join executoralbum ea "
                 "on e.id=ea.id_executor join album a "
                 "on a.id=ea.id_album group by e.name, a.name "
                 "having e.name='Михаил Рыжеков';")
print("название альбомов, в которых присутствуют исполнители более 1 жанра;")
user.command_sql("select a.name,e.name, count(eg.id_genres) from executor e inner join executorgenres eg "
                 "on e.id=eg.id_executor join executoralbum ea "
                 "on e.id=ea.id_executor join album a "
                 "on ea.id_album=a.id "
                 "group by a.name, e.name "
                 "having count(eg.id_genres) >= 2")
print("наименование треков, которые не входят в сборники;")
user.command_sql("select t.name from track t left join collectiontrack ct on t.id=ct.id_track where ct.id is null;")
print("исполнителя(-ей), "
      "написавшего самый короткий по продолжительности трек (теоретически таких треков может быть несколько);")
user.command_sql("select e.name, min(t.duration) from executor e inner join executoralbum ea "
                 "on e.id=ea.id_executor join album a on a.id=ea.id_album join track t "
                 "on t.id_album=a.id group by e.name having min(t.duration)<=1;")
print("название альбомов, содержащих наименьшее количество треков.")
user.command_sql("select a.name, count(t.id_album) from album a inner join track t "
                 "on a.id=t.id_album group by a.name order by count(t.id_album) limit 3;")