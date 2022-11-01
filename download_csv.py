# Carder Brooks
# Assignment 8 - Microservice Implementation

# references cited: https://www.geeksforgeeks.org/convert-html-table-into-csv-file-in-python/


import pandas as pd
from bs4 import BeautifulSoup

# event loop
while True:

	# check txt file to see if html file name written to file
	with open('download.txt', 'r', encoding="utf-8") as f:
		read_data = f.read()

	# set the html_file variable to written file name if something written to file
	if read_data != "":
		html_file = read_data

		# initialize some_data variable
		some_data = []

		# get header from the HTML table
		list_header = []
		soup = BeautifulSoup(open(html_file),'html.parser')
		header = soup.find_all("table")[0].find("tr")

		for items in header:
			try:
				list_header.append(items.get_text())
			except:
				continue

		# get data from the HTML table
		HTML_data = soup.find_all("table")[0].find_all("tr")[1:]

		for element in HTML_data:
			sub_data = []
			for sub_element in element:
				try:
					sub_data.append(sub_element.get_text())
				except:
					continue
			some_data.append(sub_data)

		# Stor the data into a Pandas DataFrame
		dataFrame = pd.DataFrame(data = some_data, columns = list_header)

		# Convert the Pandas DataFrame into CSV file
		dataFrame.to_csv(read_data + '.csv')

		# delete contents from the download.txt file to reset for next download attempt
		with open('download.txt', 'w', encoding="utf-8") as f:
			pass

