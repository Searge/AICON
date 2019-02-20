
# file with SVG text
filepath = 'text.txt'

# out files prefix
outprename = "Set1_"

with open(filepath) as fp:
    line = fp.readline()
    cnt = 1
    while line:

        # add space before and after
        line = ' ' + line
        line = line.replace('\n', ' \n')
#       line = ' ' + line + ' '

        # replace x1
        line = line.replace(' б', ' <line class="cls-1" x1="1"')
        line = line.replace(' в', ' <line class="cls-1" x1="2"')
        line = line.replace(' г', ' <line class="cls-1" x1="3"')
        line = line.replace(' д', ' <line class="cls-1" x1="4"')
        line = line.replace(' ж', ' <line class="cls-1" x1="5"')
        line = line.replace(' з', ' <line class="cls-1" x1="6"')
        line = line.replace(' к', ' <line class="cls-1" x1="7"')
        line = line.replace(' л', ' <line class="cls-1" x1="8"')
        line = line.replace(' м', ' <line class="cls-1" x1="9"')

        # replace y2
        line = line.replace('а ', 'y2="1"/> ')
        line = line.replace('е ', 'y2="2"/> ')
        line = line.replace('є ', 'y2="3"/> ')
        line = line.replace('и ', 'y2="4"/> ')
        line = line.replace('і ', 'y2="5"/> ')
        line = line.replace('о ', 'y2="6"/> ')
        line = line.replace('у ', 'y2="7"/> ')
        line = line.replace('ю ', 'y2="8"/> ')
        line = line.replace('я ', 'y2="9"/> ')

        # replace y1
        line = line.replace('а', ' y1="1"')
        line = line.replace('е', ' y1="2"')
        line = line.replace('є', ' y1="3"')
        line = line.replace('и', ' y1="4"')
        line = line.replace('і', ' y1="5"')
        line = line.replace('о', ' y1="6"')
        line = line.replace('у', ' y1="7"')
        line = line.replace('ю', ' y1="8"')
        line = line.replace('я', ' y1="9"')

        # replace x2
        line = line.replace('б', ' x2="1" ')
        line = line.replace('в', ' x2="2" ')
        line = line.replace('г', ' x2="3" ')
        line = line.replace('д', ' x2="4" ')
        line = line.replace('ж', ' x2="5" ')
        line = line.replace('з', ' x2="6" ')
        line = line.replace('к', ' x2="7" ')
        line = line.replace('л', ' x2="8" ')
        line = line.replace('м', ' x2="9" ')

        line = '<svg id="Set_5" data-name="Set 5" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 10 10"><defs><style>.cls-1{fill:none;stroke:#000;stroke-linecap:round;stroke-linejoin:round;stroke-width:0.5px;}</style></defs><title>Set_5</title>' + line + '</svg>'

        line = line.replace('> <', '>\n<')

        outfilename = outprename + str(cnt) + '.svg'
        outfile = open(outfilename, "w")
        outfile.write(line)
        line = fp.readline()
        cnt += 1
        outfilename = ''
