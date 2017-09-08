import os

#create a dictionary with all of the nodes that an upshift occurs
keys = []
values = []
#open the file text file with nodes and shifts, and strip out new line information
with open("SpeciesRichness.txt", "r") as f:
	words = [word.strip() for word in f]
# for each line in the file, the second column is added to keys, and the third column to the values variable
for line in words:
	code = line.split("\t")
	keys.append(code[0])
	values.append(code[1])
#this creates the dictionary from keys and values varibles
new_dict = {k: v for k, v in zip(keys, values)}


folder_path = '/Users/jacoblandis/Desktop/SisterCladeSim/Descendant_files'

for data_file in sorted(os.listdir(folder_path)):
	filename = "%s" %data_file
	filepath = '/Users/jacoblandis/Desktop/SisterCladeSim/Descendant_files/%s' % (data_file)
	f = open(filepath, "r")
	logfile = open(filename, "w")
	for line in f:
		data = line.split("\n")
		WGD = data[0]
		species = new_dict.get(WGD, "0")
		logfile.write(str(species) + "\n")
		logfile.close


Count_log = open("Count_log.txt", "w")
parsed_path = '/Users/jacoblandis/Desktop/SisterCladeSim/Parsed_data'
for data_file2 in sorted(os.listdir(folder_path)):
	filepath = '/Users/jacoblandis/Desktop/SisterCladeSim/Parsed_data/%s' % (data_file2)
	f2 = open(filepath, "r")
	counts = []
	for line in f2:
		data = line.split("\n")
		spec = data[0]
		counts.append(spec)
	split_string = list(map(int,counts))
	total_species = sum(split_string)
	Count_log.write(str(total_species) + ' species in %s' % (data_file2) + "\n")	
	