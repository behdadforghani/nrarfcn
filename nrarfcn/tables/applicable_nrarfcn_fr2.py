from tables.Table import Table


def table_applicable_nrarfcn_fr2() -> Table:
    table_id = 'applicable_nrarfcn_fr2'
    table_release_3gpp = 17
    table_ts = "3GPP TS 38.104 V17.6.0"
    table_name = "Table 5.4.2.3-2: Applicable NR-ARFCN per operating band in FR2"
    table_header = ['band', 'f_raster', 'ul_first', 'ul_step', 'ul_last', 'dl_first', 'dl_step', 'dl_last']
    table_data = [
        ['n257', 60, 2054166, 1, 2104165, 2054166, 1, 2104165],
        ['n257', 120, 2054167, 2, 2104165, 2054167, 2, 2104165],
        ['n258', 60, 2016667, 1, 2070832, 2016667, 1, 2070832],
        ['n258', 120, 2016667, 2, 2070831, 2016667, 2, 2070831],
        ['n259', 60, 2270833, 1, 2337499, 2270833, 1, 2337499],
        ['n259', 120, 2270833, 2, 2337499, 2270833, 2, 2337499],
        ['n260', 60, 2229166, 1, 2279165, 2229166, 1, 2279165],
        ['n260', 120, 2229167, 2, 2279165, 2229167, 2, 2279165],
        ['n261', 60, 2070833, 1, 2084999, 2070833, 1, 2084999],
        ['n261', 120, 2070833, 2, 2084999, 2070833, 2, 2084999],
        ['n262', 60, 2399166, 1, 2415832, 2399166, 1, 2415832],
        ['n262', 120, 2399167, 2, 2415831, 2399167, 2, 2415831],
        ['n263', 120, 2564083, 1680, 2794243, 2564083, 1680, 2794243],
        ['n263', 480, 2566603, 6720, 2788363, 2566603, 6720, 2788363],
        ['n263', 960, 2566603, 6720, 2788363, 2566603, 6720, 2788363]
    ]
    #  refer to 3GPP TS38.104 v17.6.0 tables 5.3.5-3 5.4.2.3-3 for n263 info

    return Table(table_id, table_release_3gpp, table_ts, table_name, table_header, table_data)
