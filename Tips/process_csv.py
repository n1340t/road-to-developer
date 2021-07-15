import csv
import json
from copy import copy
with open('report.csv', newline='', encoding='utf-8-sig') as csvfile:
    reader = csv.DictReader(csvfile)
    row_num = 0
    total_payout = 0
    for row in reader:
        if (row['is_paid'] == 'True' and (row['campaign_id'] == '2376119' or row['campaign_id'] == '2357918')):
            total_payout += float(row['payout'])
            row_num += 1

# with open('names.csv', 'w', newline='') as csvfile:
#     fieldnames = ['first_name', 'last_name']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

#     writer.writeheader()
#     writer.writerow({'first_name': 'Baked'})
#     writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
#     writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})
