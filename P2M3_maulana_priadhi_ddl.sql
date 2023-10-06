-- Membuat tabel yang diinginkan--
CREATE TABLE table_M3
	("Id" INTEGER PRIMARY KEY, 
	 "age" INTEGER, 
	 "job" VARCHAR(50), 
	 "marital" VARCHAR(50),
     "education" VARCHAR(50), 
	 "default" VARCHAR(50), 
	 "balance" INTEGER,
     "housing" VARCHAR(50), 
	 "loan" VARCHAR(50), 
	 "contact" VARCHAR(50), 
	 "day" INTEGER,
     "month" VARCHAR(50), 
	 "duration" INTEGER, 
	 "campaign" INTEGER,
	 "pdays" INTEGER,
     "previous" INTEGER, 
	 "poutcome" VARCHAR(50), 
	 "y" VARCHAR(50));
	 
--copy csv kedalam postgress--	 
COPY table_M3("Id", "age", "job", "marital", "education", "default", "balance",
        "housing", "loan", "contact", "day", "month", "duration", "campaign", 
		"pdays", "previous", "poutcome", "y")
FROM  '"C:\temp\P2M3_maulana_priadhi_data_raw.csv"' 

DELIMITER ','
CSV HEADER;

SELECT * FROM table_M3