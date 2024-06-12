-- list all brands with 
--Glam Rock as their main style, ranked by there longivity

SELECT  band_name, (IFNULL(split, 2022) - formed) AS lifespan FROM metal_bands WHERE style like '%Glam rock%' ORDER BY lifespan DESC;
