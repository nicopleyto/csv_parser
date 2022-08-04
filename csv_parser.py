import csv
import re
from datetime import datetime

#initializes the output file with headers
outfile = open("parsed_data.csv", 'w')
outfile_header = "First Name,Last Name,Position,Company Email,Mobile Number,Originating URL Submitted on,Form Location,Submitted on\n"
outfile.write(outfile_header)

#reads the csv file to be parsed
with open("logs-insights-results (1).csv", 'r') as infile:
  reader = csv.reader(infile)
  next(reader) #skips header of file to be read
  for row in reader:
    raw_data = row[0]

    first_name = re.compile(r'(?<=\"first_name\"=>\")(.*?)(?=\")').search(raw_data).group()
    last_name = re.compile(r'(?<=\"last_name\"=>\")(.*?)(?=\")').search(raw_data).group()
    position = re.compile(r'(?<=\"position\"=>\")(.*?)(?=\")').search(raw_data).group()
    email = re.compile(r'(?<=\"email\"=>\")(.*?)(?=\")').search(raw_data).group()
    mobile = re.compile(r'(?<=\"mobile\"=>\")(.*?)(?=\")').search(raw_data).group()
    origin_url = re.compile(r'(?<=\"url\"=>\")(.*?)(?=\")').search(raw_data).group()
    form_location = re.compile(r'(?<=\"form_location\"=>\")(.*?)(?=\")').search(raw_data).group()

    submitted_on_string = re.compile(r'(?<=I, \[)(.*?)(?=#)').search(raw_data).group().strip()
    submitted_on = datetime.fromisoformat(submitted_on_string) #convert string to datetime object

    line = "{},{},{},{},{},{},{},{}\n".format(first_name, last_name, position, email, mobile, origin_url, form_location, submitted_on)
    outfile.write(line)

outfile.close
