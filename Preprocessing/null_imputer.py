from Log_Writer.logger import App_Logger
from sklearn.impute import KNNImputer
from Preprocessing.null_col_finder import find_null_cols
import pandas as pd


def null_value_imputer(data):
    log_writer = App_Logger()
    try:
        clean_data = pd.read_csv('Cleaned_shipment_data.csv')

        # getting columns with null values
        null_cols = find_null_cols(data)

        for col in null_cols:
            """clean_col=col
            if col=="Unit_of_measure":
                clean_col='Unit of Measure (Per Pack)'
            if col=="Pack_Price":
                clean_col="Pack Price"
            if col=="Unit_Price":
                clean_col="Unit Price"
            if col=="Weight":
                clean_col='Weight (Kilograms)'
            if col=="Freight_Cost":
                clean_col='Freight Cost (USD)'"""

            imputer = KNNImputer(n_neighbors=10)
            imputer.fit(clean_data[[col]])
            data[col] = imputer.transform(data[[col]])

        log_writer.log(log_message="Null Value Imputation Completed Successfully")
        return data
    except Exception as e:
        log_writer.log(log_message="\nERROR occurred in null value imputation\n")
        return print(e)
