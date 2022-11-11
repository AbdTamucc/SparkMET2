import copy
import time
import calendar
import netCDF4
import numpy
import statistics as st 
from numpy import savez_compressed
from numpy import load
import pandas
import scipy.ndimage
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
import seaborn as sns
import os.path
import itertools
import pandas as pd
plt.rcParams.update({'axes.titlesize': 14})
plt.rc('xtick', labelsize=12)    # fontsize of the tick labels
plt.rc('ytick', labelsize=12)    # fontsize of the tick labels
plt.rc('axes', labelsize=14)     # fontsize of the x and y labels 




MUR_coords = {'P3': [246, 115], 
'P4': [225, 145]} 

NAM_coords = {'P1':[23, 6],
         'P2':[22, 8],
         'P3':[21, 10],
         'P4':[19, 12]} 


# Variable names.
NETCDF_X = 'x'
NETCDF_Y = 'y'
MUR_LATITUDE = 'lat'
MUR_LONGITUDE = 'lon'
NETCDF_LATITUDE = 'latitude'
NETCDF_LONGITUDE = 'longitude'
NETCDF_TIME = 'time'


NETCDF_UGRD_10m   = 'UGRD_10maboveground'
#NETCDF_UGRD_1000mb= 'UGRD_1000mb'
NETCDF_UGRD_975mb = 'UGRD_975mb'
NETCDF_UGRD_950mb = 'UGRD_950mb'
NETCDF_UGRD_925mb = 'UGRD_925mb'
NETCDF_UGRD_900mb = 'UGRD_900mb'
NETCDF_UGRD_875mb = 'UGRD_875mb'
NETCDF_UGRD_850mb = 'UGRD_850mb'
NETCDF_UGRD_825mb = 'UGRD_825mb'
NETCDF_UGRD_800mb = 'UGRD_800mb'
NETCDF_UGRD_775mb = 'UGRD_775mb'
NETCDF_UGRD_750mb = 'UGRD_750mb'
NETCDF_UGRD_725mb = 'UGRD_725mb'
NETCDF_UGRD_700mb = 'UGRD_700mb'
NETCDF_VGRD_10m   = 'VGRD_10maboveground'
#NETCDF_VGRD_1000mb= 'VGRD_1000mb'
NETCDF_VGRD_975mb = 'VGRD_975mb'
NETCDF_VGRD_950mb = 'VGRD_950mb'
NETCDF_VGRD_925mb = 'VGRD_925mb'
NETCDF_VGRD_900mb = 'VGRD_900mb'
NETCDF_VGRD_875mb = 'VGRD_875mb'
NETCDF_VGRD_850mb = 'VGRD_850mb'
NETCDF_VGRD_825mb = 'VGRD_825mb'
NETCDF_VGRD_800mb = 'VGRD_800mb'
NETCDF_VGRD_775mb = 'VGRD_775mb'
NETCDF_VGRD_750mb = 'VGRD_750mb'
NETCDF_VGRD_725mb = 'VGRD_725mb'
NETCDF_VGRD_700mb = 'VGRD_700mb'
#NETCDF_VVEL_1000mb= 'VVEL_1000mb'
NETCDF_VVEL_975mb = 'VVEL_975mb'
NETCDF_VVEL_950mb = 'VVEL_950mb'
NETCDF_VVEL_925mb = 'VVEL_925mb'
NETCDF_VVEL_900mb = 'VVEL_900mb'
NETCDF_VVEL_875mb = 'VVEL_875mb'
NETCDF_VVEL_850mb = 'VVEL_850mb'
NETCDF_VVEL_825mb = 'VVEL_825mb'
NETCDF_VVEL_800mb = 'VVEL_800mb'
NETCDF_VVEL_775mb = 'VVEL_775mb'
NETCDF_VVEL_750mb = 'VVEL_750mb'
NETCDF_VVEL_725mb = 'VVEL_725mb'
NETCDF_VVEL_700mb = 'VVEL_700mb'
#NETCDF_TKE_1000mb = 'TKE_1000mb'
NETCDF_TKE_975mb = 'TKE_975mb'
NETCDF_TKE_950mb = 'TKE_950mb'
NETCDF_TKE_925mb = 'TKE_925mb'
NETCDF_TKE_900mb = 'TKE_900mb'
NETCDF_TKE_875mb = 'TKE_875mb'
NETCDF_TKE_850mb = 'TKE_850mb'
NETCDF_TKE_825mb = 'TKE_825mb'
NETCDF_TKE_800mb = 'TKE_800mb'
NETCDF_TKE_775mb = 'TKE_775mb'
NETCDF_TKE_750mb = 'TKE_750mb'
NETCDF_TKE_725mb = 'TKE_725mb'
NETCDF_TKE_700mb = 'TKE_700mb'
NETCDF_TMP_SFC  = 'TMP_surface'
NETCDF_TMP_2m    = 'TMP_2maboveground'
#NETCDF_TMP_1000mb= 'TMP_1000mb'
NETCDF_TMP_975mb = 'TMP_975mb'
NETCDF_TMP_950mb = 'TMP_950mb'
NETCDF_TMP_925mb = 'TMP_925mb'
NETCDF_TMP_900mb = 'TMP_900mb'
NETCDF_TMP_875mb = 'TMP_875mb'
NETCDF_TMP_850mb = 'TMP_850mb'
NETCDF_TMP_825mb = 'TMP_825mb'
NETCDF_TMP_800mb   = 'TMP_800mb'
NETCDF_TMP_775mb   = 'TMP_775mb'
NETCDF_TMP_750mb   = 'TMP_750mb'
NETCDF_TMP_725mb   = 'TMP_725mb'
NETCDF_TMP_700mb   = 'TMP_700mb'
#NETCDF_RH_1000mb = 'RH_1000mb'
NETCDF_RH_975mb    = 'RH_975mb'
NETCDF_RH_950mb    = 'RH_950mb'
NETCDF_RH_925mb    = 'RH_925mb'
NETCDF_RH_900mb    = 'RH_900mb'
NETCDF_RH_875mb    = 'RH_875mb'
NETCDF_RH_850mb    = 'RH_850mb'
NETCDF_RH_825mb    = 'RH_825mb'
NETCDF_RH_800mb    = 'RH_800mb'
NETCDF_RH_775mb    = 'RH_775mb'
NETCDF_RH_750mb    = 'RH_750mb'
NETCDF_RH_725mb    = 'RH_725mb'
NETCDF_RH_700mb    = 'RH_700mb'
NETCDF_DPT_2m      = 'DPT_2maboveground'
NETCDF_FRICV       = 'FRICV_surface'
NETCDF_VIS         = 'VIS_surface'
NETCDF_RH_2m       = 'RH_2maboveground'
#
NETCDF_Q975        = 'Q_975mb'
NETCDF_Q950        = 'Q_950mb'
NETCDF_Q925        = 'Q_925mb'
NETCDF_Q900        = 'Q_900mb'
NETCDF_Q875        = 'Q_875mb'
NETCDF_Q850        = 'Q_850mb'
NETCDF_Q825        = 'Q_825mb'
NETCDF_Q800        = 'Q_800mb'
NETCDF_Q775        = 'Q_775mb'
NETCDF_Q750        = 'Q_750mb'
NETCDF_Q725        = 'Q_725mb'
NETCDF_Q700        = 'Q_700mb'
NETCDF_Q           = 'Q_surface'
#NETCDF_DQDZ1000SFC = 'DQDZ1000SFC'
NETCDF_DQDZ975SFC  = 'DQDZ975SFC'
NETCDF_DQDZ950975  = 'DQDZ950975'
NETCDF_DQDZ925950  = 'DQDZ925950'
NETCDF_DQDZ900925  = 'DQDZ900925'
NETCDF_DQDZ875900  = 'DQDZ875900'
NETCDF_DQDZ850875  = 'DQDZ850875'
NETCDF_DQDZ825850  = 'DQDZ825850'
NETCDF_DQDZ800825  = 'DQDZ800825'
NETCDF_DQDZ775800  = 'DQDZ775800'
NETCDF_DQDZ750775  = 'DQDZ750775'
NETCDF_DQDZ725750  = 'DQDZ725750'
NETCDF_DQDZ700725  = 'DQDZ700725'
NETCDF_LCLT        = 'LCLT'

