#Adjust the indent and format of raw signal from mode2
#to match the format of remote configuration at lircd.conf
#By Brian Rompis 09/10/2018

import fileinput

remote_key = raw_input('Enter Key Name: ')

for line in fileinput.input('lirc.conf', inplace=1):
  if fileinput.lineno() != 1 and fileinput.lineno() != 2:
    if fileinput.lineno() == 3:
      print ("          name %s" % remote_key)
    else:
      print '        ' + line,
