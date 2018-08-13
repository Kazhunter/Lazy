# Extract Insertion Queries From Excel File

Pre-requiset : 
 - install numpy and pandas lib 
 
How to use : 
  - Excel File : 
       * sheet name represent table in Database Name 
       * First row in sheet represent columns names in DB 
       * each row next is record in table 
  - Demo.py 
       * you will find 2 main variables in the begining of the script  
       * input_excel_path : full path for excel file
       * output_folder_path : full path of directory you need to generate in 
       
       
General Info :
 - This Script generate each table alone in the order of the sheets 
 - You can modified it to generate then in one big file 
 - Each file generate there is pre-fix at in file name which is the order 
   of the sheet so make sure that you take care of dependancy of your insertion queries 
 - After generation you will find list of sql files which can be easly run to your DB " you can write script to run all of them 
   such 'psql -U username -d myDataBase -a -f myInsertFile' this for postgres DB"
   
   
   
   
