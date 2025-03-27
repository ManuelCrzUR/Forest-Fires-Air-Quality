-- CREACIÓN DE TODAS LAS TABLAS QUE SON NECESARIAS (PAISES E INCENDIOS FORESETALES)

-- Tablas para Brasil 2010
CREATE TABLE fire_data_2010_Brazil (
    latitude FLOAT,
    longitude FLOAT,
    brightness FLOAT,
    scan FLOAT,
    track FLOAT,
    acq_date DATE,
    acq_time INT,
    satellite VARCHAR(10),
    instrument VARCHAR(10),
    confidence INT,
    version FLOAT,
    bright_t31 FLOAT,
    frp FLOAT,
    daynight CHAR(1),
    type INT
);

-- Tablas para Brasil
CREATE TABLE fire_data_2011_Brazil (LIKE fire_data_2010_Brazil INCLUDING ALL);
CREATE TABLE fire_data_2012_Brazil (LIKE fire_data_2010_Brazil INCLUDING ALL);
CREATE TABLE fire_data_2013_Brazil (LIKE fire_data_2010_Brazil INCLUDING ALL);
CREATE TABLE fire_data_2014_Brazil (LIKE fire_data_2010_Brazil INCLUDING ALL);
CREATE TABLE fire_data_2015_Brazil (LIKE fire_data_2010_Brazil INCLUDING ALL);
CREATE TABLE fire_data_2016_Brazil (LIKE fire_data_2010_Brazil INCLUDING ALL);
CREATE TABLE fire_data_2017_Brazil (LIKE fire_data_2010_Brazil INCLUDING ALL);
CREATE TABLE fire_data_2018_Brazil (LIKE fire_data_2010_Brazil INCLUDING ALL);
CREATE TABLE fire_data_2019_Brazil (LIKE fire_data_2010_Brazil INCLUDING ALL);
CREATE TABLE fire_data_2020_Brazil (LIKE fire_data_2010_Brazil INCLUDING ALL);

-- Tablas para Chile
CREATE TABLE fire_data_2010_Chile (LIKE fire_data_2010_Brazil INCLUDING ALL);
CREATE TABLE fire_data_2011_Chile (LIKE fire_data_2010_Brazil INCLUDING ALL);
CREATE TABLE fire_data_2012_Chile (LIKE fire_data_2010_Brazil INCLUDING ALL);
CREATE TABLE fire_data_2013_Chile (LIKE fire_data_2010_Brazil INCLUDING ALL);
CREATE TABLE fire_data_2014_Chile (LIKE fire_data_2010_Brazil INCLUDING ALL);
CREATE TABLE fire_data_2015_Chile (LIKE fire_data_2010_Brazil INCLUDING ALL);
CREATE TABLE fire_data_2016_Chile (LIKE fire_data_2010_Brazil INCLUDING ALL);
CREATE TABLE fire_data_2017_Chile (LIKE fire_data_2010_Brazil INCLUDING ALL);
CREATE TABLE fire_data_2018_Chile (LIKE fire_data_2010_Brazil INCLUDING ALL);
CREATE TABLE fire_data_2019_Chile (LIKE fire_data_2010_Brazil INCLUDING ALL);
CREATE TABLE fire_data_2020_Chile (LIKE fire_data_2010_Brazil INCLUDING ALL);

-- Tablas para Colombia
CREATE TABLE fire_data_2010_Colombia (LIKE fire_data_2010_Brazil INCLUDING ALL);
CREATE TABLE fire_data_2011_Colombia (LIKE fire_data_2010_Brazil INCLUDING ALL);
CREATE TABLE fire_data_2012_Colombia (LIKE fire_data_2010_Brazil INCLUDING ALL);
CREATE TABLE fire_data_2013_Colombia (LIKE fire_data_2010_Brazil INCLUDING ALL);
CREATE TABLE fire_data_2014_Colombia (LIKE fire_data_2010_Brazil INCLUDING ALL);
CREATE TABLE fire_data_2015_Colombia (LIKE fire_data_2010_Brazil INCLUDING ALL);
CREATE TABLE fire_data_2016_Colombia (LIKE fire_data_2010_Brazil INCLUDING ALL);
CREATE TABLE fire_data_2017_Colombia (LIKE fire_data_2010_Brazil INCLUDING ALL);
CREATE TABLE fire_data_2018_Colombia (LIKE fire_data_2010_Brazil INCLUDING ALL);
CREATE TABLE fire_data_2019_Colombia (LIKE fire_data_2010_Brazil INCLUDING ALL);
CREATE TABLE fire_data_2020_Colombia (LIKE fire_data_2010_Brazil INCLUDING ALL);