#+++++++++++++++
NETCDF_SST    = 'analysed_sst'
NETCDF_TMPDPT = 'TMP-DPT'
NETCDF_TMPSST = 'TMP-SST'
NETCDF_DPTSST = 'DPT-SST'


NETCDF_PREDICTOR_NAMES = {
    'All': [NETCDF_TMP_2m, NETCDF_TMP_975mb, NETCDF_TMP_950mb, NETCDF_TMP_925mb, NETCDF_TMP_900mb, NETCDF_TMP_875mb, NETCDF_TMP_850mb, 
    NETCDF_TMP_825mb, NETCDF_TMP_800mb, NETCDF_TMP_775mb, NETCDF_TMP_750mb, NETCDF_TMP_725mb, NETCDF_TMP_700mb, 
    NETCDF_UGRD_10m, NETCDF_VGRD_10m, NETCDF_FRICV, NETCDF_UGRD_975mb, NETCDF_VGRD_975mb, NETCDF_TKE_975mb,
    NETCDF_UGRD_950mb, NETCDF_VGRD_950mb, NETCDF_TKE_950mb, NETCDF_UGRD_925mb, NETCDF_VGRD_925mb, NETCDF_TKE_925mb, NETCDF_UGRD_900mb, NETCDF_VGRD_900mb,
    NETCDF_TKE_900mb, NETCDF_UGRD_875mb, NETCDF_VGRD_875mb, NETCDF_TKE_875mb, NETCDF_UGRD_850mb, NETCDF_VGRD_850mb, NETCDF_TKE_850mb, NETCDF_UGRD_825mb,
    NETCDF_VGRD_825mb, NETCDF_TKE_825mb, NETCDF_UGRD_800mb, NETCDF_VGRD_800mb, NETCDF_TKE_800mb, NETCDF_UGRD_775mb, NETCDF_VGRD_775mb,
    NETCDF_TKE_775mb, NETCDF_UGRD_750mb, NETCDF_VGRD_750mb, NETCDF_TKE_750mb, NETCDF_UGRD_725mb, NETCDF_VGRD_725mb, NETCDF_TKE_725mb,
    NETCDF_UGRD_700mb,  NETCDF_VGRD_700mb, NETCDF_TKE_700mb, NETCDF_Q975, NETCDF_Q950, NETCDF_Q925, NETCDF_Q900, NETCDF_Q875, NETCDF_Q850,
    NETCDF_Q825, NETCDF_Q800, NETCDF_Q775,NETCDF_Q750, NETCDF_Q725, NETCDF_Q700, NETCDF_RH_975mb, NETCDF_RH_950mb, NETCDF_RH_925mb,NETCDF_RH_900mb, 
    NETCDF_RH_875mb, NETCDF_RH_850mb, NETCDF_RH_825mb, NETCDF_RH_800mb, NETCDF_RH_775mb, NETCDF_RH_750mb, NETCDF_RH_725mb, NETCDF_RH_700mb, 
    NETCDF_DPT_2m, NETCDF_Q, NETCDF_RH_2m, NETCDF_LCLT, NETCDF_VIS, NETCDF_VVEL_975mb, NETCDF_VVEL_950mb, NETCDF_VVEL_925mb, NETCDF_VVEL_900mb, 
    NETCDF_VVEL_875mb, NETCDF_VVEL_850mb, NETCDF_VVEL_825mb, NETCDF_VVEL_800mb, NETCDF_VVEL_775mb, NETCDF_VVEL_750mb, NETCDF_VVEL_725mb, NETCDF_VVEL_700mb],

    'Physical_G1':[NETCDF_FRICV, NETCDF_UGRD_10m, NETCDF_UGRD_975mb, NETCDF_UGRD_950mb, NETCDF_UGRD_925mb, NETCDF_UGRD_900mb,
    NETCDF_UGRD_875mb, NETCDF_UGRD_850mb, NETCDF_UGRD_825mb, NETCDF_UGRD_800mb, NETCDF_UGRD_775mb,  NETCDF_UGRD_750mb,
    NETCDF_UGRD_725mb, NETCDF_UGRD_700mb, NETCDF_VGRD_10m, NETCDF_VGRD_975mb, NETCDF_VGRD_950mb, NETCDF_VGRD_925mb,
    NETCDF_VGRD_900mb, NETCDF_VGRD_875mb, NETCDF_VGRD_850mb, NETCDF_VGRD_825mb, NETCDF_VGRD_800mb, NETCDF_VGRD_775mb, NETCDF_VGRD_750mb,
    NETCDF_VGRD_725mb, NETCDF_VGRD_700mb],
    'Physical_G2':[NETCDF_TKE_975mb, NETCDF_TKE_950mb, NETCDF_TKE_925mb, NETCDF_TKE_900mb, NETCDF_TKE_875mb, NETCDF_TKE_850mb, NETCDF_TKE_825mb,
    NETCDF_TKE_800mb, NETCDF_TKE_775mb, NETCDF_TKE_750mb, NETCDF_TKE_725mb, NETCDF_TKE_700mb, NETCDF_Q975, NETCDF_Q950, NETCDF_Q925, NETCDF_Q900,
    NETCDF_Q875, NETCDF_Q850, NETCDF_Q825, NETCDF_Q800, NETCDF_Q775,NETCDF_Q750, NETCDF_Q725, NETCDF_Q700],
    'Physical_G3':[NETCDF_TMP_2m, NETCDF_TMP_975mb, NETCDF_TMP_950mb, NETCDF_TMP_925mb, NETCDF_TMP_900mb, NETCDF_TMP_875mb, NETCDF_TMP_850mb,
    NETCDF_TMP_825mb, NETCDF_TMP_800mb, NETCDF_TMP_775mb, NETCDF_TMP_750mb, NETCDF_TMP_725mb, NETCDF_TMP_700mb, NETCDF_DPT_2m, NETCDF_RH_2m,
    NETCDF_RH_975mb, NETCDF_RH_950mb, NETCDF_RH_925mb,NETCDF_RH_900mb, NETCDF_RH_875mb, NETCDF_RH_850mb, NETCDF_RH_825mb, NETCDF_RH_800mb,
    NETCDF_RH_775mb, NETCDF_RH_750mb, NETCDF_RH_725mb, NETCDF_RH_700mb],
    'Physical_G4':[NETCDF_Q, NETCDF_LCLT, NETCDF_VIS, NETCDF_VVEL_975mb, NETCDF_VVEL_950mb, NETCDF_VVEL_925mb, NETCDF_VVEL_900mb, NETCDF_VVEL_875mb, NETCDF_VVEL_850mb, NETCDF_VVEL_825mb,
    NETCDF_VVEL_800mb, NETCDF_VVEL_775mb, NETCDF_VVEL_750mb, NETCDF_VVEL_725mb, NETCDF_VVEL_700mb], 
    'Mixed':[NETCDF_SST, NETCDF_TMPDPT, NETCDF_TMPSST, NETCDF_DPTSST], 
    'MUR': [NETCDF_SST], 
    'Generated': [NETCDF_TMPDPT, NETCDF_TMPSST, NETCDF_DPTSST], 
    'TMP': [NETCDF_TMP_SFC, NETCDF_TMP_2m, NETCDF_DPT_2m]
    }



