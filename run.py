import subprocess
import pandas as pd

#open text file and batch files, you can edit "ex.txt" to whatever your input file name is, you'd also need to edit the content of the batch file
with open('ex.txt', 'r') as file:
    data = file.readlines()
with open('run.bat', 'r') as file:
    run = file.readlines()

#loop to create all input and output files, and run each file
for i in range(20):
    N = i
    Val = 4.9 - 0.1 * N
    Val = str(Val)
    data[13] = '2 so ' + Val + "\n"
    N3 = str(N)
    exfile = 'ex' + N3 + ".txt"
    with open(exfile, 'w') as file:
        file.writelines(data)

    exrun = 'ex' + N3 + ".txt"
    out = "o" + N3 + ".txt"
    run[0] = "mcnp5 i= " + exrun + " o= " + out + "\n"
    runname = "run" + N3 + ".bat"
    with open(runname, 'w') as file:
        file.writelines(run)
    subprocess.call(runname)

values = []

#loop for reading output file tally, edit according to desire
for i in range(0, 20):
    Nout = i
    Nout = str(Nout)
    outnumber = "o" + Nout + ".txt"
    with open(outnumber, 'r') as file:
        output = file.readlines()
        trial = str(output[151])
        values.append(trial)

#creating an excel file with the values extracted
pd.DataFrame(values).to_excel(
    'outputtrail2.xlsx', header=True, index=False)
