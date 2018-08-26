import os


fpath = ('/flooreq')
new_content = 'Floor;-0.0231876;0.9997158;0.005523662;1.067132;\n'
for (dirname, dirs, files) in os.walk(fpath):
    for x in dirs:
        ppath = os.path.join(fpath, x)
        for (dirname, dirs, files) in os.walk(ppath):
            for y in files:
                file = os.path.join(ppath, y)
                f = open(file, 'r+')
                lines = f.readlines()
                f.seek(0)
                f.write(new_content)
                for line in lines:
                    f.write(line)
                f.close()