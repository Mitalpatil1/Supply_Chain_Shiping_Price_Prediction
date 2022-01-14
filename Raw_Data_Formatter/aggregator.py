from Log_Writer.logger import App_Logger
from flask import request
import numpy as np


def aggregate_data():
    log_writer = App_Logger()
    try:

        Country = request.form['Country']
        Manufacturing_Site = request.form['Manufacturing Site']
        Brand = request.form['Brand']
        Item_Description = request.form['Item Description']
        Product_Group = request.form['Product Group']
        Sub_Classification = request.form['Sub Classification']
        Molecule_Test_Type = request.form['Molecule/Test Type']
        Dosage_Form = request.form['Dosage Form']
        Dosage = request.form['Dosage']
        Managed_By = request.form['Managed By']
        Fulfill_Via = int(request.form['Fulfill Via'])
        Shipment_Mode = request.form['Shipment Mode']

        if request.form['dlvry_delay'] == "":
            dlvry_delay = np.nan
        else:
            dlvry_delay = float(request.form['dlvry_delay'])

        if request.form['dlvry_verif_time_delay'] == "":
            dlvry_verif_time_delay = np.nan
        else:
            dlvry_verif_time_delay = float(request.form['dlvry_verif_time_delay'])

        if request.form['Unit of Measure (Per Pack)'] == "":
            Unit_of_measure = np.nan
        else:
            Unit_of_measure = float(request.form['Unit of Measure (Per Pack)'])

        if request.form['Line Item Quantity'] == "":
            Line_Item_Quantity = np.nan
        else:
            Line_Item_Quantity = float(request.form['Line Item Quantity'])

        if request.form['Pack Price'] == "":
            Pack_Price = np.nan
        else:
            Pack_Price =float(request.form['Pack Price'])

        if request.form['Unit Price'] == "":
            Unit_Price = np.nan
        else:
            Unit_Price = float(request.form['Unit Price'])

        First_Line_Designation = int(request.form['First Line Designation'])

        if request.form['Weight (Kilograms)'] == "":
            Weight = np.nan
        else:
            Weight = float(request.form['Weight (Kilograms)'])

        if request.form['Freight Cost (USD)'] == "":
            Freight_Cost = np.nan
        else:
            Freight_Cost = float(request.form['Freight Cost (USD)'])

        Freight_cost_special = request.form['Freight_cost_special']

        if request.form['Line Item Insurance (USD)'] == "":
            Line_Item_Insurance = np.nan
        else:
            Line_Item_Insurance = float(request.form['Line Item Insurance (USD)'])

        if request.form['Line Item Value'] == "":
            Line_Item_Value = np.nan
        else:
            Line_Item_Value = float(request.form['Line Item Value'])

        item_value = (Line_Item_Value + Line_Item_Insurance) / Line_Item_Quantity

        log_writer.log(log_message="Collected inputs from HTML form")

        data = [[Country,Manufacturing_Site,Brand,Item_Description
                 ,Product_Group,Sub_Classification,Molecule_Test_Type
                 ,Dosage_Form,Dosage,Managed_By,Fulfill_Via,Shipment_Mode
                 ,dlvry_delay,dlvry_verif_time_delay,Unit_of_measure
                 ,Line_Item_Quantity,Pack_Price,Unit_Price,First_Line_Designation
                 ,Weight,Freight_Cost,Freight_cost_special,Line_Item_Insurance
                 ,item_value]]

        log_writer.log(log_message="Aggregated data inputs from HTML form")
        return data

    except Exception as e:
        log_writer.log(log_message="ERROR occured in Data Collection and Aggregation")
        return print(e)
