import sys
from deploy import deploy

appname  =  sys.argv[0]
ear = sys.argv[1]
node = sys.argv[2]
cell = sys.argv[3]

try:
	install_options = sys.argv[4]
except:
	install_options = ''
	pass

deploy(appname, ear, node, cell, install_options)
