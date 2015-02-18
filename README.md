# APW-docs
Used for moving scanned invoices to the vendor folder

A very basic script to distribute files between multiple folders using filename as a criteria.

Input folder: "Coded"
Output folder: "Scanned docs"

The script is iterating over each file in Input folder, comparing first part of filename (before space) to the existing folder in the Output folder and moves the file there if folder found. It can either skip the file or create the folder if such is not present in the output folder.