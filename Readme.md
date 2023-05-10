## Running multiple mcnp inputs automatically
Created this program because i wanted to get around 20 different values for the flux according to how many neutrons passed through a lead shield
This is is just to iterate the radius of the sphere 20 times, and hence get input files, output files, and batch run files.

# input file
The input file is already provided as "ex.txt", line 13 in my case is edited to reduce the radius by 0.1 for each input file.

# run file
since each time you run, a new ex file is generated (i.e:ex1, ex2), it's also necessary to iterate the run command

# output file
it's inconvenient to go and find the tally yourself from each output file, since it's always on the same line for this type of run it's convenient to read the output files and gather
the tally using pandas library.

Overall this is a very simple code, but useful in these niche cases.
