--1. количество исполнителей в каждом жанре;

SELECT name_genere, COUNT(name_executor) FROM executor 
LEFT JOIN listofgenere_executor ON listofgenere_executor.executor_id = executor.id
LEFT JOIN listofgenere ON listofgenere_executor.listofgenere_id = listofgenere.id
GROUP BY name_genere;

--2. количество треков, вошедших в альбомы 2019-2020 годов;

 SELECT date, COUNT(name_track) FROM album a
 JOIN track t  ON a.id = t.album_id
 WHERE a.date  >= '2019-01-01' AND a.date <= '2020-12-31'
 GROUP BY date;

--3. средняя продолжительность треков по каждому альбому;

SELECT name_album, AVG(duration) FROM album a
JOIN track t  ON a.id = t.album_id
GROUP BY name_album;

--4. все исполнители, которые не выпустили альбомы в 2020 году; 

SELECT name_executor, date FROM album a
JOIN executor_album ea  ON a.id = ea.album_id
JOIN executor e  ON ea.executor_id = e.id
WHERE a.date NOT BETWEEN '2018-01-01' AND '2018-12-31';

--5. названия сборников, в которых присутствует конкретный исполнитель (выберите сами) Noize MC;

SELECT name_collection FROM collection с
JOIN collection_track ct  ON с.id = ct.collection_id
JOIN track t  ON ct.track_id = t.id
JOIN album a  ON t.album_id = a.id
JOIN executor_album ea  ON a.id = ea.album_id
JOIN executor e  ON ea.executor_id = e.id
WHERE e.name_executor LIKE 'Noize MC';

--6. название альбомов, в которых присутствуют исполнители более 1 жанра; 

SELECT name_album FROM album a
JOIN executor_album ea  ON a.id = ea.album_id
JOIN executor e  ON ea.executor_id = e.id
JOIN listofgenere_executor le  ON e.id = le.executor_id
GROUP BY e.name_executor, a.name_album
HAVING count(le.listofgenere_id) > 1;


--7. наименование треков, которые не входят в сборники;

SELECT name_track FROM track t
LEFT JOIN collection_track ct ON t.id = ct.track_id
WHERE ct.track_id IS NULL;

--8. исполнителя(-ей), написавшего самый короткий по продолжительности трек (теоретически таких треков может быть несколько);

SELECT e.name_executor, t.duration FROM executor e
JOIN executor_album ea ON e.id = ea.executor_id
JOIN album a ON ea.album_id = a.id
JOIN track t ON a.id = t.album_id
WHERE t.duration IN (SELECT MIN(duration) FROM track)

--9. название альбомов, содержащих наименьшее количество треков.

SELECT a.name_album FROM album a
JOIN track t  ON a.id = t.album_id
GROUP BY a.name_album 
HAVING count(t.id) in (
SELECT COUNT (t.id)
FROM album a
JOIN track t  ON a.id = t.album_id
GROUP BY a.name_album
ORDER BY count(t.id) LIMIT 1)