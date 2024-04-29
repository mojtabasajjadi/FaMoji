# -*- coding: utf-8 -*-
"""

@author: Mojtaba Sajjadi
"""

import re
import pandas as pd
# Read data
df = pd.read_excel('emojis.xlsx', sheetname='Sheet1')
emoji = df['emoji'].tolist()
meaning = df['meaning'].tolist()
emojis_dict = dict(zip(emoji, meaning))


def replace_emojis_with_meaning(text):
    for emot in emojis_dict:
        text = re.sub(r'('+emot+')', "_".join(emojis_dict[emot].replace(",","").replace(":","").split()), text)
    return text

text = "وای بازی رو ندیدی؟ 🤦 زدیم ترکوندیم 🔥 کل شب رو هوا بودیم 😁"
print( replace_emojis_with_meaning(text))

