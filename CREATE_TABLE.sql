CREATE TABLE ListOfGenere (
id SERIAL PRIMARY KEY,
name_genere VARCHAR(60)
);

CREATE TABLE Executor (
id SERIAL PRIMARY KEY,
name_executor VARCHAR(60)
);

CREATE TABLE ListOfGenere_Executor (
ListOfGenere_id INTEGER REFERENCES ListOfGenere(id),
Executor_id INTEGER REFERENCES Executor(id),
CONSTRAINT le PRIMARY KEY (ListOfGenere_id,
Executor_id)
);

CREATE TABLE Album (
id SERIAL PRIMARY KEY,
name_album VARCHAR(60),
date date  
);

CREATE TABLE Track (
id SERIAL PRIMARY KEY,
Album_id INTEGER REFERENCES Album(id),
name_track VARCHAR(60),
duration time 
);

CREATE TABLE Executor_Album (
Executor_id INTEGER REFERENCES Executor(id),
Album_id INTEGER REFERENCES Album(id),
CONSTRAINT fk PRIMARY KEY (Executor_id,
Album_id)
);

CREATE TABLE Collection (
id SERIAL PRIMARY KEY,
name_collection VARCHAR(60),
date date
);

CREATE TABLE Collection_Track (
Collection_id INTEGER REFERENCES Collection(id),
Track_id INTEGER REFERENCES Track(id),
CONSTRAINT ffk PRIMARY KEY (Collection_id,
Track_id)
);