
import os
import requests
import requests as req


# check if bioact file path exist
try:
    os.mkdir('./bioact')

except FileExistsError:
    pass


# use req to get the link 
'''
res = req.get('https://phytochem.nal.usda.gov/biological-activities-chemicals-csv-export/4/all?page&_format=csv')

#res2 = req.get('https://phytochem.nal.usda.gov/biological-activities-chemicals-csv-export/5/all?page&_format=csv')

csv = open('./bioact/4.csv', 'wb')
csv.write(res.content)

csv.close()

print('File 4 downloaded')

'''

# do it as a loop
base = 'https://phytochem.nal.usda.gov'

for i in range(1, 11):
    res = req.get(base + f'/biological-activities-chemicals-csv-export/{i}/all?page&_format=csv')

    csv = open(f'./bioact/{i}.csv', 'wb')
    csv.write(res.content)

    csv.close()

    print(f'File {i} downloaded')
    