NETCDF_MUR_NAMES   = [NETCDF_SST]
NETCDF_TMP_NAMES   = [NETCDF_TMP_SFC, NETCDF_TMP_2m, NETCDF_DPT_2m]
NETCDF_MIXED_NAMES = [NETCDF_SST, NETCDF_TMPDPT, NETCDF_TMPSST, NETCDF_DPTSST]
NETCDF_GEN_NAMES   = [NETCDF_TMPDPT, NETCDF_TMPSST, NETCDF_DPTSST]


DEFAULT_IMAGE_DIR_NAME = ('/data1/fog-data/fog-maps/')
DEFAULT_TARGET_DIR_NAME = ('/data1/fog/Dataset/TARGET')


DATE_FORMAT            = '%Y%m%d'
DATE_FORMAT_REGEX      = '[0-9][0-9][0-9][0-9][0-1][0-9][0-3][0-9]'
TIME_CYCLE_FORMAT      = '[0-9][0-9][0][0]'
HOUR_PREDICTION_FORMAT = '[0][0-9][0-9]'

### Defult Names and Settings
PREDICTOR_NAMES_KEY  = 'predictor_names'
PREDICTOR_MATRIX_KEY = 'predictor_matrix'
CUBE_NAMES_KEY       = 'cube_name'
SST_MATRIX_KEY       = 'sst_matrix'
SST_NAME_KEY         = 'sst_name'



