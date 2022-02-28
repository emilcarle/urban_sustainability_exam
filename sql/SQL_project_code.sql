-- SQL code

-- Creating a new data base (e.g. bikeability_index) in PostgreSQL

-- creating an extension for postgis
CREATE EXTENSION postgis;


-- selecting the full version 
SELECT post_gis_full_version();


-- searching spatial data e.g. on fisbroker
-- implementing the spatial data (WFS) in QGIS
-- exporting shapefiles to local drive
-- creating Post GIS data base connection in QGIS 
-- uploading the shapefiles to QGIS 
-- refreshing the data base in PostgreSQL


-- Subsetting our district layer (ortsteile) to a single district
-- e.g. Charlottenburg

CREATE TABLE charlottenburg AS
SELECT * FROM ortsteile
WHERE nam = ‘Charlottenburg’


-- Creating polygon layer (hexagon shape) for the subset district
-- layer, e.g. Charlottenburg

CREATE TABLE hex_chbrg AS
SELECT charlottenburg.nam, hex.geom
FROM charlottenburg
CROSS JOIN ST_HexagonGrid(10, charlottenburg.geom) AS hex
WHERE ST_Intersects(charlottenburg.geom, hex.geom);


-- Joining the polygon layer with the target infrastructure data 
--  of the respective shapefile (e.g. type of bike lanes from 
-- radverkehrsanlagen.shp)

--  Joining line string and hexagon
--  bikepath layer
CREATE TABLE rad_chbrg AS
SELECT
  hc.nam,
  rad.ortstl,
  rad.rva_typ,
  hc.geom
FROM hex_chbrg AS hc
JOIN radverkehrsanlagen AS rad
ON ST_Intersects(hc.geom,rad.geom); 


-- Joining line string and hexagon
--  speed limit layer
CREATE TABLE speed_chbrg AS
SELECT
  hc.nam,
  speed.wert_ves,
  hc.geom
FROM hex_chbrg AS hc
JOIN tempolimits AS speed
ON ST_Intersects(hc.geom,speed.geom); 

-- Joining line string and hexagon
-- traffic volume layer

CREATE TABLE traffic_chbrg AS
SELECT
  hc.nam,
  traffic.dtvw_kfz,
  traffic.dtvw_lkw,
  hc.geom
FROM hex_chbrg AS hc
JOIN verkehrsmengen AS traffic 
ON ST_Intersects(hc.geom,traffic.geom); 

-- Joining line string and hexagon
-- traffic lights

CREATE TABLE lights_chbrg AS
SELECT
  hc.nam,
  lights.kname,
  hc.geom
FROM hex_chbrg AS hc
JOIN lichtsignalanlagen AS lights 
ON ST_Intersects(hc.geom,lights.geom); 

--Joining line string and hexagon
-- strassenbelag
CREATE TABLE belag_chbrg AS
SELECT
  hc.nam,
  belag.str_belag,
  hc.geom
FROM hex_chbrg AS hc
JOIN strassenbelag AS belag
ON ST_Intersects(hc.geom,belag.geom); 


-- Union of the layers
-- in QGIS: Vevtor > Geoprocessing > Union 
-- input layer and overlay layer, creating temporary layer, exporting this,

-- importing „union_table“ into sql
-- > Database > DB Manager > PostGIS > select database (e.g. bikeability_index)
--> Import Layer/File >  „union_table“

--refreshing database In Postgres 

-- deleting duplicate columns
ALTER TABLE union_table 
DROP COLUMN nam_2,
DROP COLUMN nam_3;


-- Creating columns for the scores 
--Setting scores for the bike lane type
ALTER TABLE union_table ADD COLUMN radweg_score smallint;
UPDATE union_table
SET radweg_score = CASE 
           WHEN union_table.rva_typ = 'Radweg' THEN 0
           WHEN union_table.rva_typ = 'Radfahrstreifen' THEN 0
           WHEN union_table.rva_typ = 'Schutzstreifen'  THEN 5
		   WHEN union_table.rva_typ = 'Bussonderstreifen'  THEN 10
           ELSE 15
        END;

-- Setting scores for the speed limit 
ALTER TABLE union_table ADD COLUMN tempolimit_score smallint;
UPDATE union_table
SET tempolimit_score = CASE 
           WHEN union_table.wert_ves = 5 THEN 10
           WHEN 5 < union_table.wert_ves AND union_table.wert_ves <= 30 THEN 0
           WHEN 30 < union_table.wert_ves AND union_table.wert_ves <= 50 THEN 15
		   WHEN union_table.wert_ves > 50 THEN 25
           ELSE 15
        END;
		
-- Setting scores for the traffic volume of cars
ALTER TABLE union_table ADD COLUMN cars_score smallint;
UPDATE union_table
SET cars_score = CASE 
           WHEN union_table.dtvw_kfz < 10001 THEN 10
           WHEN 10001 <= union_table.dtvw_kfz AND union_table.dtvw_kfz <= 20000 THEN 15
		   WHEN union_table.dtvw_kfz > 20000 THEN 25
           ELSE 0
        END;
		
-- Setting scores for the traffic volume of trucks
ALTER TABLE union_table ADD COLUMN trucks_score smallint;
UPDATE union_table
SET trucks_score = CASE 
           WHEN union_table.dtvw_lkw < 101 THEN 5
           WHEN 101 <= union_table.dtvw_lkw AND union_table.dtvw_lkw <= 250 THEN 10
		   WHEN union_table.dtvw_lkw > 250 THEN 25
           ELSE 0
        END;


-- Setting scores for the str belag into a score column 
-- and where NULL gets 0 as an asigned score value 
ALTER TABLE union_table ADD COLUMN belag_score smallint;
UPDATE union_table
SET belag_score = CASE 
           WHEN union_table.str_belag = 25 THEN 25
           WHEN union_table.str_belag = 10 THEN 10
           ELSE 0
        END;


-- Adding the scores together in one column    
ALTER TABLE union_table ADD COLUMN bikeability_score real;

UPDATE union_table
SET bikeability_score = (radweg_sco + tempolimit + cars_score + trucks_sco + belag_score);

-- Standardising the bikeability score
ALTER TABLE union_table ADD COLUMN std_bikeability_score real;
UPDATE union_table
-- with max_possible_score = 115
SET std_bikeability_score = bikeability_score / 115;

-- Inverting the bikeability score 
ALTER TABLE union_table ADD COLUMN inv_std_bikeability_score real;
UPDATE union_table
-- with max_possible_score = 115
SET inv_std_bikeability_score = 1 - std_bikeability_score;


-- Refreshing the Postgis Browser in QGIS
-- Inserting union_table into the layers and renaming it to bikeability_index and creating a bikeability index map 

-- Calculating the bikeability index value for the whole district
SELECT AVG(inv_std_bikeability_score) FROM union_table;

—Result: 0.6860248062769353



