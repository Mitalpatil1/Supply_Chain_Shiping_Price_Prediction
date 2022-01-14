from Log_Writer.logger import App_Logger
import pandas as pd


def format(data):
    log_writer = App_Logger()
    try:
        log_writer.log(log_message="Converting raw data to DataFrame")

        data = pd.DataFrame(data=data, columns=['Country', 'Manufacturing_Site', 'Brand', 'Item_Description'
            , 'Product_Group', 'Sub_Classification', 'Molecule_Test_Type'
            , 'Dosage_Form', 'Dosage', 'Managed_By', 'Fulfill_Via', 'Shipment_Mode'
            , 'dlvry_delay', 'dlvry_verif_time_delay', 'Unit of Measure (Per Pack)'
            , 'Line_Item_Quantity', 'Pack Price', 'Unit Price', 'First_Line_Designation'
            , 'Weight (Kilograms)', 'Freight Cost (USD)', 'Freight_cost_special', 'Line_Item_Insurance'
            , 'item_value'])

        log_writer.log(log_message="Converted Raw Data to DataFrame")
        return data

    except Exception as e:
        log_writer.log(log_message="ERROR occured in converting Raw Data to DataFrame")
        return print(e)
