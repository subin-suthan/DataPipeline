
####################### Converting Semi-Structured Data to Structured CSV Data##########################################

import os
import csv

data=[['USAF','WBAN','date','time','lat','long','ele','winddir','sky','visdist','airtemp','dewpointtemp','atmpress']]

csv_file="2014.csv"


def extract_substring(input_string,x,y):
        substring = input_string[x:y]  
        return substring

def convert(line):
         
         global data
         USAF = extract_substring(line,4,10)
         WBAN = extract_substring(line,10,15)
         date = extract_substring(line,15,23)
         time = extract_substring(line,23,27)
         lat = extract_substring(line,28,34)
         long = extract_substring(line,34,41)
         ele = extract_substring(line,46,51)
         winddir = extract_substring(line,60,63)
         sky = extract_substring(line,70,75)
         visdist = extract_substring(line,78,84)
         airtemp = extract_substring(line,87,92)
         dewpointtemp = extract_substring(line,93,98)
         atmpress = extract_substring(line,99,104)

         
         data.append([USAF,WBAN,date,time,lat,long,ele,winddir,sky,visdist,airtemp,dewpointtemp,atmpress])

def extract_lines_from_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return lines

def main(directory):
    global data
    for dir in os.listdir(directory):
           entry=os.path.join(directory,dir)  
           if not os.path.isdir(entry):
        #       for filename in os.listdir(entry):
                   data=[['USAF','WBAN','date','time','lat','long','ele','winddir','sky','visdist','airtemp','dewpointtemp','atmpress']]
                   
                   #file_path = os.path.join(entry, dir)
                   print(f"Extracting lines from file: {entry}")
                   lines = extract_lines_from_file(entry)

                   for line in lines:
                       convert(line)
            
            
                   csv_file=dir[13:17]+".csv"
                  #  with open(csv_file, mode='w', newline='') as file:
                  #       writer = csv.writer(file)
                  #       writer.writerows(data)

                #    newdir="./dataConverted/"+os.path.basename(dir)
                #    os.makedirs(newdir, exist_ok=True)     
                   file_path = os.path.join("./dataConverted/", csv_file)

                   with open(file_path, mode='w', newline='') as file:
                      writer = csv.writer(file)
                      writer.writerows(data)

    
                  
if __name__ == "__main__":
    directory = "./data" 
    main(directory)

