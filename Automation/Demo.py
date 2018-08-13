import numpy as np
import pandas

output_folder_path = "/home/kazhunter/PycharmProjects/InsertionQuery/Lazy/Lazy/Automation/"
input_excel_path = '/home/kazhunter/PycharmProjects/InsertionQuery/Lazy/Lazy/Automation/test.xlsx'


def to_str(var):
    return str(list(np.reshape(np.asarray(var), (1, np.size(var)))[0]))[1:-1]


def write_queries_to_file(file_path, queries_list):
    file = open(file_path, "w")
    for currentQuery in queries_list:
        file.write(currentQuery)
        file.write("\n\n")
    file.close()


def get_columns_names(insertion_query, excel_file):
    for column_name in excel_file.columns:
        if column_name == excel_file.columns[-1]:
            insertion_query += column_name
        else:
            insertion_query += column_name + ", "
    return insertion_query


def get_columns_values(insertion_query, excel_file):
    for columnsName in excel_file.columns:
        column_value = excel_file[columnsName][currentRowIndex]
        if columnsName == excel_file.columns[-1]:
            insertion_query += to_str(column_value)
        else:
            insertion_query += to_str(column_value) + ", "
    return insertion_query


excelFileMetaData = pandas.ExcelFile(input_excel_path)

insertionQueries = []
insertionQuery = "INSERT INTO "


def create_save_file_name(output_folder_path, table_name):
    return output_folder_path + to_str(excelFileMetaData.sheet_names.index(table_name)) + "_" + table_name + ".txt"


for tableName in excelFileMetaData.sheet_names:
    excelFile = pandas.read_excel(input_excel_path, tableName)

    for currentRowIndex in range(excelFile[excelFile.columns[0]].size):
        insertionQuery = "INSERT INTO " + tableName + " ("

        insertionQuery = get_columns_names(insertionQuery, excelFile)

        insertionQuery += " )" + " VALUES ("

        insertionQuery = get_columns_values(insertionQuery, excelFile)

        insertionQuery += ");"

        insertionQueries.append(insertionQuery)

    write_queries_to_file(create_save_file_name(output_folder_path, tableName), insertionQueries)
    insertionQueries = []
