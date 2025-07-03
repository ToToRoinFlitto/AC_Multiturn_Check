import pandas as pd
import json

raw = pd.read_excel('/mnt/c/Users/Flitto/My Documents/AC/멀티턴대화/QC/dataset/rawdata.xlsx')


for j in range(5):
    
    data = {
        "script": str(raw[1][j])
    }

    with open(f'/mnt/c/Users/Flitto/My Documents/AC/멀티턴대화/QC/dataset/script_{j}.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
