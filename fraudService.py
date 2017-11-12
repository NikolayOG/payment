import collections
import dateutil.parser
import pandas as pd

import model
import util


def detect_fraud_json(rows):
    json_data = collections.defaultdict(dict)
    for row in rows:
        print(row)
        id = row["id"] - 1
        json_data["place"][id] = row["merchant"]
        json_data["id"][id] = id
        date = dateutil.parser.parse(row["date"])
        json_data["year"][id] = date.year
        json_data["month"][id] = date.month
        json_data["day"][id] = date.day
        json_data["hour"][id] = date.hour

    return dict(json_data)

data = util.get_transactions_db(include_id=True)
detData = detect_fraud_json(data)
print(detData)
print(model.detect_fraud(pd.DataFrame.from_dict(detData)))