DATE_FORMAT = '%Y%m%d'
DATE_FORMAT_REGEX = '[0-9][0-9][0-9][0-9][0-1][0-9][0-3][0-9]'
TIME_CYCLE_FORMAT = '[0-9][0-9][0][0]'
HOUR_PREDICTION_FORMAT = '[0-9][0-9][0-9]'




def time_string_to_unix(time_string, time_format):
    """Converts time from string to Unix format.
    Unix format = seconds since 0000 UTC 1 Jan 1970.
    :param time_string: Time string.
    :param time_format: Format of time string (example: "%Y%m%d" or
        "%Y-%m-%d-%H%M%S").
    :return: unix_time_sec: Time in Unix format.
    """
    return calendar.timegm(time.strptime(time_string, time_format))


def time_unix_to_string(unix_time_sec, time_format):
    """Converts time from Unix format to string.
    Unix format = seconds since 0000 UTC 1 Jan 1970.
    :param unix_time_sec: Time in Unix format.
    :param time_format: Desired format of time string (example: "%Y%m%d" or
        "%Y-%m-%d-%H%M%S").
    :return: time_string: Time string.
    """
    return time.strftime(time_format, time.gmtime(unix_time_sec))


def _nc_file_name_to_date(netcdf_file_name):
    """Parses date from name of image (NetCDF) file.
    :param netcdf_file_name: Path to input file.
    :return: date_string: Date (format "yyyymmdd").
    """
    pathless_file_name = os.path.split(netcdf_file_name)[-1]
    date_string = pathless_file_name.replace(pathless_file_name[0:5], '').replace(
        pathless_file_name[-18:], '')
    # Verify.
    time_string_to_unix(time_string=date_string, time_format=DATE_FORMAT)
    return date_string

def _nc_file_name_to_timecycle(netcdf_file_name):
    """Parses date from name of image (NetCDF) file.
    :param netcdf_file_name: Path to input file.
    :return: time-cycle prediction.
    """
    pathless_file_name = os.path.split(netcdf_file_name)[-1]
    timecycle_string = pathless_file_name.replace(pathless_file_name[0:14], '').replace(
        pathless_file_name[-13:], '')
    # Verify.
    #time_string_to_unix(time_string=timecycle_string, time_format=TIME_CYCLE_FORMAT)
    return timecycle_string

