
--Жанры

INSERT INTO listofgenere(name_genere)
VALUES('Pop');

INSERT INTO listofgenere(name_genere)
VALUES('Rap and Hip hop');

insert into listofgenere(name_genere)
VALUES('Rock');

INSERT INTO listofgenere(name_genere)
VALUES('Classic');
 
INSERT INTO listofgenere(name_genere)
VALUES('R&B');

--Исполнители

INSERT INTO executor(name_executor)
VALUES('ANNA ASTI');

INSERT INTO executor(name_executor)
VALUES('Artik & Asti');

INSERT INTO executor(name_executor)
VALUES('Noize MC');

INSERT INTO executor(name_executor)
VALUES('Black Eyed Peas');

INSERT INTO executor(name_executor)
VALUES('Pink Floyd');

INSERT INTO executor(name_executor)
VALUES('The Beatles');

INSERT INTO executor(name_executor)
VALUES('Ludovico Einaudi');

INSERT INTO executor(name_executor)
VALUES('Secret Garden');

INSERT INTO executor(name_executor)
VALUES('Rihanna');

INSERT INTO executor(name_executor)
VALUES('The Weeknd');

--Жанр Исполнитель

INSERT INTO listofgenere_executor(listofgenere_id, executor_id)
VALUES(1, 1);

INSERT INTO listofgenere_executor(listofgenere_id, executor_id)
VALUES(1, 2);

INSERT INTO listofgenere_executor(listofgenere_id, executor_id)
VALUES(1, 9);

INSERT INTO listofgenere_executor(listofgenere_id, executor_id)
VALUES(1, 10);

INSERT INTO listofgenere_executor(listofgenere_id, executor_id)
VALUES(2, 10);

INSERT INTO listofgenere_executor(listofgenere_id, executor_id)
VALUES(2, 3);

INSERT INTO listofgenere_executor(listofgenere_id, executor_id)
VALUES(2, 4);

INSERT INTO listofgenere_executor(listofgenere_id, executor_id)
VALUES(3, 5);

INSERT INTO listofgenere_executor(listofgenere_id, executor_id)
VALUES(3, 6);

INSERT INTO listofgenere_executor(listofgenere_id, executor_id)
VALUES(4, 7);

INSERT INTO listofgenere_executor(listofgenere_id, executor_id)
VALUES(4, 8);

INSERT INTO listofgenere_executor(listofgenere_id, executor_id)
VALUES(5, 9);

INSERT INTO listofgenere_executor(listofgenere_id, executor_id)
VALUES(5, 10);

--album

INSERT INTO album(name_album, date)
VALUES('Феникс', '2022-06-03');

INSERT INTO album(name_album, date)
VALUES('LIVE в A2 Green Concert', '2018-06-16');

INSERT INTO album(name_album, date)
VALUES('No Comments', '2018-03-10');

INSERT INTO album(name_album, date)
VALUES('THE E.N.D.', '2009-04-15');

INSERT INTO album(name_album, date)
VALUES('The Wall', '1979-03-20');

INSERT INTO album(name_album, date)
VALUES('Yellow Submarine', '1969-05-01');

INSERT INTO album(name_album, date)
VALUES('LonelinessPiano Collection', '2022-05-01');

INSERT INTO album(name_album, date)
VALUES('Earthsongs', '2005-12-01');

INSERT INTO album(name_album, date)
VALUES('Right Now', '2013-11-20');

INSERT INTO album(name_album, date)
VALUES('You Da One', '2011-09-22');

INSERT INTO album(name_album, date)
VALUES('My Dear Melancholy', '2018-09-25');

--executoralbum

INSERT INTO executor_album(executor_id, album_id)
VALUES(1, 1);

INSERT INTO executor_album(executor_id, album_id)
VALUES(2, 2);

INSERT INTO executor_album(executor_id, album_id)
VALUES(3, 3);

INSERT INTO executor_album(executor_id, album_id)
VALUES(4, 4);

INSERT INTO executor_album(executor_id, album_id)
VALUES(5, 5);

INSERT INTO executor_album(executor_id, album_id)
VALUES(6, 6);

INSERT INTO executor_album(executor_id, album_id)
VALUES(7, 7);

INSERT INTO executor_album(executor_id, album_id)
VALUES(8, 8);

INSERT INTO executor_album(executor_id, album_id)
VALUES(9, 9);

INSERT INTO executor_album(executor_id, album_id)
VALUES(9, 10);

INSERT INTO executor_album(executor_id, album_id)
VALUES(10, 11);

--track

INSERT INTO track(album_id, name_track, duration)
VALUES(1, 'По барам', '3:57');

INSERT INTO track(album_id, name_track, duration)
VALUES(1, 'Химия', '2:37');

INSERT INTO track(album_id, name_track, duration)
VALUES(1, 'Феникс', '3:49');

INSERT INTO track(album_id, name_track, duration)
VALUES(2, 'Таких не бывает', '3:06');

INSERT INTO track(album_id, name_track, duration)
VALUES(2, 'Никому не отдам', '3:24');

INSERT INTO track(album_id, name_track, duration)
VALUES(3, 'Детка, послушай', '3:38');

INSERT INTO track(album_id, name_track, duration)
VALUES(3, 'В темноте', '3:26');

INSERT INTO track(album_id, name_track, duration)
VALUES(4, 'Out Of My Head', '3:51');

INSERT INTO track(album_id, name_track, duration)
VALUES(4, 'Boom Boom Pow', '4:11');

INSERT INTO track(album_id, name_track, duration)
VALUES(5, 'One Of My Turns', '3:36');

