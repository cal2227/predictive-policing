import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data/data.csv")

type(data)
# <class 'pandas.core.frame.DataFrame'>

len(data)
# 1706742

data.columns
# Index(['sex', 'city', 'build', 'race', 'pct', 'pos_knife', 'pos_handgun',
#        'pos_rifle', 'pos_assault', 'pos_machgun', 'pos_otherweap',
#        'pos_illegal', 'cs_susp_obj', 'rf_unseasonal_attire', 'cs_crime_attire',
#        'cs_susp_bulge', 'cs_match_desc', 'cs_recon', 'cs_lookout',
#        'cs_drug_trade', 'cs_covert', 'rf_violent', 'cs_violent',
#        'ac_crime_area', 'ac_crime_time', 'ac_crime_assoc', 'ac_avoid_cops',
#        'label'],
#       dtype='object')

data['city'].head()
# 0    city_4
# 1    city_2
# 2    city_4
# 3    city_1
# 4    city_1
# Name: city, dtype: object

type(data['city'])
# <class 'pandas.core.series.Series'>

data['city'].dtype
# dtype('O')

for c in data.columns:
    print("{}: {}".format(c, set(data[c].values)))
# sex: {'M', 'F', 'Z'}
# city: {'Z', 'city_3', 'city_2', 'city_1', 'city_5', 'city_4'}
# build: {'build_1', 'build_4', 'build_3', 'build_2', 'Z'}
# race: {'race_5', 'race_4', 'race_7', 'race_6', 'race_1', 'race_3', 'Z', 'race_8'}
# pct: {'pct_10', 'pct_11', 'pct_12', 'pct_13', 'pct_14', 'pct_15', 'pct_16', 'pct_17', 'pct_18', 'pct_19', 'pct_50', 'pct_32', 'pct_20', 'pct_39', 'pct_58', 'pct_35', 'pct_38', 'pct_77', 'pct_74', 'pct_75', 'pct_72', 'pct_59', 'pct_70', 'pct_71', 'pct_54', 'pct_55', 'pct_56', 'pct_57', 'pct_36', 'pct_51', 'pct_52', 'pct_73', 'pct_25', 'pct_24', 'pct_27', 'pct_26', 'pct_21', 'pct_49', 'pct_23', 'pct_22', 'pct_66', 'pct_29', 'pct_28', 'pct_69', 'pct_3', 'pct_33', 'pct_46', 'pct_0', 'pct_1', 'pct_2', 'pct_31', 'pct_4', 'pct_5', 'pct_6', 'pct_7', 'pct_8', 'pct_9', 'pct_34', 'pct_53', 'pct_37', 'pct_61', 'pct_60', 'pct_63', 'pct_62', 'pct_65', 'pct_64', 'pct_67', 'pct_48', 'pct_47', 'pct_68', 'pct_45', 'pct_44', 'pct_43', 'pct_42', 'pct_41', 'pct_40'}
# pos_knife: {0, 1}
# pos_handgun: {0, 1}
# pos_rifle: {0, 1}
# pos_assault: {0, 1}
# pos_machgun: {0, 1}
# pos_otherweap: {0, 1}
# pos_illegal: {0, 1}
# cs_susp_obj: {0, 1}
# rf_unseasonal_attire: {0, 1}
# cs_crime_attire: {0, 1}
# cs_susp_bulge: {0, 1}
# cs_match_desc: {0, 1}
# cs_recon: {0, 1}
# cs_lookout: {0, 1}
# cs_drug_trade: {0, 1}
# cs_covert: {0, 1}
# rf_violent: {0, 1}
# cs_violent: {0, 1}
# ac_crime_area: {0, 1}
# ac_crime_time: {0, 1}
# ac_crime_assoc: {0, 1}
# ac_avoid_cops: {0, 1}
# label: {1, -1}

for c in data.columns:
    print("{}: {}".format(c, data[c].unique()))
