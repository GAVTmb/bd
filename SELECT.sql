--название и год выхода альбомов, вышедших в 2018 году+

SELECT name_album, date FROM album
WHERE date > '2017-12-31' AND date < '2019-01-01'; 

--название треков, продолжительность которых не менее 3,5 минуты+

SELECT name_track FROM track
WHERE duration >= '3:30';

--названия сборников, вышедших в период с 2018 по 2020 год включительно+

SELECT name_collection FROM collection
WHERE date > '2017-12-31' AND date < '2021-01-01';

--название треков, которые содержат слово "мой"/"my"+

SELECT name_track FROM track
WHERE name_track LIKE '%My%';

--исполнители, чье имя состоит из 1 слова+

SELECT name_track FROM track
WHERE name_track NOT LIKE '% %';

--название и продолжительность самого длительного трека+

SELECT name_track, duration FROM track
ORDER BY duration DESC
LIMIT 1;