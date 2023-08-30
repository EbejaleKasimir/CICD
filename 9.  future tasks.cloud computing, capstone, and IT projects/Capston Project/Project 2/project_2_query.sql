
    CREATE OR REPLACE FUNCTION haversine(
    lat1 float,
    lon1 float,
    lat2 float,
    lon2 float
    ) RETURNS float AS $$
    DECLARE
    x float := 69.1 * (lat2 - lat1);
    y float := 69.1 * (lon2 - lon1) * cos(radians(lat1));
    BEGIN
    RETURN sqrt(x^2 + y^2) * 1.609344;
    END;
    $$ LANGUAGE plpgsql;

ALTER TABLE wpi_data_tbl
    ALTER COLUMN "Latitude_degrees" TYPE bigint,
    ALTER COLUMN "Longitude_degrees" TYPE bigint;
	

    CREATE OR REPLACE FUNCTION haversine(
    lat1 float,
    lon1 float,
    lat2 float,
    lon2 float
    ) RETURNS float AS $$
    DECLARE
    x float := 69.1 * (lat2 - lat1);
    y float := 69.1 * (lon2 - lon1) * cos(radians(lat1));
    BEGIN
    RETURN sqrt(x^2 + y^2) * 1.609344;
    END;
    $$ LANGUAGE plpgsql;

    SELECT
        "Main_port_name" AS port_name, "Latitude_degrees","Longitude_degrees",
        haversine(CAST("Latitude_degrees" AS float),
        CAST("Longitude_degrees" AS float),
        -- Replace these values with a subquery that selects the latitude and longitude for JURONG ISLAND
        (SELECT CAST("Latitude_degrees" AS float) FROM wpi_data_tbl WHERE "Main_port_name" = 'JURONG ISLAND'),
        (SELECT CAST("Longitude_degrees" AS float) FROM wpi_data_tbl WHERE "Main_port_name" = 'JURONG ISLAND')) AS distance_in_kilometers
    FROM
        wpi_data_tbl
    WHERE
        "Main_port_name" <> 'JURONG ISLAND'
    ORDER BY
        distance_in_kilometers
    LIMIT 5;




    SELECT
    "Wpi_country_code" AS country,
    COUNT(*) AS port_count
    FROM
    wpi_data_tbl
    WHERE
    "Load_offload_wharves" = 'Y'
    GROUP BY
    "Wpi_country_code"
    ORDER BY
    port_count DESC
    LIMIT 1;

    SELECT 
        "Wpi_country_code" AS country,
        "Main_port_name" AS port_name, 
        "Latitude_degrees" AS port_latitude,
        "Longitude_degrees" AS port_longitude
    FROM
        wpi_data_tbl
    WHERE
        "Supplies_provisions" = 'Y' AND 
        "Supplies_water" = 'Y' AND
        "Supplies_fuel_oil" = 'Y' AND
        "Supplies_diesel_oil" = 'Y'
    ORDER BY
        (haversine(CAST("Latitude_degrees" AS float),
                CAST("Longitude_degrees" AS float), 
                32.610982, 
                -38.706256))
    LIMIT 1;

