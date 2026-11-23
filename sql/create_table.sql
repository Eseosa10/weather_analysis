CREATE TABLE weather_data (
    jahr SMALLINT NOT NULL
        CHECK (jahr BETWEEN 1700 AND 2200),

    monat SMALLINT NOT NULL
        CHECK (monat BETWEEN 1 AND 12),

    bundesland TEXT NOT NULL,

    temperatur DOUBLE PRECISION,

    PRIMARY KEY (
        jahr,
        monat,
        bundesland
    )
);