# sex: ['M' 'F' 'Z']
# city: ['city_4' 'city_2' 'city_1' 'city_5' 'city_3' 'Z']
# build: ['build_3' 'build_4' 'build_2' 'Z' 'build_1']
# race: ['race_6' 'race_4' 'race_7' 'race_5' 'race_3' 'Z' 'race_1' 'race_8']
# pct: ['pct_41' 'pct_47' 'pct_9' 'pct_63' 'pct_42' 'pct_16' 'pct_1' 'pct_36'
#  'pct_13' 'pct_52' 'pct_59' 'pct_55' 'pct_38' 'pct_68' 'pct_51' 'pct_25'
#  'pct_74' 'pct_67' 'pct_75' 'pct_45' 'pct_14' 'pct_72' 'pct_39' 'pct_43'
#  'pct_4' 'pct_22' 'pct_48' 'pct_62' 'pct_49' 'pct_15' 'pct_18' 'pct_44'
#  'pct_24' 'pct_29' 'pct_70' 'pct_17' 'pct_10' 'pct_37' 'pct_73' 'pct_77'
#  'pct_28' 'pct_23' 'pct_57' 'pct_60' 'pct_50' 'pct_19' 'pct_27' 'pct_61'
#  'pct_8' 'pct_65' 'pct_11' 'pct_64' 'pct_34' 'pct_58' 'pct_66' 'pct_2'
#  'pct_56' 'pct_5' 'pct_7' 'pct_46' 'pct_31' 'pct_40' 'pct_33' 'pct_26'
#  'pct_21' 'pct_12' 'pct_6' 'pct_71' 'pct_53' 'pct_54' 'pct_3' 'pct_69'
#  'pct_20' 'pct_32' 'pct_0' 'pct_35']
# pos_knife: [0 1]
# pos_handgun: [0 1]
# pos_rifle: [0 1]
# pos_assault: [0 1]
# pos_machgun: [0 1]
# pos_otherweap: [0 1]
# pos_illegal: [0 1]
# cs_susp_obj: [0 1]
# rf_unseasonal_attire: [0 1]
# cs_crime_attire: [0 1]
# cs_susp_bulge: [0 1]
# cs_match_desc: [0 1]
# cs_recon: [0 1]
# cs_lookout: [0 1]
# cs_drug_trade: [0 1]
# cs_covert: [0 1]
# rf_violent: [0 1]
# cs_violent: [0 1]
# ac_crime_area: [1 0]
# ac_crime_time: [0 1]
# ac_crime_assoc: [0 1]
# ac_avoid_cops: [0 1]
# label: [-1  1]

data.dtypes
# sex                     object
# city                    object
# build                   object
# race                    object
# pct                     object
# pos_knife                int64
# pos_handgun              int64
# pos_rifle                int64
# pos_assault              int64
# pos_machgun              int64
# pos_otherweap            int64
# pos_illegal              int64
# cs_susp_obj              int64
# rf_unseasonal_attire     int64
# cs_crime_attire          int64
# cs_susp_bulge            int64
# cs_match_desc            int64
# cs_recon                 int64
# cs_lookout               int64
# cs_drug_trade            int64
# cs_covert                int64
# rf_violent               int64
# cs_violent               int64
# ac_crime_area            int64
# ac_crime_time            int64
# ac_crime_assoc           int64
# ac_avoid_cops            int64
# label                    int64
# dtype: object

data['city'].astype('category')
# 0          city_4
# 1          city_2
# ...
# 1706740    city_2
# 1706741    city_1
# Name: city, dtype: category
# Categories (6, object): [Z, city_1, city_2, city_3, city_4, city_5]

data['pos_illegal'].astype('category')
# 0          0
# 1          0
# ...
# 1706740    0
# 1706741    0
# Name: pos_illegal, dtype: category
# Categories (2, int64): [0, 1]

data['city'].value_counts().plot(kind='bar')
# <matplotlib.axes._subplots.AxesSubplot object at 0x11aef2d10>
plt.show()

data.groupby('city').size().plot(kind='bar')
# <matplotlib.axes._subplots.AxesSubplot object at 0x10666b290>
plt.show()

