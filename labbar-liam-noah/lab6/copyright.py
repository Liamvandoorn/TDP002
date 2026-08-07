#!usr/bin/env python3
#import argparse # Bibliotek för att läsa flaggor från terminalen
import argparse
import re
import os
#hämtar filen,
#skär filen vid regexmönster

parser = argparse.ArgumentParser() # argument parser
                                   

parser.add_argument("copyrightFile")
parser.add_argument("destination")
parser.add_argument("-c", "--filetype")
parser.add_argument("-u", "--filetypenew")

args = parser.parse_args()

copyrightText = open(args.copyrightFile).read().removesuffix("\n")

if os.path.isfile(args.destination):
    if not (args.filetype != None and ".".join(args.destination.split(".")[1:]) != args.filetype):
        with open(args.destination, "r+") as destFile:
            string = destFile.read()
            print("Before:",string)
            string = re.split(r"BEGIN COPYRIGHT(?:(?!BEGIN COPYRIGHT|END COPYRIGHT).)*END COPYRIGHT",string)
            string = ("BEGIN COPYRIGHT " + copyrightText + " END COPYRIGHT").join(string)
            print("After:",string)
            destFile.seek(0)
            destFile.write(string)
            destFile.truncate()
            if args.filetypenew != None:
                os.rename(destFile.name, destFile.name.split(".")[0] + "." + args.filetypenew)

elif os.path.isdir(args.destination):
    for dirFile in os.listdir(args.destination):
        if not (args.filetype != None and ".".join(dirFile.split(".")[1:]) != args.filetype):
            with open(args.destination + "/" + dirFile, "r+") as destFile:
                string = destFile.read()
                print("Before (",dirFile,"):",string)
                string = re.split(r"BEGIN COPYRIGHT(?:(?!BEGIN COPYRIGHT|END COPYRIGHT).)*END COPYRIGHT",string)
                string = ("BEGIN COPYRIGHT " + copyrightText + " END COPYRIGHT").join(string)
                print("After (",dirFile,"):",string)
                destFile.seek(0)
                destFile.write(string)
                destFile.truncate()
                if args.filetypenew != None:
                    os.rename(destFile.name, destFile.name.split(".")[0] + "." + args.filetypenew)
            
# def main():
#     with open(args.copyRight-File, 'r') as f:
#         x = re.findall(r'BEGIN COPYRIGHT.*END COPYRIGHT')
        
    
    # hitta copryright filen
    # hitta destinations filen
     # hitta regex mönstret i destinationsfilen
     # Bifoga copyright filen vid regexmönstret i destinationsfilen.

         
    # bifoga copyright filens innehåll 

