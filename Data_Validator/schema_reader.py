import json
from Log_Writer.logger import App_Logger

def load_schema(path):
    log_writer=App_Logger()
    try:
        schema = open(path, 'r')
        schema_dic = json.load(schema)
        schema.close()
        col_length = schema_dic["column_length"]
        col_names = schema_dic["col_names"]
        dtypes = schema_dic["dtypes"]
        log_writer.log("Extracted column length and column names from schema")

        return col_length, col_names, dtypes
    except Exception as e:
        log_writer.log("ERROR occured while extracting schema information")
        print(e)