import pandas as pd
import numpy as np
from numpy.random import randn

# Dataframe looks like excel spreadsheet
data = randn(4,3) # Rows, Columns
rows = ["A", "B", "C", "D"]
cols = ["Monday", "Tuesday", "Friday"]

# Create dataframe
df1 = pd.DataFrame(data, rows, cols)
"""
     Monday   Tuesday    Friday
A  1.744477  1.452297  1.353898
B -0.866605 -0.066310 -2.130730
C -1.795608 -0.198530 -0.736941
D -0.800174 -1.851988  1.473071

"""

# import csv file
df2 = pd.read_csv('../data/dog_data.csv')
print(df2)
"""
                    Breed              Color        DogName  OwnerZip
0                COCKAPOO              BROWN        CHARLEY     15236
1            GER SHEPHERD        BLACK/BROWN         TACODA     15238
2           BELG MALINOIS            BRINDLE           EICH     15238
3                   MIXED        BLACK/BROWN          ARROW     15104
4     AM PIT BULL TERRIER        WHITE/BROWN         OAKLEY     15139
...                   ...                ...            ...       ...
2665         GOLDENDOODLE              BROWN        WINSLOW     15044
2666    YORKSHIRE TERRIER        BLACK/BROWN  ROCKY KALAKOS     15220
2667              LAB MIX  WHITE/BLACK/BROWN          ELLIE     15220
2668         GOLDENDOODLE              WHITE       CLARENCE     15143
2669    SHETLAND SHEEPDOG              BLACK        GRIFFIN     15136
"""

# Print row 0
row0 = df2[0]

# Print multiple rows
row058 = df2[[0,5,8]


