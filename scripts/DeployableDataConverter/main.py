sourcefile = open("Source.txt", "r", encoding="utf-8", errors="ignore")
outputfile = open("finished.md", "w", encoding="utf-8")

for sourceline in sourcefile.readlines():
    if '#' in sourceline:
        outputline = '## %s \n\n' % (sourceline[0:sourceline.find('#')])
        outputfile.write(outputline)
        continue
    if ':' in sourceline:
        outputline = '- %s \n\n' % (sourceline[0:sourceline.find(':')])
        outputline += '    `%s`\n\n' % (
            sourceline[sourceline.find(':')+1:sourceline.find('\n')])
        outputfile.write(outputline)
