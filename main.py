import re
import os
#file = "concurrency.md"

def filtcontent(lines):
    pluslines = [el for el in lines if '+ [' in el]
    #print(pluslines)

    fplines = [re.findall(r"\(+#[\w-]+", el) for el in pluslines]
    fp = [f[0][2:] for f in fplines if len(f) > 0]
    # for el in fp:
    #     print(el)
    return fp

def makelinkeblemd(file):
    with open(file, "r", encoding='utf-8') as f:
        lines = f.readlines()
    #print(lines)
    fp = filtcontent(lines)
    flines = []
    for line in lines:
        if "## " in line and "###" not in line and "## #" not in line:
            try:
                line = f'### <a name="{fp[0]}"></a>{line[3:]}\n'
            except:
                print(f"\n{line}\n in file {file}")
                exit(0)
            fp = fp[1:]
        flines.append(line)
    with open(f"filterdmds/{file}", "w") as wf:
        wf.writelines(flines)

def main():
    files = os.listdir()
    files = [f for f in files if ".md" in f]
    print(files)
    for f in files:
        makelinkeblemd(f)


if __name__ == '__main__':
    main()