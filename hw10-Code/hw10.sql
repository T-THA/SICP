.read hw10_data.sql

-- The size of each dog
CREATE TABLE size_of_dogs AS
  SELECT name,size  FROM dogs,sizes WHERE height>min AND height <=max;


-- All dogs with parents ordered by decreasing height of their parent
CREATE TABLE by_parent_height AS
  SELECT child AS name FROM dogs,parents WHERE parent = name ORDER BY height DESC;


-- Sentences about siblings that are the same size
CREATE TABLE sentences AS
  SELECT  "The two siblings, " || a.name || " plus "|| b.name || " have the same size: " || a.size 
  FROM size_of_dogs AS a, size_of_dogs AS b, parents as c, parents as d 
  WHERE a.name != b.name 
  AND a.size = b.size 
  AND a.name<b.name 
  AND c.parent=d.parent
  AND c.child=a.name
  AND d.child=b.name
  ORDER BY a.size;
