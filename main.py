import os
import csv
import pathlib

results = csv.writer(open("results.csv", mode='w'))

def textFileSearch(file, tts):
    content = open(file, "r").read().splitlines()
    for i in range(len(content)):
        if(content[i].find(tts) != -1):
            results.writerow([file, i + 1, content[i]])

def csvFileSearch(file, tts):
    content = csv.reader(open(file, mode='r'))
    for i in range(len(content)):
        for j in content[i]:
            if(j.find(tts)):
                results.writerow([file, i + 1, content[i]])

def search(dir, tts):
    os.chdir(dir)
    files = os.listdir()
    for file in files:
        if os.path.isdir(file):
            search(dir + "\\" + file, tts)
            os.chdir(dir)
        else:
            fileType = pathlib.Path(file).suffix
            if fileType == ".txt" or fileType == "":
                textFileSearch(dir + "\\" + file, tts)
            elif fileType == ".csv":
                csvFileSearch(dir + "\\" + file, tts)

#To start, input the directory

directory = input()

#input the text to be searched

txtToSearch = input()
results.writerow(["file", "line #", "content"])
search(directory, txtToSearch)