-- TABLAS POR AÑO
-- Tabla general por año
CREATE TABLE fire_data_2010 AS
SELECT * FROM fire_data_2010_Brazil
UNION ALL
SELECT * FROM fire_data_2010_Chile
UNION ALL
SELECT * FROM fire_data_2010_Colombia;

CREATE TABLE fire_data_2011 AS
SELECT * FROM fire_data_2011_Brazil
UNION ALL
SELECT * FROM fire_data_2011_Chile
UNION ALL
SELECT * FROM fire_data_2011_Colombia;

CREATE TABLE fire_data_2012 AS
SELECT * FROM fire_data_2012_Brazil
UNION ALL
SELECT * FROM fire_data_2012_Chile
UNION ALL
SELECT * FROM fire_data_2012_Colombia;

CREATE TABLE fire_data_2013 AS
SELECT * FROM fire_data_2013_Brazil
UNION ALL
SELECT * FROM fire_data_2013_Chile
UNION ALL
SELECT * FROM fire_data_2013_Colombia;

CREATE TABLE fire_data_2014 AS
SELECT * FROM fire_data_2014_Brazil
UNION ALL
SELECT * FROM fire_data_2014_Chile
UNION ALL
SELECT * FROM fire_data_2014_Colombia;

CREATE TABLE fire_data_2015 AS
SELECT * FROM fire_data_2015_Brazil
UNION ALL
SELECT * FROM fire_data_2015_Chile
UNION ALL
SELECT * FROM fire_data_2015_Colombia;

CREATE TABLE fire_data_2016 AS
SELECT * FROM fire_data_2016_Brazil
UNION ALL
SELECT * FROM fire_data_2016_Chile
UNION ALL
SELECT * FROM fire_data_2016_Colombia;

CREATE TABLE fire_data_2017 AS
SELECT * FROM fire_data_2017_Brazil
UNION ALL
SELECT * FROM fire_data_2017_Chile
UNION ALL
SELECT * FROM fire_data_2017_Colombia;

CREATE TABLE fire_data_2018 AS
SELECT * FROM fire_data_2018_Brazil
UNION ALL
SELECT * FROM fire_data_2018_Chile
UNION ALL
SELECT * FROM fire_data_2018_Colombia;

CREATE TABLE fire_data_2019 AS
SELECT * FROM fire_data_2019_Brazil
UNION ALL
SELECT * FROM fire_data_2019_Chile
UNION ALL
SELECT * FROM fire_data_2019_Colombia;

CREATE TABLE fire_data_2020 AS
SELECT * FROM fire_data_2020_Brazil
UNION ALL
SELECT * FROM fire_data_2020_Chile
UNION ALL
SELECT * FROM fire_data_2020_Colombia;

-- CRACIÓN DE TABLA GENERA UNIFICADA

CREATE TABLE fire_data AS
SELECT * FROM fire_data_2010
UNION ALL
SELECT * FROM fire_data_2011
UNION ALL
SELECT * FROM fire_data_2012
UNION ALL
SELECT * FROM fire_data_2013
UNION ALL
SELECT * FROM fire_data_2014
UNION ALL
SELECT * FROM fire_data_2015
UNION ALL
SELECT * FROM fire_data_2016
UNION ALL
SELECT * FROM fire_data_2017
UNION ALL
SELECT * FROM fire_data_2018
UNION ALL
SELECT * FROM fire_data_2019
UNION ALL
SELECT * FROM fire_data_2020;

