import sys
from inspect import getouterframes, currentframe

def deploy(appname, ear, node, cell, install_options=''):
    AdminApp =  sys._getframe( len(getouterframes(currentframe(0))) -1 ).f_locals['AdminApp']
    AdminConfig =  sys._getframe( len(getouterframes(currentframe(0))) -1 ).f_locals['AdminConfig']
    AdminControl = sys._getframe( len(getouterframes(currentframe(0))) -1 ).f_locals['AdminControl']


    print ""
    print "-----------------------------------------"
    print "Uninstall..."
    print "-----------------------------------------"
    try:
    	AdminApp.uninstall(appname)
    except:
    	print "Error:\n"+str(sys.exc_info()[1])
    	pass

    print ""
    print "-----------------------------------------"
    print "Save..."
    print "-----------------------------------------"
    AdminConfig.save()

    print ""
    print "-----------------------------------------"
    print "Install..."
    print "-----------------------------------------"
    AdminApp.install(ear,
        '[  -nopreCompileJSPs -distributeApp -nouseMetaDataFromBinary -nodeployejb -appname '
        + appname + ' -createMBeansForResources ' + install_options
        + ' -noreloadEnabled -nodeployws -validateinstall warn -processEmbeddedConfig -filepermission .*\.dll=755#.*\.so=755#.*\.a=755#.*\.sl=755 -noallowDispatchRemoteInclude -noallowServiceRemoteInclude -asyncRequestDispatchType DISABLED -nouseAutoLink]' )
    print ""
    print "-----------------------------------------"
    print "Save..."
    print "-----------------------------------------"
    AdminConfig.save()


    print ""
    print "-----------------------------------------"
    print "Start..."
    print "-----------------------------------------"

    try:
        appManager = AdminControl.queryNames('cell='+ cell +',node=' + node
            + ',type=ApplicationManager,process=server1,*')
        AdminControl.invoke(appManager, 'startApplication', appname)
    except:
        print "Error:\n" + str(sys.exc_info()[1])
        print ""
        print "Second try..."
        sleep(30)
        try:
            appManager = AdminControl.queryNames('cell='+ cell +',node=' + node
                + ',type=ApplicationManager,process=server1,*')
            AdminControl.invoke(appManager, 'startApplication', appname)
        except:
            print "Error:\n"+str(sys.exc_info()[1])
            print ""
            print "Could not initialize application. Try manually through console."
            raise ValueError('Could not initialize application. Try manually through console.')

    print ""
    print "-----------------------------------------"
    print "Done!!!!"
    print "-----------------------------------------"
