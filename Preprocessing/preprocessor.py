from Log_Writer.logger import App_Logger
from Preprocessing.null_imputer import null_value_imputer
from Preprocessing.categ_encoding import encode
from Preprocessing.normalizer import normalize

class Preprocessor:

    def __init__(self):
        self.log_writer=App_Logger()

    def preprocess(self,data):
        try:
            data=encode(data)
            data=null_value_imputer(data)
            data=normalize(data)
            self.log_writer.log("Data Preprocessing Completed Successfully\n\n")
            return data

        except Exception as e:
            self.log_writer.log("\nERROR occured while preprocessing data\n")
            return print(e)