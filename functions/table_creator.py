import csv

new_element = {
    'short_name': 'WHV703',
    'Carrier': 'CLARO',
    'Firmware': '--',
    'Dealer': 'TSO Mobile Colombia',
    'Last date reported': '5/29/2025 2:31:08 PM',
    'Requested video':'Y'
}

with open('elements.csv', mode='a', newline='') as file:
    file.write('\n')
    csv_writer = csv. DictWriter(file, fieldnames = new_element.keys())
    csv_writer.writerow(new_element)