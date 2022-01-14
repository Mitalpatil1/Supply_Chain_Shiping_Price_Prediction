from Log_Writer.logger import App_Logger

def encode(data):
    log_writer=App_Logger()
    try:
        country_map = {'Other': 80, 'South Africa': 1406, 'Nigeria': 1194, "Côte d'Ivoire": 1083, 'Uganda': 779,
                       'Vietnam': 688, 'Zambia': 683, 'Haiti': 655, 'Mozambique': 631, 'Zimbabwe': 538}
        data.Country = data.Country.map(country_map)

        manuf_site_map = {'Aurobindo Unit III, India': 3172, 'Other': 2, 'Mylan (formerly Matrix) Nashik': 1415,
                          'Hetero Unit III Hyderabad IN': 869, 'Cipla, Goa, India': 665,
                          'Strides, Bangalore, India': 540,
                          'Alere Medical Co., Ltd.': 481, 'Trinity Biotech, Plc': 405,
                          'ABBVIE Ludwigshafen Germany': 366,
                          'Inverness Japan': 345}
        data["Manufacturing_Site"] = data["Manufacturing_Site"].map(manuf_site_map)

        brand_map = {'Generic': 7285, 'Other': 5, 'Determine': 799, 'Uni-Gold': 373, 'Aluvia': 250, 'Kaletra': 165,
                     'Norvir': 136,
                     'Stat-Pak': 115, 'Bioline': 113, 'Truvada': 94}
        data.Brand = data.Brand.map(brand_map)

        item_map = {'Other': 1, 'Efavirenz 600mg, tablets, 30 Tabs': 755, 'Nevirapine 200mg, tablets, 60 Tabs': 623,
                    'Lamivudine/Zidovudine 150/300mg, tablets, 60 Tabs': 597,
                    'Lamivudine/Nevirapine/Zidovudine 150/200/300mg, tablets, 60 Tabs': 580,
                    'HIV 1/2, Determine Complete HIV Kit, 100 Tests': 577, 'Lamivudine 150mg, tablets, 60 Tabs': 378,
                    'HIV 1/2, Uni-Gold HIV Kit, 20 Tests': 369, 'Zidovudine 300mg, tablets, 60 Tabs': 317,
                    'Lamivudine/Tenofovir Disoproxil Fumarate 300/300mg, tablets, 30 Tabs': 301}
        data["Item_Description"] = data["Item_Description"].map(item_map)

        prod_group_map = {'ARV': 8550, 'HRDT': 1728, 'ANTM': 22, 'ACT': 16, 'MRDT': 8}
        data["Product_Group"] = data['Product_Group'].map(prod_group_map)

        sub_class_map = {'Adult': 6595, 'Pediatric': 1955, 'HIV test': 1567, 'HIV test - Ancillary': 161, 'Malaria': 30,
                         'ACT': 16}
        data['Sub_Classification'] = data['Sub_Classification'].map(sub_class_map)

        test_type_map = {'Other': 5,
                         'Efavirenz': 1125,
                         'Nevirapine': 877,
                         'Lamivudine/Nevirapine/Zidovudine': 707,
                         'Lamivudine/Zidovudine': 689,
                         'Lopinavir/Ritonavir': 633,
                         'Lamivudine': 592,
                         'HIV 1/2, Determine Complete HIV Kit': 577,
                         'Zidovudine': 529,
                         'Abacavir': 453,
                         'HIV 1/2, Uni-Gold HIV Kit': 37}
        data["Molecule_Test_Type"] = data["Molecule_Test_Type"].map(test_type_map)

        dosage_form_map = {'Tablet': 3532,
                           'Tablet - FDC': 2749,
                           'Test kit': 1575,
                           'Capsule': 729,
                           'Oral solution': 727,
                           'Chewable/dispersible tablet - FDC': 239,
                           'Oral suspension': 214,
                           'Test kit - Ancillary': 161,
                           'Chewable/dispersible tablet': 146,
                           'Delayed-release capsules': 131,
                           'Other': 121}
        data['Dosage_Form'] = data['Dosage_Form'].map(dosage_form_map)

        dosage_map = {'Other': 2,
                      '300mg': 1188,
                      '200mg': 1115,
                      '600mg': 926,
                      '150/300mg': 720,
                      '150/300/200mg': 686,
                      '10mg/ml': 671,
                      '150mg': 515,
                      '200/50mg': 475,
                      '300/300mg': 367
                      }
        data.Dosage = data.Dosage.map(dosage_map)

        managed_by_map = {'PMO - US': 10265,
                          'South Africa Field Office': 57,
                          'Haiti Field Office': 1,
                          'Ethiopia Field Office': 1}
        data['Managed_By'] = data['Managed_By'].map(managed_by_map)

        shipment_mode_map = {'Air': 6334, 'Truck': 2930, 'Air Charter': 671, 'Ocean': 389}
        data['Shipment_Mode'] = data['Shipment_Mode'].map(shipment_mode_map)

        freight_spcl_map = {'Normal Measurement': 6198,
                            'See ASN/DN Tag': 2445,
                            'Freight Included in Commodity Cost': 1442,
                            'Invoiced Separately': 239}
        data['Freight_cost_special'] = data['Freight_cost_special'].map(freight_spcl_map)

        log_writer.log("Encoded all categorical columns successfully")
        return data

    except Exception as e:
        log_writer.log("\nError Occurred while Encoding Columns\n")
        return print(e)



