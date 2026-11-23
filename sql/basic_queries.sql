-- Überblick
SELECT * FROM weather_data

-- Welche Bundesländer sind durchschnittlich am wärmsten
SELECT bundesland, ROUND(AVG(temperatur)::numeric, 2) AS temperatur
FROM weather_data
GROUP BY bundesland
ORDER BY temperatur DESC

--Welche Bundesländer liegen über dem Deutschland Durchschnitt
SELECT bundesland, ROUND(AVG(temperatur)::numeric, 2) AS avg_temp
FROM weather_data
GROUP BY bundesland
HAVING AVG(temperatur)>=(SELECT AVG(temperatur) FROM weather_data
					WHERE bundesland='Deutschland')

-- Welche Monate sind im Durchschnitt am wärmsten
SELECT monat, ROUND(AVG(temperatur)::numeric,2) as avg_temp
FROM weather_data
GROUP BY monat
ORDER BY avg_temp DESC

-- Welche Jahre waren wärmer als der durchschnitt aller Jahre
SELECT jahr, ROUND(AVG(temperatur)::numeric,2) as avg_temp
FROM weather_data
GROUP BY jahr
HAVING AVG(temperatur) > (SELECT AVG(temperatur) FROM weather_data WHERE bundesland='Deutschland')
ORDER BY avg_temp DESC

--Wärmsten Jahre Deutschlands & kälteste (einfach ohne DESC)
SELECT jahr, ROUND(AVG(temperatur)::numeric,2) as avg_temp
FROM weather_data
WHERE bundesland ='Deutschland'
GROUP BY jahr
ORDER BY avg_temp DESC

-- Temperaturtrend der letzten 20 Jahre
SELECT
jahr,
ROUND(AVG(temperatur)::numeric,2) AS avg_temp
FROM weather_data
WHERE bundesland = 'Deutschland'
AND jahr >= 2000
GROUP BY jahr
ORDER BY jahr

-- Temperaturtrend nach Jahrzenten
SELECT
    (jahr / 10) * 10 AS decade,
    ROUND(AVG(temperatur)::numeric,2) AS avg_temp
FROM weather_data
WHERE bundesland = 'Deutschland'
GROUP BY decade
ORDER BY decade


--Durchschnitts Temperatur pro Monat und Bundesland
SELECT
    monat,
    bundesland,
    ROUND(AVG(temperatur)::numeric,2) AS avg_temp
FROM weather_data
GROUP BY monat, bundesland
ORDER BY monat, avg_temp DESC