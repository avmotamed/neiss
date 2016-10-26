from sys import argv

""" This routine was created to merge multiple CSV files into one large file
to enable uploading NEISS data to MS Access.

The files are put together in combined.txt, so initial file should be renamed
to combined.txt and then run with argument of file to be appended to
main file.
"""

script, from_file = argv #from_file is file to be added to combined.txt file

to_file = "combined.txt" #will be repository for all data

# Read and write line by line
with open(from_file) as in_file:
    next(in_file) #skips first line of input file (header row)
    with open (to_file, 'a+') as out_file: #append file, add to end of file
        for line in in_file:
            out_file.write(line)

print "Alright, all done."

out_file.close()
in_file.close()
