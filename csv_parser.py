import csv
import re

#initializes the output file with headers
outfile = open("parsed_data.csv", 'w')
outfile_header = "First Name,Last Name,Position,Company Email,Mobile Number,Originating URL Submitted on,Form Location,Status,Submitted on\n"
outfile.write(outfile_header)

#reads the csv file to be parsed
with open("logs-insights-results (1).csv", 'r') as infile:
  reader = csv.reader(infile)
  next(reader) #skips header of file to be read
  for row in reader:
    raw_data = row[0]
    first_name = re.compile(r'(?<=\"first_name\"=>\")(.*?)(?=\")').search(raw_data).group()
    # last_name =
    # position =
    # email =
    # mobile =
    # origin =
    # form_location =
    # status =
    # submitted_on =
    # print(raw_data)
    line = "{}\n".format(first_name)
    # line = "{},{},{},{},{},{},{},{},{}\n".format(first_name, last_name, position, email, mobile, origin, form_location, status, submitted_on)
    outfile.write(line)

outfile.close
