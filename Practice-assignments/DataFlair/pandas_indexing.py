
import numpy as np
import pandas as pd

dataflair_df=pd.read_csv("http://theeventscalendar.com/content/uploads/2014/09/test-data-venues11.csv")
print(dataflair_df.head())
"""
                   VENUE NAME  ...               VENUE WEBSITE
0      Art Institute of Chicago  ...       http://www.artic.edu/
1                    Party Haus  ...                         NaN
2  Cambridge University Library  ...   http://www.lib.cam.ac.uk/
3          New Brookland Tavern  ...                         NaN
4                 Musee D’Orsay  ...  http://www.musee-orsay.fr/
"""

print(dataflair_df.index)
#RangeIndex(start=0, stop=12, step=1)

print(dataflair_df.columns)
"""
Index(['VENUE NAME', 'VENUE ADDRESS', 'VENUE ADDRESS 2', 'VENUE CITY',
       'VENUE STATE/PROVINCE', 'VENUE ZIP', 'VENUE COUNTRY', 'VENUE PHONE',
       'VENUE WEBSITE'],
      dtype='object')
"""

print(dataflair_df[["VENUE NAME","VENUE CITY","VENUE ZIP"]])
"""
                    VENUE NAME     VENUE CITY VENUE ZIP
0       Art Institute of Chicago        Chicago     60603
1                     Party Haus    Los Angelos     90013
2   Cambridge University Library      Cambridge   CB3 9DR
3           New Brookland Tavern  West Columbia     29169
4                  Musee D’Orsay          Paris     75007
5                   Bamboo Fresh        Lahaina     96761
6                The Corn Palace       Mitchell     57301
7                  San Diego Zoo      San Diego     92101
8                Doug Fir Lounge       Portland     97214
9                   Krispy Kreme      St. Louis     63129
10                   The Beanery      Corvallis     97330
11      Winchester Mystery House       San Jose     95128
"""

dataflair_df=pd.read_csv("http://theeventscalendar.com/content/uploads/2014/09/test-data-venues11.csv", index_col="VENUE NAME")
print(dataflair_df.head())
"""
                                  VENUE ADDRESS  ...               VENUE WEBSITE
VENUE NAME                                                  ...                            
Art Institute of Chicago                111 S Michigan Ave  ...       http://www.artic.edu/
Party Haus                                  330 S Broadway  ...                         NaN
Cambridge University Library                     West Road  ...   http://www.lib.cam.ac.uk/
New Brookland Tavern                      122 State Street  ...                         NaN
Musee D’Orsay                 1 Rue de la Légion d'Honneur  ...  http://www.musee-orsay.fr/
"""

print(dataflair_df.index)
print("\n")
"""
Index(['Art Institute of Chicago', 'Party Haus',
       'Cambridge University Library', 'New Brookland Tavern', 'Musee D’Orsay',
       'Bamboo Fresh', 'The Corn Palace', 'San Diego Zoo', 'Doug Fir Lounge',
       'Krispy Kreme', 'The Beanery', 'Winchester Mystery House'],
      dtype='object', name='VENUE NAME')
"""

print(dataflair_df.loc["Party Haus"])
print("\n")
"""
VENUE ADDRESS           330 S Broadway
VENUE ADDRESS 2               Unit 602
VENUE CITY                 Los Angelos
VENUE STATE/PROVINCE                CA
VENUE ZIP                        90013
VENUE COUNTRY            united States
VENUE PHONE                        NaN
VENUE WEBSITE                      NaN
Name: Party Haus, dtype: object
"""

print(dataflair_df.loc[["Party Haus","San Diego Zoo","Krispy Kreme"]])
print("\n")
"""
VENUE ADDRESS  ...                 VENUE WEBSITE
VENUE NAME                           ...                              
Party Haus           330 S Broadway  ...                           NaN
San Diego Zoo        2920 Zoo Drive  ...   http://zoo.sandiegozoo.org/
Krispy Kreme   6935 South Lindbergh  ...  https://www.krispykreme.com/
"""

print(dataflair_df.loc[["Party Haus","Bamboo Fresh"],["VENUE ZIP","VENUE PHONE"]])
print("\n")
"""
VENUE ZIP VENUE PHONE
VENUE NAME                        
Party Haus       90013         NaN
Bamboo Fresh     96761         NaN
"""

print(dataflair_df.loc[:,["VENUE CITY","VENUE COUNTRY"]])
print("\n")
"""
 VENUE CITY   VENUE COUNTRY
VENUE NAME                                                 
Art Institute of Chicago            Chicago   United States
Party Haus                      Los Angelos   united States
Cambridge University Library      Cambridge  United Kingdom
New Brookland Tavern          West Columbia   United States
Musee D’Orsay                         Paris          France
Bamboo Fresh                        Lahaina   United States
The Corn Palace                    Mitchell   United States
San Diego Zoo                     San Diego   United States
Doug Fir Lounge                    Portland   United States
Krispy Kreme                      St. Louis             NaN
The Beanery                       Corvallis   United States
Winchester Mystery House           San Jose   United States

"""

print(dataflair_df.iloc[4])
print("\n")
"""
VENUE ADDRESS           1 Rue de la Légion d'Honneur
VENUE ADDRESS 2                                  NaN
VENUE CITY                                     Paris
VENUE STATE/PROVINCE                             NaN
VENUE ZIP                                      75007
VENUE COUNTRY                                 France
VENUE PHONE                        +33 1 40 49 48 14
VENUE WEBSITE             http://www.musee-orsay.fr/
Name: Musee D’Orsay, dtype: object
"""