def _nc_file_name_to_hourprediction(netcdf_file_name):
    """Parses date from name of image (NetCDF) file.
    :param netcdf_file_name: Path to input file.
    :return: time-cycle prediction.
    """
    pathless_file_name = os.path.split(netcdf_file_name)[-1]
    hourpredic_string = pathless_file_name.replace(pathless_file_name[0:19], '').replace(
        pathless_file_name[-9:], '')
    return hourpredic_string




class input_dataframe_generater():

    def __init__(self, img_path = None, target_path = None, first_date_string = None, last_date_string = None, lead_time_pred = None):

        self.img_path          = img_path
        self.first_date_string = first_date_string
        self.last_date_string  = last_date_string
        self.lead_time_pred    = lead_time_pred


        if img_path is None: 
            self.img_path = DEFAULT_IMAGE_DIR_NAME

        if target_path is None: 
            target_path = DEFAULT_TARGET_DIR_NAME

        CSVfile = '{0:s}/Target.csv'.format(target_path)
        self.target  = self.reading_csv_target_file(CSVfile)


    def return_dataframe(self):

        targets_within_time_range = self.find_targets_within_time_range(first_date_string = self.first_date_string, last_date_string = self.last_date_string, target = self.target)
        netcef_nams_file_name, netcef_murs_file_name, targets_cleaned = self.matual_map_target_daily_cleaning(targets_within_time_range)
        output = self.generate_revised_dataframe(netcef_nams_file_name, netcef_murs_file_name, targets_cleaned)

        return output


    def generate_revised_dataframe(self, netcef_nams_file_name, netcef_murs_file_name, targets):
        
        netcdf_nam_names, netcdf_mur_names = [], []
        for i, row in targets.iterrows():
            day_time_obs = row['Name'] 

            timeseries_daily_nam_names, timeseries_daily_mur_names = self.return_daily_map_names_timeseries_list(netcef_nams_file_name, netcef_murs_file_name, day_time_obs)
            
            netcdf_nam_names.append(timeseries_daily_nam_names[0])
            netcdf_mur_names.append(timeseries_daily_mur_names)

        targets['nam_nc_files_path'] =  netcdf_nam_names
        targets['nam_nc_files_path'] =  targets['nam_nc_files_path'].astype('object')

        targets['mur_nc_files_path'] =  netcdf_mur_names
        targets['mur_nc_files_path'] =  targets['mur_nc_files_path'].astype('object')

        targets = targets.drop(columns=['WXCODE'])

        targets = targets.rename(columns={'Date_Time': 'date_time', "RoundTime":'round_time', "timecycle":'cycletime', "Date": "date", "Name":"date_cycletime", "VIS":"vis", "VIS_Cat": "vis_class"})
        targets.reset_index(inplace = True, drop = True)

        targets = targets[['date_time', 'round_time', 'date_cycletime', 'date', 'cycletime', 'year', 'month', 'day', 'nam_nc_files_path', 'mur_nc_files_path', 'vis']] 
        
        return targets


    def return_day_of_map_name(self, map_name): 

        namesplit = os.path.split(map_name)[-1]
        name      = namesplit.replace(namesplit[:5], '').replace(namesplit[18:], '')

        return name

    def return_day_of_mur_name(self, map_name): 

        namesplit = os.path.split(map_name)[-1]
        name      = namesplit.replace(namesplit[:5], '').replace(namesplit[13:], '')
        

        return name




    def return_daily_map_names_timeseries_list(self, nc_nam_file_names, nc_mur_file_names, day_time_obs):

        mur_day_time = day_time_obs[:8]
        
        

        nam_output = [name for name in nc_nam_file_names if self.return_day_of_map_name(name) == day_time_obs]
        mur_output = [name for name in nc_mur_file_names if self.return_day_of_mur_name(name) == mur_day_time][0:4]

        
        return nam_output, mur_output


    def find_targets_within_time_range(self, first_date_string, last_date_string, target):
        """Finds image (NetCDF) files in the given date range.
        :param first_date_string: First date ("yyyymmdd") in range.
        :param last_date_string: Last date ("yyyymmdd") in range.
        :param image_dir_name: Name of directory with image (NetCDF) files.
        :return: netcdf_file_names: 1-D list of paths to image files.
        """
        # check the target and return the desierd target index:
        Dates = target['Date'].values
        good_indices_target = numpy.where(numpy.logical_and(
            Dates >= int(first_date_string),
            Dates <= int(last_date_string)
        ))[0]

        target = target.take(good_indices_target)
        target.reset_index(inplace = True, drop = True)

        return target


    def matual_map_target_daily_cleaning(self, target):
        """
        Nan removal 
        days with less than 4 lead time observations removal
        """
        # 

        target_notnull                                             = self.null_target_detection(target) 
        target_notnull_full_day_obs                                = self.remove_days_with_incomplete_obs(target_notnull)
        netcef_nams_file_name, netcef_murs_file_name, target_outpu = self.return_nam_mur_nc_file_names(target_notnull_full_day_obs)

            
        return netcef_nams_file_name, netcef_murs_file_name, target_outpu


    def null_target_detection(self, target):
        # Reading Target data and list all NAM index to check and remove them plus corresponding map data:
        nan_targets_index = target[target['VIS_Cat'].isnull().values].index.tolist()


        # delete null rows
        target = target.drop(index = nan_targets_index)
        target.reset_index(inplace = True, drop = True)

        # delete rows with less than 4 lead-time observations per day: 
        for d in target['Date']:
            if target.loc[target.Date == d, 'Date'].count() < 4:
                target = target.drop(target.loc[target.Date == d, 'Date'].index)
        target.reset_index(inplace = True, drop = True)


        return target

    def remove_days_with_incomplete_obs(self, target): 

        for root, dirs, files in os.walk(self.img_path):
            dirs.sort()
            files.sort()

            if len(files) < 149 and len(files) != 0:
                if files[0].endswith(".nc"):
                    namesplit = os.path.split(files[0])[-1]
                    match_name = namesplit.replace(namesplit[:5], '').replace(namesplit[13:], '')
                    #print(('The expected maps is 149 which there are "{0}" maps for {1} day!').format(len(files), match_name))
                    target = target.drop(target[target.Date == int(match_name)].index)
                    #print('Removed the corresponding target values for days with incomplete data!')
                    #print('=====================================================================')

        return target


    def return_nam_mur_nc_file_names(self, target):

        # Reading the directory of map data and check and remove those they are incomplete or target is NAN!
        netcef_nams_file_name = []   
        netcef_murs_file_name = []   

        for root, dirs, files in os.walk(self.img_path):
            dirs.sort()
            files.sort()

            
            if len(files) == 149:
                namesplit     = os.path.split(files[0])[-1]
                nc_file_names = namesplit.replace(namesplit[:5], '').replace(namesplit[13:], '')
                
                if int(nc_file_names) in list(target['Date'].values):   #(foldercondition is True):
                    for name in files:
                        namesplit = os.path.split(name)[-1]
                        namOrmur = namesplit.replace(namesplit[4:], '')
                        if (namOrmur == 'murs'):
                            name = root +'/'+ name
                            netcef_murs_file_name.append(name)
                            netcef_murs_file_name.sort()
                        elif (namOrmur == 'maps'):
                            name = root +'/'+ name
                            netcef_nams_file_name.append(name)
                            netcef_nams_file_name.sort()


        netcef_nams_file_name_leadtime, netcef_murs_file_name_leadtime = self.find_names_within_leadtime(netcef_nams_file_name, netcef_murs_file_name)
        
        return netcef_nams_file_name_leadtime, netcef_murs_file_name_leadtime, target


    def find_names_within_leadtime(self, netcdf_nam_file_names, netcdf_mur_file_names):

        """Depend on the time prediction this function just select the name of selected maps:
        for example in this case, the time prediction 000, 003 and 006 hour has been selected.
        """
        file_date_strings = [_nc_file_name_to_hourprediction(f) for f in netcdf_nam_file_names]
        file_date_strings = pandas.DataFrame(file_date_strings, columns = ['str'])

        if self.lead_time_pred == 6: 
            hour_prediction_names = ['000', '006']
            good_indices = file_date_strings[
                (file_date_strings['str'] == hour_prediction_names[0]) |
                (file_date_strings['str'] == hour_prediction_names[1]) ]

            netcdf_mur_file_names2 = [8*[netcdf_mur_file_names[i]] for i in range(len(netcdf_mur_file_names))]
            netcdf_mur_file_names2 = list(itertools.chain.from_iterable(netcdf_mur_file_names2))

            
        elif self.lead_time_pred == 12: 
            hour_prediction_names = ['000', '006', '009', '012']
            good_indices = file_date_strings[
                (file_date_strings['str'] == hour_prediction_names[0]) |
                (file_date_strings['str'] == hour_prediction_names[1]) |
                (file_date_strings['str'] == hour_prediction_names[2]) |
                (file_date_strings['str'] == hour_prediction_names[3])]

            netcdf_mur_file_names2 = [16*[netcdf_mur_file_names[i]] for i in range(len(netcdf_mur_file_names))]
            netcdf_mur_file_names2 = list(itertools.chain.from_iterable(netcdf_mur_file_names2))


        elif self.lead_time_pred == 24: 
            hour_prediction_names = ['000', '006', '012', '024']
            good_indices = file_date_strings[
                (file_date_strings['str'] == hour_prediction_names[0]) |
                (file_date_strings['str'] == hour_prediction_names[1]) |
                (file_date_strings['str'] == hour_prediction_names[2]) |
                (file_date_strings['str'] == hour_prediction_names[3])]

            netcdf_mur_file_names2 = [16*[netcdf_mur_file_names[i]] for i in range(len(netcdf_mur_file_names))]
            netcdf_mur_file_names2 = list(itertools.chain.from_iterable(netcdf_mur_file_names2))


        return [netcdf_nam_file_names[k] for k in list(good_indices.index)], netcdf_mur_file_names2


    def reading_csv_target_file(self, csv_file_name):

        data = pandas.read_csv(csv_file_name, header=0, sep=',')
        year, month, day, timecycle = [], [], [], []
        for i in range(len(data)):
            year.append(data.iloc[i]['Name'][:4]) 
            month.append(data.iloc[i]['Name'][4:6])
            day.append(data.iloc[i]['Name'][6:8])
            timecycle.append(data.iloc[i]['Name'][9:]) 

        data['timecycle'] = timecycle
        data['year']      = year
        data['month']     = month
        data['day']       = day
        

        return data


