import os

cad_path = '/mnt/data/cincinnati/2016-06-20/'
shp_basepath = '/mnt/data/cincinnati/shapefiles/'
shp_info = {'cad_station_areas': (4326, 4326),
            'fire_polygons': (3735, 4326),
            'fire_stations': (3735, 4326),
            'response_areas': (3735, 4326)}
tiger_urls = ['ftp://ftp2.census.gov/geo/tiger/TIGER2013/BG/tl_2013_39_bg.zip',
              'ftp://ftp2.census.gov/geo/tiger/TIGER2013/TRACT/tl_2013_39_tract.zip',
              'ftp://ftp2.census.gov/geo/tiger/TIGER2013/PLACE/tl_2013_39_place.zip']
data_paths = {'info':['/mnt/data/cincinnati/source_files/OPDA_CFD_RESPONSE_TYP_FACT_TBL.xls',
                      '/mnt/data/cincinnati/DSSG/FIREHOUSE EQUIP & LOCATIONS.xls'],
              'sp':['/mnt/data/cincinnati/2016-06-15/SafetyPadCinci1.accdb',
                    '/mnt/data/cincinnati/2016-06-15/SafetyPadCinci2.accdb',
                    '/mnt/data/cincinnati/2016-06-20/SafetyPadCinci3.accdb',
                    '/mnt/data/cincinnati/2016-07-18/Database1.mdb',
                    '/mnt/data/cincinnati/2016-07-18/Database2.mdb',
                    '/mnt/data/cincinnati/2016-07-18/EMS_Analytics.accdb'],
              }

cad_files = []
for f in os.listdir(cad_path):
    if f.endswith(".csv"):
        cad_files.append(cad_path + f)
data_paths['cad'] = cad_files

shp_paths = []
for shpdir in shp_info:
    shp_paths.append(shp_basepath + shpdir)
data_paths['shp'] = shp_paths

# Tables to process as schema:tables dictionary:
tables = {'info': ['unit_dictionary',
                  'cdf_response_typ',
                  'cfd_station_info',
                   ],
          'cad':['dbo_gqlaudit',
                      'dbo_gqlincident',
                      'dbo_iincident',
                      'dbo_iincidentunitsummary',
                      'dbo_rfirehouseapparatus',
                      'dbo_rfirehouseincident',
                      'udt4_idisposition',
                      'udt4_itypeinfo',
                      'udt4_punit'],
          'sp': ['TL_ANSWER',
                 'T_ADDENDUM',
                 'T_AGENCY',
                 'T_AID',
                 'T_ALERT',
                 'T_ALLERGY',
                 'T_ATSCENE',
                 'T_CASE',
                 'T_CAUSE',
                 'T_COMMENT',
                 'T_COMPLAINT',
                 'T_CREW',
                 'T_DELAYS',
                 'T_DESTINATION',
                 'T_EVENTTIME',
                 'T_FINDING',
                 'T_IMPRESSION',
                 'T_INCIDENT',
                 'T_FIREBASIC',
                 'T_LOCATION',
                 'T_MEDICATION',
                 'T_PATIENT',
                 'T_PREEXIST',
                 'T_RESULT',
                 'T_SYMPTOM',
                 'T_TX',
                 'T_TXCATEGORY',
                 'T_TXPROVIDER',
                 'T_TXTYPE',
                 'T_UNIT',
                 'T_USER',
                 'T_VITALS',
                 'dbo_T_CASE',
                 'dbo_T_CAUSE',
                 'dbo_T_COMPLAINT',
                 'dbo_T_CREW',
                 'dbo_T_DESTINATION',
                 'dbo_T_INCIDENT',
                 'dbo_T_EVENTTIME'],
         }