print(dataflair_df.iloc[:4])
print("\n")
"""
VENUE ADDRESS  ...              VENUE WEBSITE
VENUE NAME                                        ...                           
Art Institute of Chicago      111 S Michigan Ave  ...      http://www.artic.edu/
Party Haus                        330 S Broadway  ...                        NaN
Cambridge University Library           West Road  ...  http://www.lib.cam.ac.uk/
New Brookland Tavern            122 State Street  ...                        NaN
"""

print(dataflair_df.iloc[[2,4,6]])
print("\n")
"""
 VENUE ADDRESS  ...               VENUE WEBSITE
VENUE NAME                                                  ...                            
Cambridge University Library                     West Road  ...   http://www.lib.cam.ac.uk/
Musee D’Orsay                 1 Rue de la Légion d'Honneur  ...  http://www.musee-orsay.fr/
The Corn Palace                              601 N Main St  ...      http://cornpalace.com/
"""

print(dataflair_df.iloc[[2,3],[5,6]])
print("\n")
"""
VENUE COUNTRY      VENUE PHONE
VENUE NAME                                                   
Cambridge University Library  United Kingdom  +44 1223 333000
New Brookland Tavern           United States   (803) 791-4413
"""


print(dataflair_df.iloc[:,[2,4,5]])
print("\n")
"""
VENUE CITY VENUE ZIP   VENUE COUNTRY
VENUE NAME                                                           
Art Institute of Chicago            Chicago     60603   United States
Party Haus                      Los Angelos     90013   united States
Cambridge University Library      Cambridge   CB3 9DR  United Kingdom
New Brookland Tavern          West Columbia     29169   United States
Musee D’Orsay                         Paris     75007          France
Bamboo Fresh                        Lahaina     96761   United States
The Corn Palace                    Mitchell     57301   United States
San Diego Zoo                     San Diego     92101   United States
Doug Fir Lounge                    Portland     97214   United States
Krispy Kreme                      St. Louis     63129             NaN
The Beanery                       Corvallis     97330   United States
Winchester Mystery House           San Jose     95128   United States
"""

#Multi-indexing in Pandas
dataflair_df.set_index(["VENUE CITY","VENUE ADDRESS"], inplace=True)
print(dataflair_df)
"""
VENUE ADDRESS 2  ...                           VENUE WEBSITE
VENUE CITY    VENUE ADDRESS                                 ...                                        
Chicago       111 S Michigan Ave                       NaN  ...                   http://www.artic.edu/
Los Angelos   330 S Broadway                      Unit 602  ...                                     NaN
Cambridge     West Road                                NaN  ...               http://www.lib.cam.ac.uk/
West Columbia 122 State Street                         NaN  ...                                     NaN
Paris         1 Rue de la Légion d'Honneur             NaN  ...              http://www.musee-orsay.fr/
Lahaina       655 Front St.                           #108  ...                                     NaN
Mitchell      601 N Main St                            NaN  ...                  http://cornpalace.com/
San Diego     2920 Zoo Drive                           NaN  ...             http://zoo.sandiegozoo.org/
Portland      830 E. Burnside St.                      NaN  ...           http://www.dougfirlounge.com/
St. Louis     6935 South Lindbergh                     NaN  ...            https://www.krispykreme.com/
Corvallis     500 SW 2nd St                            NaN  ...                                     NaN
San Jose      525 S Winchester Blvd                    NaN  ...  http://www.winchestermysteryh
"""

print(dataflair_df.index)
"""
MultiIndex([(      'Chicago',           '111 S Michigan Ave'),
            (  'Los Angelos',               '330 S Broadway'),
            (    'Cambridge',                    'West Road'),
            ('West Columbia',             '122 State Street'),
            (        'Paris', '1 Rue de la Légion d'Honneur'),
            (      'Lahaina',                '655 Front St.'),
            (     'Mitchell',                '601 N Main St'),
            (    'San Diego',               '2920 Zoo Drive'),
            (     'Portland',          '830 E. Burnside St.'),
            (    'St. Louis',         '6935 South Lindbergh'),
            (    'Corvallis',                '500 SW 2nd St'),
            (     'San Jose',        '525 S Winchester Blvd')],
           names=['VENUE CITY', 'VENUE ADDRESS'])
"""


dataflair_df.sort_index(inplace=True)
print(dataflair_df)
"""
VENUE ADDRESS 2  ...                           VENUE WEBSITE
VENUE CITY    VENUE ADDRESS                                 ...                                        
Cambridge     West Road                                NaN  ...               http://www.lib.cam.ac.uk/
Chicago       111 S Michigan Ave                       NaN  ...                   http://www.artic.edu/
Corvallis     500 SW 2nd St                            NaN  ...                                     NaN
Lahaina       655 Front St.                           #108  ...                                     NaN
Los Angelos   330 S Broadway                      Unit 602  ...                                     NaN
Mitchell      601 N Main St                            NaN  ...                  http://cornpalace.com/
Paris         1 Rue de la Légion d'Honneur             NaN  ...              http://www.musee-orsay.fr/
Portland      830 E. Burnside St.                      NaN  ...           http://www.dougfirlounge.com/
San Diego     2920 Zoo Drive                           NaN  ...             http://zoo.sandiegozoo.org/
San Jose      525 S Winchester Blvd                    NaN  ...  http://www.winchestermysteryhouse.com/
St. Louis     6935 South Lindbergh                     NaN  ...            https://www.krispykreme.com/
West Columbia 122 State Street                         NaN  ...                                     NaN

"""