INSERT INTO track(album_id, name_track, duration)
VALUES(5, 'Goodbye Blue Sky', '2:47');

INSERT INTO track(album_id, name_track, duration)
VALUES(6, 'Yellow Submarine', '2:39');

INSERT INTO track(album_id, name_track, duration)
VALUES(6, 'Hey Bulldog', '3:11');

INSERT INTO track(album_id, name_track, duration)
VALUES(7, 'Fly From', '5:39');

INSERT INTO track(album_id, name_track, duration)
VALUES(7, 'Una Mattina From', '4:00');

INSERT INTO track(album_id, name_track, duration)
VALUES(8, 'Song From A Secret Garden', '3:31');

INSERT INTO track(album_id, name_track, duration)
VALUES(8, 'Lotus', '4:35');

INSERT INTO track(album_id, name_track, duration)
VALUES(9, 'Right Now Ralphi Rosario Mix', '7:42');

INSERT INTO track(album_id, name_track, duration)
VALUES(9, 'Right Now Sick Individuals Radio Edit', '3:17');

INSERT INTO track(album_id, name_track, duration)
VALUES(10, 'You Da One Dave Aude Radio', '3:51');

INSERT INTO track(album_id, name_track, duration)
VALUES(10, 'You Da One Gregor Salto Vegas Club', '4:44');

INSERT INTO track(album_id, name_track, duration)
VALUES(11, 'Call Out My Name', '3:44');

INSERT INTO track(album_id, name_track, duration)
VALUES(11, 'Try Me', '3:41');

--collection

INSERT INTO collection(name_collection, date)
VALUES('Rock collection', '2022-10-1');

INSERT INTO collection(name_collection, date)
VALUES('Collection of songs', '2022-11-2');

insert into collection(name_collection, date)
VALUES('Pop collection', '2022-11-2');

INSERT INTO collection(name_collection, date)
VALUES('Rap and Hip hop collection', '2022-01-01');

INSERT INTO collection(name_collection, date)
VALUES('Classic', '2021-03-23');

INSERT INTO collection(name_collection, date)
VALUES('R&B collection', '2021-04-13');

INSERT INTO collection(name_collection, date)
VALUES('Collection winter 2022', '2022-01-01');

INSERT INTO collection(name_collection, date)
VALUES('Collection 2018', '2018-01-01');

--collectiontrack

INSERT INTO collection_track(collection_id, track_id)
VALUES(1, 10);

INSERT INTO collection_track(collection_id, track_id)
VALUES(1, 11);

INSERT INTO collection_track(collection_id, track_id)
VALUES(1, 13);

INSERT INTO collection_track(collection_id, track_id)
VALUES(1, 12);

INSERT INTO collection_track(collection_id, track_id)
VALUES(2, 1);

INSERT INTO collection_track(collection_id, track_id)
VALUES(2, 7);

INSERT INTO collection_track(collection_id, track_id)
VALUES(2, 20);

INSERT INTO collection_track(collection_id, track_id)
VALUES(2, 17);

INSERT INTO collection_track(collection_id, track_id)
VALUES(2, 11);

INSERT INTO collection_track(collection_id, track_id)
VALUES(2, 3);

INSERT INTO collection_track(collection_id, track_id)
VALUES(3, 1);

INSERT INTO collection_track(collection_id, track_id)
VALUES(3, 3);

INSERT INTO collection_track(collection_id, track_id)
VALUES(3, 5);

INSERT INTO collection_track(collection_id, track_id)
VALUES(3, 20);

INSERT INTO collection_track(collection_id, track_id)
VALUES(3, 22);

INSERT INTO collection_track(collection_id, track_id)
VALUES(4, 6);

INSERT INTO collection_track(collection_id, track_id)
VALUES(4, 7);

INSERT INTO collection_track(collection_id, track_id)
VALUES(4, 8);

INSERT INTO collection_track(collection_id, track_id)
VALUES(4, 9);

INSERT INTO collection_track(collection_id, track_id)
VALUES(5, 14);

INSERT INTO collection_track(collection_id, track_id)
VALUES(5, 15);

INSERT INTO collection_track(collection_id, track_id)
VALUES(5, 17);

INSERT INTO collection_track(collection_id, track_id)
VALUES(6, 18);

INSERT INTO collection_track(collection_id, track_id)
VALUES(6, 19);

INSERT INTO collection_track(collection_id, track_id)
VALUES(6, 20);

INSERT INTO collection_track(collection_id, track_id)
VALUES(6, 21);

INSERT INTO collection_track(collection_id, track_id)
VALUES(6, 22);

INSERT INTO collection_track(collection_id, track_id)
VALUES(6, 23);

INSERT INTO collection_track(collection_id, track_id)
VALUES(7, 1);


INSERT INTO collection_track(collection_id, track_id)
VALUES(7, 2);

INSERT INTO collection_track(collection_id, track_id)
VALUES(7, 3);

INSERT INTO collection_track(collection_id, track_id)
VALUES(7, 14);

INSERT INTO collection_track(collection_id, track_id)
VALUES(7, 15);

INSERT INTO collection_track(collection_id, track_id)
VALUES(8, 4);

INSERT INTO collection_track(collection_id, track_id)
VALUES(8, 5);

INSERT INTO collection_track(collection_id, track_id)
VALUES(8, 6);

INSERT INTO collection_track(collection_id, track_id)
VALUES(8, 7);

INSERT INTO collection_track(collection_id, track_id)
VALUES(8, 22);

INSERT INTO collection_track(collection_id, track_id)
VALUES(8, 23);