from sys import argv, exit
import os, string, shutil

# Setting variables for folder names
source = "Coded"
dest = "Scanned docs"

def visit(dest, dirname, names):
        for each in names:
                print each
                fileName = string.split(each, '.')[0]
                companyName = string.split(fileName, '-')[1]
		
def folderName(vendor):
        allSubfolders = os.walk(dest).next()[1]
        for item in allSubfolders:
                if vendor == item.split()[0].upper():
                        return item
        return None

for i in os.listdir(source):
        print "Processing file: ", i
        vendor = i.split()[0].upper()
        src = source + '\\' + i
        if folderName(vendor) <> None:
                # TODO: Check if multiple - which to use
                print "Folder exists. Copying... ",
                src = source + '\\' + i
                dst = dest + '\\' + folderName(vendor) + '\\' + i
                shutil.move(src, dst)
                print "Done"
        else:
                print '"', vendor, '"', " folder does not exist."
                guessInLower = ''
                while guessInLower not in ['n','s','c']:
                        guessText = 'Press "n" to create folder ' + vendor + '; "s" to skip this file or "c" to cancel:'
                        guess = raw_input(guessText)
                        guessInLower = guess.lower()
                if guessInLower == 'n':
                        print "Creating new folder...",
                        os.mkdir(dest + '\\' + vendor)
                        dst = dest + '\\' + vendor + '\\' + i
                        shutil.move(src, dst)
                        print "Done"
                if guessInLower == 's':
                        print "Skipped"
                if guessInLower == 'c':
                        print "Exiting..."
                        break