class return_train_variable_mean_std():

    def __init__(self, dataset, predictor_names = None, lead_time_pred = None):
        self.dataset = dataset
        self.predictor_names = predictor_names 
        self.lead_time_pred = lead_time_pred

    def return_full_timeseries_names(self, netcdf_file_root_name):

        if self.lead_time_pred == 6:
            netcdf_file_006_names  = netcdf_file_root_name[0:57] + '006_input.nc'
            netcdf_file_names_list = [netcdf_file_root_name, netcdf_file_006_names]
            lead_time_steps = ['000', '006']

        elif self.lead_time_pred == 12:
            netcdf_file_006_names = netcdf_file_root_name[0:57] + '006_input.nc'
            netcdf_file_009_names = netcdf_file_root_name[0:57] + '009_input.nc'
            netcdf_file_012_names = netcdf_file_root_name[0:57] + '012_input.nc'
            netcdf_file_names_list = [netcdf_file_root_name, netcdf_file_006_names, netcdf_file_009_names, netcdf_file_012_names]
            lead_time_steps = ['000', '006', '009', '012']
        elif self.lead_time_pred == 24:
            netcdf_file_006_names = netcdf_file_root_name[0:57] + '006_input.nc'
            netcdf_file_012_names = netcdf_file_root_name[0:57] + '012_input.nc'
            netcdf_file_024_names = netcdf_file_root_name[0:57] + '024_input.nc'
            netcdf_file_names_list = [netcdf_file_root_name, netcdf_file_006_names, netcdf_file_012_names, netcdf_file_024_names]
            lead_time_steps = ['000', '006', '012', '024']

        return netcdf_file_names_list, lead_time_steps

    def return_mean_std_dict(self):

        output_dict = {}
        for name in self.predictor_names: 
            
            list_of_mean = []
            for idx in range(len(self.dataset)):

                nc_nam_timeseries_files_path_list = self.dataset.loc[idx]['nam_nc_files_path'] 
                full_timeseries_names, _ = self.return_full_timeseries_names(nc_nam_timeseries_files_path_list)

                for idx, nc_file_name in enumerate(full_timeseries_names):
            
                    dataset_object = netCDF4.Dataset(nc_file_name)

                    this_predictor_matrix = numpy.array(
                        dataset_object.variables[name][:], dtype = float)


                    this_predictor_leadtime_mean = numpy.mean(this_predictor_matrix)

                    list_of_mean.append(this_predictor_leadtime_mean)


            this_predictor_mean = st.mean(list_of_mean)
            this_predictor_std  = st.pstdev(list_of_mean)

            output_dict [name] = [this_predictor_mean, this_predictor_std] 

        return output_dict


