import csv
import os

with open('../../speakers_list.csv', newline='',encoding="utf8") as csvfile:
	f = csv.DictReader(csvfile)
	for row in f:
		#firstname, lastname, affiliation, stage, title
		path_to_file = "talk-{0}-{1}.md".format(row['First Name'],row['Last Name'])
		if not os.path.exists(path_to_file):
			g = open(path_to_file,"w")
			g.writelines("--- \n")
			g.writelines("name: {0} \n".format(row['Title']))
			g.writelines("speakers: \n - {0} {1}  \ncategories:\n - {2}\n".format(row['First Name'],row['Last Name'],row['type']))
			g.writelines("--- \n \n")
			g.writelines("{0}".format(row['Abstract']))
			g.close()
		else:
			pass
