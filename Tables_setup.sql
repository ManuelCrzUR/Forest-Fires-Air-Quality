
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


-- Crear tablas para Brasil
CREATE TABLE modis_2010_Brazil (LIKE fire_data_2010_Brazil INCLUDING ALL);
CREATE TABLE modis_2011_Brazil (LIKE fire_data_2010_Brazil INCLUDING ALL);
CREATE TABLE modis_2012_Brazil (LIKE fire_data_2010_Brazil INCLUDING ALL);
CREATE TABLE modis_2013_Brazil (LIKE fire_data_2010_Brazil INCLUDING ALL);
CREATE TABLE modis_2014_Brazil (LIKE fire_data_2010_Brazil INCLUDING ALL);
CREATE TABLE modis_2015_Brazil (LIKE fire_data_2010_Brazil INCLUDING ALL);
CREATE TABLE modis_2016_Brazil (LIKE fire_data_2010_Brazil INCLUDING ALL);
CREATE TABLE modis_2017_Brazil (LIKE fire_data_2010_Brazil INCLUDING ALL);
CREATE TABLE modis_2018_Brazil (LIKE fire_data_2010_Brazil INCLUDING ALL);
CREATE TABLE modis_2019_Brazil (LIKE fire_data_2010_Brazil INCLUDING ALL);
CREATE TABLE modis_2020_Brazil (LIKE fire_data_2010_Brazil INCLUDING ALL);

-- Crear tablas para Colombia
CREATE TABLE modis_2010_Colombia (LIKE fire_data_2010_Brazil INCLUDING ALL);
CREATE TABLE modis_2011_Colombia (LIKE fire_data_2010_Brazil INCLUDING ALL);
CREATE TABLE modis_2012_Colombia (LIKE fire_data_2010_Brazil INCLUDING ALL);
CREATE TABLE modis_2013_Colombia (LIKE fire_data_2010_Brazil INCLUDING ALL);
CREATE TABLE modis_2014_Colombia (LIKE fire_data_2010_Brazil INCLUDING ALL);
CREATE TABLE modis_2015_Colombia (LIKE fire_data_2010_Brazil INCLUDING ALL);
CREATE TABLE modis_2016_Colombia (LIKE fire_data_2010_Brazil INCLUDING ALL);
CREATE TABLE modis_2017_Colombia (LIKE fire_data_2010_Brazil INCLUDING ALL);
CREATE TABLE modis_2018_Colombia (LIKE fire_data_2010_Brazil INCLUDING ALL);
CREATE TABLE modis_2019_Colombia (LIKE fire_data_2010_Brazil INCLUDING ALL);
CREATE TABLE modis_2020_Colombia (LIKE fire_data_2010_Brazil INCLUDING ALL);

-- Crear tablas para Chile
CREATE TABLE modis_2010_Chile (LIKE fire_data_2010_Brazil INCLUDING ALL);
CREATE TABLE modis_2011_Chile (LIKE fire_data_2010_Brazil INCLUDING ALL);
CREATE TABLE modis_2012_Chile (LIKE fire_data_2010_Brazil INCLUDING ALL);
CREATE TABLE modis_2013_Chile (LIKE fire_data_2010_Brazil INCLUDING ALL);
CREATE TABLE modis_2014_Chile (LIKE fire_data_2010_Brazil INCLUDING ALL);
CREATE TABLE modis_2015_Chile (LIKE fire_data_2010_Brazil INCLUDING ALL);
CREATE TABLE modis_2016_Chile (LIKE fire_data_2010_Brazil INCLUDING ALL);
CREATE TABLE modis_2017_Chile (LIKE fire_data_2010_Brazil INCLUDING ALL);
CREATE TABLE modis_2018_Chile (LIKE fire_data_2010_Brazil INCLUDING ALL);
CREATE TABLE modis_2019_Chile (LIKE fire_data_2010_Brazil INCLUDING ALL);
CREATE TABLE modis_2020_Chile (LIKE fire_data_2010_Brazil INCLUDING ALL);

	
