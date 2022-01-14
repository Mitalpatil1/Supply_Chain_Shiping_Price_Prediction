from Log_Writer.logger import App_Logger

def find_null_cols(data):
    log_writer=App_Logger()
    try:
        null_val_cols = (data.isnull().sum()[data.isnull().sum() > 0]).index
        log_writer.log("Successfully fould columns with null values")
        return null_val_cols
    except Exception as e :
        return print(e)
