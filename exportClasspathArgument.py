from java.io import FileInputStream
import sys, datetime


def expClasspath(csvLoc):
  try:
    out = open(csvLoc,'a+')
    print('\n========== Export Classpaths ==========')
    # Looping every Server
    cd('/Servers')
    redirect('/dev/null','false')
    servers = ls(returnMap='true',returnType='c')
	
    for server in servers:
      cd('/Servers/'+ server +'/ServerStart/'+ server)
      print('Servers: ' + server)
      classpaths = cmo.getClassPath()
	  
      if str(classpaths) == "None" or str(classpaths) == '':
        output = 'classpath,' + server + ',-' + '\n'
      else:
        output = 'classpath,' + server + ',' + str(classpaths) + '\n'
		
      out.write(output)
	  
    out.close()

  except Exception, e:
    print e


def expArgument(csvLoc):
  try:
    out = open(csvLoc,'a+')
    print('\n========== Export Arguments ==========')  
    # Looping every Server
    cd('/Servers')
    redirect('/dev/null','false')
    servers = ls(returnMap='true',returnType='c')
	
    for server in servers:
      cd('/Servers/'+ server +'/ServerStart/'+ server)
      print('Servers: ' + server)
      argument = cmo.getArguments()
	  
      if str(argument) == "None" or str(argument) == '':
        output = 'argument,' + server + ',-' + '\n'
      else:
        output = 'argument,' + server + ',' + str(argument) + '\n'
		
      out.write(output)
	  
    out.close()

  except Exception, e:
    print e
    
def main():
  propInputStream = FileInputStream(sys.argv[1])
  configProps = Properties()
  configProps.load(propInputStream)
  
  adminUrl = configProps.get("adminUrl")
  importUser = configProps.get("importUser")
  importPassword = configProps.get("importPassword")
  csvLoc = configProps.get("csvLoc")
  #log = configProps.get("log")
  
  connect(importUser, importPassword, adminUrl)
  edit()
  startEdit()
  
  #date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  #file = open(csvLoc)
  
  expClasspath(csvLoc)
  expArgument(csvLoc)
  
  print('\n')
  
  activate()
  disconnect()

main()
