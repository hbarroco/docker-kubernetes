#--------------------------------------------------------------------------
# Get global variables
#--------------------------------------------------------------------------
print ' ***** Starting Create and Get Global Variables ***** '
Server=AdminConfig.getid('/Cell:' + AdminControl.getCell() + '/Node:' + AdminControl.getNode() + '/Server:server1')
Node=AdminConfig.getid('/Cell:' + AdminControl.getCell() + '/Node:' + AdminControl.getNode() + '/')
Cell=AdminConfig.getid('/Cell:' + AdminControl.getCell() + '/')
NodeName=AdminControl.getNode()
print ' ***** End Create and Get Global Variables ***** '

#--------------------------------------------------------------------------
# Create a JAASAuthData object for component-managed authentication
#--------------------------------------------------------------------------
print ' ***** Starting Creating Authenication Alias - JAASAuthData ***** '
alias = NodeName + "/jarvis"
aliasName = ['alias', alias]
userId = ['userId', 'admin']
password = ['password', 'admin']
attrs = [aliasName, userId, password]
try:
	GlobalSecurityVar=AdminConfig.getid('/Cell:' + AdminControl.getCell() + '/' + 'Security:/')
	AdminConfig.create('JAASAuthData', GlobalSecurityVar, attrs)
	print 'OK!'
except:
	print "Error:\n"+str(sys.exc_info()[1])
	pass	
	
print ' ***** End Creating Authenication Alias - JAASAuthData ***** '

#--------------------------------------------------------------------------
# Save Configurations
#--------------------------------------------------------------------------
print ' ***** Starting Save Configurations ***** '
AdminConfig.save()
print ' ***** End Save Configurations ***** '