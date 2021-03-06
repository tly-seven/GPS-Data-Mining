from datetime import datetime
from apyori import apriori

from data_utils.data import return_data_rows


def do_apriori(min_support):
    transactions = []
    result = return_data_rows()
    for row in result:
        one_trip_locations = []
        for location in row.polyline:
            x = str(location.lat)[:8] + "," + str(location.long)[:8]
            one_trip_locations.append(x)
        transactions.append(one_trip_locations)
    start_time = datetime.now()
    item_sets = list(apriori(transactions, min_support=min_support / 10, min_confidence=1))
    end_time = datetime.now()
    diff = (end_time - start_time)
    print(item_sets)
    print("apriori longs : ", diff.total_seconds(), "seconds")
