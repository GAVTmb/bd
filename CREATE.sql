create table ListOfGenere (
id SERIAL primary key,
name VARCHAR(60) NOT NULL UNIQUE 
);

create table Executor (
id SERIAL primary key,
name VARCHAR(60)NOT NULL
);

create table ListOfGenereExecutor (
ListOfGenere_id INTEGER references ListOfGenere(id),
Executor_id INTEGER references Executor(id),
CONSTRAINT le primary key (ListOfGenere_id, Executor_id)
);

create table Album (
id SERIAL primary key,
name VARCHAR(60) NOT NULL,
date date NOT NULL 
);

create table Track (
id SERIAL primary key,
Album_id INTEGER references Album(id),
name VARCHAR(60) NOT NULL,
duration integer NOT NULL
);

create table ExecutorAlbum (
Executor_id INTEGER references Executor(id),
Album_id INTEGER references Album(id),
CONSTRAINT fk primary key (Executor_id, Album_id)
);

create table Collection (
id SERIAL primary key,
name VARCHAR(60) NOT NULL,
date date NOT NULL
);

create table CollectionTrack (
Collection_id INTEGER references Collection(id),
Track_id INTEGER references Track(id),
CONSTRAINT ffk primary key (Collection_id, Track_id)
);