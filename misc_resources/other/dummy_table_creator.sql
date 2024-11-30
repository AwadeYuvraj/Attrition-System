CREATE TABLE dummy_data (
	id_col SERIAL PRIMARY KEY,
	int_col	INT,
	float_col FLOAT,
	string_col VARCHAR,
	bool_col BOOLEAN,
	na_col VARCHAR,
	time_col timestamptz,
	latitude_col FLOAT,
	longitude_col FLOAT
);