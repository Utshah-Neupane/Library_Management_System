.mode table
.header on


UPDATE BOOK_LOANS
SET 
    Date_Out = STRFTIME('%Y-%m-%d',
               SUBSTR(Date_Out, LENGTH(Date_Out) - 3, 4) || '-' ||
               
               CASE
                   WHEN INSTR(Date_Out, '/') = 2 THEN '0' || SUBSTR(Date_Out, 1, 1)
                   ELSE SUBSTR(Date_Out, 1, INSTR(Date_Out, '/') - 1)
               END || '-' ||
               
               CASE
                   WHEN LENGTH(SUBSTR(Date_Out, INSTR(Date_Out, '/') + 1, INSTR(SUBSTR(Date_Out, INSTR(Date_Out, '/') + 1), '/') - 1)) = 1 THEN
                       '0' || SUBSTR(Date_Out, INSTR(Date_Out, '/') + 1, 1)
                   ELSE
                       SUBSTR(Date_Out, INSTR(Date_Out, '/') + 1, INSTR(SUBSTR(Date_Out, INSTR(Date_Out, '/') + 1), '/') - 1)
               END
    ),

    Due_Date = STRFTIME('%Y-%m-%d',
               
               SUBSTR(Due_Date, LENGTH(Due_Date) - 3, 4) || '-' ||
               
               CASE
                   WHEN INSTR(Due_Date, '/') = 2 THEN '0' || SUBSTR(Due_Date, 1, 1)
                   ELSE SUBSTR(Due_Date, 1, INSTR(Due_Date, '/') - 1)
               END || '-' ||
               
               CASE
                   WHEN LENGTH(SUBSTR(Due_Date, INSTR(Due_Date, '/') + 1, INSTR(SUBSTR(Due_Date, INSTR(Due_Date, '/') + 1), '/') - 1)) = 1 THEN
                       '0' || SUBSTR(Due_Date, INSTR(Due_Date, '/') + 1, 1)
                   ELSE
                       SUBSTR(Due_Date, INSTR(Due_Date, '/') + 1, INSTR(SUBSTR(Due_Date, INSTR(Due_Date, '/') + 1), '/') - 1)
               END
    ),

    Returned_Date = STRFTIME('%Y-%m-%d',
               
               SUBSTR(Returned_Date, LENGTH(Returned_Date) - 3, 4) || '-' ||
               -- Extract Month with Padding
               CASE
                   WHEN INSTR(Returned_Date, '/') = 2 THEN '0' || SUBSTR(Returned_Date, 1, 1)
                   ELSE SUBSTR(Returned_Date, 1, INSTR(Returned_Date, '/') - 1)
               END || '-' ||
               
               CASE
                   WHEN LENGTH(SUBSTR(Returned_Date, INSTR(Returned_Date, '/') + 1, INSTR(SUBSTR(Returned_Date, INSTR(Returned_Date, '/') + 1), '/') - 1)) = 1 THEN
                       '0' || SUBSTR(Returned_Date, INSTR(Returned_Date, '/') + 1, 1)
                   ELSE
                       SUBSTR(Returned_Date, INSTR(Returned_Date, '/') + 1, INSTR(SUBSTR(Returned_Date, INSTR(Returned_Date, '/') + 1), '/') - 1)
               END
    );



SELECT 
	(SELECT COUNT(*) FROM PUBLISHER) AS PUBLISHER,

	(SELECT COUNT(*) FROM LIBRARY_BRANCH) AS LIBRARY_BRANCH,

	(SELECT COUNT(*) FROM BORROWER) AS BORROWER,

	(SELECT COUNT(*) FROM BOOK) AS BOOK,

	(SELECT COUNT(*) FROM BOOK_LOANS) AS BOOK_LOANS,

	(SELECT COUNT(*) FROM BOOK_COPIES) AS BOOK_COPIES,

	(SELECT COUNT(*) FROM BOOK_AUTHORS) AS BOOK_AUTHORS;









