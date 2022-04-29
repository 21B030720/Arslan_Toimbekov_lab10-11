"""from csv import writer
list_data=['11222211111111111','2222222','222222222222']
with open('d.csv', 'a', newline='') as f_object:
    # Pass the CSV  file object to the writer() function
    writer_object = writer(f_object)
    # Result - a writer object
    # Pass the data in the list as an argument into the writerow() function
    writer_object.writerow(list_data)
    # Close the file object
    f_object.close()"""
import json
with open('snake_data.json', 'r') as f:
    f = json.load(f)
    f['k'] = 0
    p = open('snake_data.json', 'w')
    json.dump(f ,p)

