from Log_Writer.logger import App_Logger
from sklearn.preprocessing import FunctionTransformer
import pandas as pd
import numpy as np

def normalize(data):
    log_writer = App_Logger()
    try:
        num_index=["Line_Item_Quantity","Pack Price","Weight (Kilograms)", "Freight Cost (USD)","Line_Item_Insurance","item_value"]
        func = FunctionTransformer(np.log1p)
        trans = func.fit_transform(data[num_index])

        data[num_index]=trans
        log_writer.log(log_message="Data normalization Completed Successfully")
        return data

    except Exception as e:
        log_writer.log(log_message="\nERROR occurred in normalizing data\n")
        return print(e)