def split_data_train_valid_test(dataset, year_split_dict = None):

    train_years = year_split_dict['train']
    valid_years = year_split_dict['valid']
    test_years  = year_split_dict['test']


    train_df = dataset[dataset['year'].isin([train_years])]
    train_df.reset_index(inplace = True, drop=True)

    valid_df = dataset[dataset['year'].isin([valid_years])]
    valid_df.reset_index(inplace = True, drop=True)

    test_df  = dataset[dataset['year'].isin([test_years])]
    test_df.reset_index(inplace = True, drop=True)


    return [train_df, valid_df, test_df]



class DataAdopter(): 

    def __init__(self, dataframe, vis_threshold = None, 
                                map_structure = None, 
                                predictor_names = None, 
                                lead_time_pred = None, 
                                mean_std_dict  = None,
                                point_geolocation_dic = None): 

        self.dataframe            = dataframe
        self.vis_threshold        = vis_threshold
        self.map_structure        = map_structure
        self.predictor_names      = predictor_names
        self.lead_time_pred       = lead_time_pred
        self.mean_std_dict        = mean_std_dict 
        self.point_geolocation_dic= point_geolocation_dic


    def __getitem__(self, idx): 

        # reading the data date and cycletime: 
        date_time      = self.dataset.loc[idx]['date_time']
        round_time     = self.dataset.loc[idx]['round_time']
        date_cycletime = self.dataset.loc[idx]['date_cycletime']


        # reading the nam map
        nc_nam_timeseries_files_path_list = self.dataset.loc[idx]['nam_nc_files_path']
        nam_timeseries_predictor_matrix   = self.read_nc_nam_maps(nc_nam_timeseries_files_path_list)

        # reading mur map 
        #nc_mur_timeseries_files_path_list = self.dataset.loc[idx]['mur_nc_files_path']
        #mur_timeseries_predictor_matrix   = self.read_nc_nam_maps(nc_mur_timeseries_files_path_list)

        #=============================================== reading the target visibility =======================================#
        visibility = self.dataset.loc[idx]['vis']

        # binarize the visibility to a class
        if visibility <= self.vis_threshold:
            label = 1
        else: 
            label = 0 

        #=============================================== return the sample =======================================#
        sample = {"date_time": date_time, "round_time": round_time, "date_cycletime": date_cycletime, "input": nam_timeseries_predictor_matrix, "label": label}


        return sample

    def read_nc_nam_maps(self, netcdf_file_root_names):

        NETCDF_PREDICTOR_NAMES = self.predictor_names

        if self.lead_time_pred == 6:

            netcdf_file_006_names  = netcdf_file_root_names[0:57] + '006_input.nc'
            netcdf_file_names_list = [netcdf_file_root_names, netcdf_file_006_names]
            lead_time_steps = ['000', '006']

        elif self.lead_time_pred == 12:

            netcdf_file_006_names = netcdf_file_root_names[0:57] + '006_input.nc'
            netcdf_file_009_names = netcdf_file_root_names[0:57] + '009_input.nc'
            netcdf_file_012_names = netcdf_file_root_names[0:57] + '012_input.nc'
            netcdf_file_names_list = [netcdf_file_root_names, netcdf_file_006_names, netcdf_file_009_names, netcdf_file_012_names]
            lead_time_steps = ['000', '006', '009', '012']

        elif self.lead_time_pred == 24:

            netcdf_file_006_names = netcdf_file_root_names[0:57] + '006_input.nc'
            netcdf_file_012_names = netcdf_file_root_names[0:57] + '012_input.nc'
            netcdf_file_024_names = netcdf_file_root_names[0:57] + '024_input.nc'
            netcdf_file_names_list = [netcdf_file_root_names, netcdf_file_006_names, netcdf_file_012_names, netcdf_file_024_names]
            lead_time_steps = ['000', '006', '012', '024']


        timeseries_predictor_matrix = None

        for idx, nc_file_name in enumerate(netcdf_file_names_list):
            
            dataset_object = netCDF4.Dataset(nc_file_name)

            predictor_matrix = None

            for this_predictor_name in NETCDF_PREDICTOR_NAMES:
                this_predictor_matrix = numpy.array(
                    dataset_object.variables[this_predictor_name][:], dtype=float
                )

                this_predictor_matrix = numpy.expand_dims(
                    this_predictor_matrix, axis=-1)
                
                this_predictor_mean  = self.mean_std_dict[this_predictor_name][0]
                this_predictor_std   = self.mean_std_dict[this_predictor_name][1] 

                this_predictor_matrix = (this_predictor_matrix - this_predictor_mean)/this_predictor_std

                if predictor_matrix is None:
                    predictor_matrix = this_predictor_matrix + 0.
                else:
                    predictor_matrix = numpy.concatenate(
                        (predictor_matrix, this_predictor_matrix), axis=-1
                    )

            if self.map_structure == '1D':

                lead_time_pred = lead_time_steps[idx]
                timeseries_predictor_matrix = self.return_tabular_data(predictor_matrix, lead_time_pred) 

            elif self.map_structure == '2D' or self.map_structure == '3D':

                if timeseries_predictor_matrix is None:
                    timeseries_predictor_matrix = predictor_matrix + 0.

                else:
                    timeseries_predictor_matrix = numpy.concatenate(
                        (timeseries_predictor_matrix, predictor_matrix), axis=-1
                    )

            elif self.map_structure == '4D':

                if timeseries_predictor_matrix is None:
                    timeseries_predictor_matrix = predictor_matrix + 0.

                else:
                    timeseries_predictor_matrix = numpy.concatenate(
                        (timeseries_predictor_matrix, predictor_matrix), axis=0
                    )
        
        return timeseries_predictor_matrix


    def return_tabular_data(self, nam_predictor_matrix):
            
        output_dfs = []

        for key in self.point_geolocation_dic:
            i = self.point_geolocation_dic[key][0]
            j = self.point_geolocation_dic[key][1]
            
            this_point_df = pd.DataFrame()

            for i in range(nam_predictor_matrix.shape[2]):
                this_predictor_matrix = nam_predictor_matrix.shape[:, :, i] 
                feature_value         = this_predictor_matrix[i, j]
                feature_name          = self.predictor_names[i] + '_' + key

                this_point_df.at[0, feature_name] = feature_value
            
            output_dfs.append(this_point_df)
        
        output = pandas.concat(output_dfs, axis=1)

        return output 
        
        

            

        



