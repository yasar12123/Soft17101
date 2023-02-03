import os

#This section lists paths and files
path = r'C:\Users\yh28\PycharmProjects\Python Project'
fileEPL = 'epl.txt'
EPLFullPath = os.path.join(path, fileEPL)

for line in open(EPLFullPath):
    print(line)