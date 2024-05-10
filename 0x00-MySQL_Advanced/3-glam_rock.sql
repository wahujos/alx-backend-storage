--Write a SQL script that lists all bands with Glam rock
-- as their main style, ranked by their longevity
SELECT band_name, IFNULL(2022 - formed, "Still Active") AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY IFNULL(2022 - formed, 2022 - split) DESC;
