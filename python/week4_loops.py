# -*- coding: utf-8 -*-
"""Week4_Loops.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xtkOKZTLFJWHpBlr5cwUArtDocMb_1WH
"""

import requests
import json

url_base = "https://api.stlouisfed.org/fred/series/observations?series_id={}&api_key=fcc029f036677d1128e99b6ff0deeb22&file_type=json"

file_base = "tracking-{}.json"

coinlist = ['EMISSCO2VCLRCBNMA', 'EMISSCO2VCLACBRIA', 'EMISSCO2TOTVICTOUSA', 'EMISSCO2VAVACBA']

for i in coinlist:  
   print(i) 

   URL = url_base.format(i)
   print(URL)
 
   data = requests.get(URL).json()
   print(data)

   fileName = file_base.format(i)
   print(fileName)

   with open(fileName, 'w', encoding='utf-8') as f:
     json.dump(data, f, ensure_ascii=False, indent=4)

   files.download('{}'.format(fileName))