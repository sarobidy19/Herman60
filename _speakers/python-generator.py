import csv
import os

with open('../../GRASS-2026.csv', newline='',encoding="utf8") as csvfile:
	f = csv.DictReader(csvfile)
	for row in f:
		#firstname, lastname, affiliation, stage, title
		if row["Do you consent to have your name and affiliation listed on GRASS 2026's website?"] == "Yes":
			path_to_file = "{0} {1}.md".format(row['First Name'],row['Last Name'])
			if not os.path.exists(path_to_file):
				g = open(path_to_file,"w")
				g.writelines("--- \n")
				g.writelines("name: {0} {1}  \n".format(row['First Name'],row['Last Name']))
				g.writelines("first_name: {0} \n".format(row['First Name']))
				g.writelines("last_name: {0} ({1}) \n".format(row['Last Name'],row['Affiliation']))
				g.writelines("hide: true \n")
				g.writelines("--- \n \n ")
				#if row['talk'] == 'Yes':
				#	g.writelines("**Title**: *{0}*\n \n".format(row['title']))
				#	g.writelines(" **Abstract**:\n \n ")
				#elif row['talk'] == 'Undecided':
				#	g.writelines("**Title**: *{0}*\n \n".format("TBA"))
					#g.writelines(" **Abstract**:\n \n {0}".format(row['abstract']))
				#else:
				#	pass
				g.close()