# All Datetime columns for each table for each schema
datetime_columns = {
                    'cad':
                        {'dbo_gqlaudit':['auditdate',
                                         'dt_audittime',
                                         'received_timestamp'],
                         'dbo_gqlincident':[
                                            'time_into_psap',
                                            'pickup_time',
                                            'create_time',
                                            'transmit_time',
                                            'dispatch_time',
                                            'arrival_time',
                                            'closed_time',
                                            'transmit_date',
                                            'dispatch_date',
                                            'closed_date',
                                            'last_modified_timestamp',
                                            'received_timestamp'
                                            ],
                         'dbo_iincident':['i_ttimeintopsap',
                                          'i_ttimepickup',
                                          'i_ttimecreate',
                                          'i_ttimetransmit',
                                          'i_ttimedispatch',
                                          'i_ttimearrival',
                                          'i_ttimeclosed',
                                          'i_ttimelastmodified',
                                          'i_ttimeenroute',
                                          'i_ttimeearliest'],
                      'dbo_iincidentunitsummary':['iiu_tdispatch',
                                                  'iiu_tenroute',
                                                  'iiu_tarrive',
                                                  'iiu_tenroutehospital',
                                                  'iiu_tclear',
                                                  'iiu_tother2',
                                                  'iiu_ttripend'],
                      'dbo_rfirehouseapparatus':['iiu_tdispatch',
                                                 'iiu_tenroute',
                                                 'iiu_tarrive',
                                                 'iiu_tenroutehospital',
                                                 'iiu_tclear'],
                      'dbo_rfirehouseincident':['i_ttimecreate',
                                                'i_ttimedispatch',
                                                'i_ttimearrival',
                                                'i_ttimeclosed']},

                  'sp':
                        {'TL_ANSWER':['STARTDATE',
                                      'ENDDATE',
                                      'LASTUPDATEDDATE'],
                         'T_ADDENDUM':['CREATEDDATE'],
                         'T_AGENCY':[],
                         'T_AID':['EVENTTIME',
                                  'CREATEDDATE'],
                         'T_ALERT':[],
                         'T_ALLERGY':['CREATEDDATE'],
                         'T_ATSCENE':[],
                         'T_CASE':['CREATEDATETIME',
                                   'CREATEDDATE',
                                   'LASTUPDATEDDATE'],
                         'T_CAUSE':['EVENTTIME',
                                    'CREATEDDATE'],
                         'T_COMMENT':['CREATEDDATE'],
                         'T_COMPLAINT':['CREATEDDATE'],
                         'T_CREW':['CREATEDDATE',
                                   'LASTUPDATEDDATE'],
                         'T_DELAYS':['CREATEDDATE'],
                         'T_DESTINATION':['CREATEDDATE'],
                         'T_EVENTTIME':['EVENTTIME','CREATEDDATE'],
                         'T_FINDING':['EVENTTIME','CREATEDDATE'],
                         'T_FIREBASIC':['CREATEDDATE'],
                         'T_IMPRESSION':['CREATEDDATE'],
                         'T_INCIDENT':['CREATEDATETIME',
                                       'CREATEDDATE'],
                         'T_LOCATION':['CREATEDDATE'],
                         'T_MEDICATION':['CREATEDDATE'],
                         'T_PATIENT':['CREATEDDATE'],
                         'T_PREEXIST':['CREATEDDATE'],
                         'T_RESULT':['CREATEDDATE'],
                         'T_SYMPTOM':['CREATEDDATE'],
                         'T_TX':['EVENTTIME',
                                 'CREATEDDATE'],
                         'T_TXCATEGORY':[],
                         'T_TXPROVIDER':['CREATEDDATE'],
                         'T_TXTYPE':[],
                         'T_UNIT':['CREATEDDATE'],
                         'T_USER':[],
                         'T_VITALS':['EVENTTIME',
                                     'CREATEDDATE'],
                         'dbo_T_CASE':['CREATEDDATE',
                                       'LASTUPDATEDDATE'],
                         'dbo_T_CAUSE':['EVENTTIME',
                                        'CREATEDDATE'],
                         'dbo_T_COMPLAINT':['CREATEDDATE'],
                         'dbo_T_CREW':['CREATEDDATE',
                                       'LASTUPDATEDBY'
                                       'LASTUPDATEDDATE'],
                         'dbo_T_DESTINATION':['CREATEDDATE'],
                         'dbo_T_EVENTTIME':['EVENTTIME',
                                            'CREATEDDATE'],
                         'dbo_T_INCIDENT':['CREATEDATETIME',
                                           'CREATEDDATE']
                         }

                }

# Pairwise joints ((table1,table2),(key1,key2))
joins_CAD = [
             (('dbo_iincident','dbo_iincidentunitsummary'),
                 ('i_incident_pk','iiu_kincident')),
             (('dbo_iincident','dbo_gqlincident'),
                 ('i_eventnumber','incidentnumber')),
             (('dbo_iincident','udt4_itypeinfo'),
                 ('i_ktypeinfo','iti_typeinfo_pk')),
             (('dbo_iincident','udt4_punit'),
                 ('i_kprimaryunit','pun_unit_pk')),
             (('dbo_iincident','udt4_idisposition'),
                 ('i_kdisposition1','idi_disposition_pk')),
             (('dbo_iincident','dbo_rfirehouseapparatus'),
                 ('i_eventnumber','i_eventnumber')),
             (('dbo_iincident','dbo_rfirehouseincident'),
                 ('i_eventnumber','i_eventnumber'))
             ]
joins_SP = [
            (('t_incident','t_location'),('KEY_INCIDENT','KEY_INCIDENT')),
            (('t_incident','t_case'),('KEY_INCIDENT','KEY_INCIDENT')),
            (('t_case','t_addendum'),('KEY_CASE','KEY_CASE')),
            (('t_case','t_unit'),('KEY_UNIT','KEY_UNIT')),
            (('t_unit','t_aid'),('KEY_UNIT','KEY_UNIT')),
            (('t_case','t_allergy'),('KEY_CASE','KEY_CASE')),
            (('t_case','t_cause'),('KEY_CASE','KEY_CASE')),
            (('t_case','t_complaint'),('KEY_CASE','KEY_CASE')),
            (('t_case','t_crew'),('KEY_CASE','KEY_CASE')),
            (('t_case','t_delays'),('KEY_CASE','KEY_CASE')),
            (('t_case','t_destination'),('KEY_CASE','KEY_CASE')),
            (('t_case','t_eventtime'),('KEY_CASE','KEY_CASE')),
            (('t_case','t_finding'),('KEY_CASE','KEY_CASE')),
            (('t_case','t_impression'),('KEY_CASE','KEY_CASE')),
            (('t_case','t_medication'),('KEY_CASE','KEY_CASE')),
            (('t_case','t_patient'),('KEY_PATIENT','KEY_PATIENT')),
            (('t_case','t_preexist'),('KEY_CASE','KEY_CASE')),
            (('t_case','t_result'),('KEY_CASE','KEY_CASE')),
            (('t_case','t_symptom'),('KEY_CASE','KEY_CASE')),
            (('t_case','t_tx'),('KEY_CASE','KEY_CASE')),
            (('t_tx','t_txprovider'),('KEY_TX','KEY_TX')),
            (('t_case','t_vitals'),('KEY_CASE','KEY_CASE'))
           ]
orphan_SP = ['t_agency','t_alert','t_atscene','t_txcategory','t_txtype',
             'tl_answer']
