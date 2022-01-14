from Data_Validator.verifier import verify_with_schema
from Log_Writer.logger import App_Logger
class Validator:

    def __init__(self):
        self.schema_path="Data_Schema/schema.json"
        self.log_writer=App_Logger()

    def validate(self,data):
        try :
            err=verify_with_schema(data, self.schema_path)
            if err == 0:
                self.log_writer.log("Data Validation Successfull")
            else :
                self.log_writer.log("ERROR occured in data validation")
            return err

        except Exception as e:
            self.log_writer.log("ERROR occured in data validation")
            return print(e)