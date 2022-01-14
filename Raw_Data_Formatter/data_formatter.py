from Log_Writer.logger import App_Logger
from Raw_Data_Formatter import aggregator
from Raw_Data_Formatter import format

class formatter:

    def __init__(self):
        self.log_writer=App_Logger()

    def format_data(self):
        try:
            raw_data = aggregator.aggregate_data()
            data = format.format(raw_data)
            self.log_writer.log(log_message="Formatted Data Successfully")
            return data

        except Exception as e:
            self.log_writer.log(log_message="ERROR in Data Formatting")
            return print(e)



