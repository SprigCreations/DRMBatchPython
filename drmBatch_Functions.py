# Sprig Creations - 8/9/2019
# Functions with parameters for running exports, books, action scripts
import subprocess
import sys
import Connection_Params as connParamsObj
strUserName=connParamsObj.DRM_Conn_Params.USER_NAME.value
strAppPassword=connParamsObj.DRM_Conn_Params.PASSWORD.value
strBatchClientPath=connParamsObj.DRM_Conn_Params.DRM_CLIENT_PATH.value
strAppUrl=connParamsObj.DRM_Conn_Params.DRM_APP_URL.value
strCurrentVersion=connParamsObj.DRM_Conn_Params.VERSION_NAME.value

#  Export By Name   - Standard Export
def SPC_RunExpByNameStd(strExportName,strExportFileName,strLogFileName):
 SPC_UpdLogs(strLogFileName,"Calling Standard Export" + strExportName)
 cmdString=strBatchClientPath, ' /u=' + strUserName , ' /pw=' + strAppPassword , ' /url=' + strAppUrl , ' /op=E /log=' + strLogFileName , ' /outfile=' + strExportFileName , ' /xtype=' + 'E' , ' /xname=' + strExportName , ' /cver=' + strCurrentVersion , ' /pver=' + strCurrentVersion
  # print(cmdString)
 subprocess.call(['cmd', '/c', cmdString])
 SPC_UpdLogs(strLogFileName,"Standard Export completed successfully - " + strExportName)

#  Export By Name   - Access Group
def SPC_RunExpByNameAGrp(strExportName,strExportFileName,strLogFileName,strExportAccessGrp):
  SPC_UpdLogs(strLogFileName,"Calling Object Access Group Export" + strExportName +"- " + strExportAccessGrp)
  cmdString=strBatchClientPath, ' /u=' + strUserName , ' /pw=' + strAppPassword , ' /url=' + strAppUrl , ' /op=E /log=' + strLogFileName , ' /outfile=' + strExportFileName , ' /xtype=' + 'E' , ' /xname=' + strExportName ,' /objectaccess=' + strExportAccessGrp, ' /cver=' + strCurrentVersion , ' /pver=' + strCurrentVersion
  # print(cmdString)
  subprocess.call(['cmd', '/c', cmdString])
  SPC_UpdLogs(strLogFileName,strExportName + "Export completed successfully")

#  Book Export   - Standard Export    
def SPC_RunBookByNameStd(strBookName,strCmbExportFileName,strLogFileName):
  SPC_UpdLogs(strLogFileName,"Calling Standard Book" + strBookName)
  cmdString=strBatchClientPath, ' /u=' + strUserName , ' /pw=' + strAppPassword , ' /url=' + strAppUrl , ' /op=E /log=' + strLogFileName , ' /outfile=' + strCmbExportFileName , ' /xtype=' + 'B' , ' /bk=' + strBookName , ' /bkcmb=Y  /cver=' + strCurrentVersion , ' /pver=' + strCurrentVersion
  # print(cmdString)
  subprocess.call(['cmd', '/c', cmdString])
  SPC_UpdLogs(strLogFileName,strBookName + "Book completed successfully")

#  Book Export   - Access Group        
def SPC_RunBookByNameAGrp(strBookName,strCmbExportFileName,strLogFileName,strExportAccessGrp):
  SPC_UpdLogs(strLogFileName,"Calling Object Access Group Book" + strBookName + "-" + strExportAccessGrp)
  cmdString=strBatchClientPath, ' /u=' + strUserName , ' /pw=' + strAppPassword , ' /url=' + strAppUrl , ' /op=E /log=' + strLogFileName , ' /outfile=' + strCmbExportFileName , ' /xtype=' + 'B' , ' /bk=' + strBookName,' /objectaccess=' + strExportAccessGrp , ' /cver=' + strCurrentVersion , ' /pver=' + strCurrentVersion
  # print(cmdString)
  subprocess.call(['cmd', '/c', cmdString])
  SPC_UpdLogs(strLogFileName,strBookName + "Book completed successfully")

#  Action Script - Tab seperated file
def SPC_RunActionScript(strActionScriptFileName,strDelimiter,strLogFileName):
 SPC_UpdLogs(strLogFileName,"Running Action Script File - " + strActionScriptFileName)
 cmdString=strBatchClientPath, ' /u=' + strUserName , ' /pw=' + strAppPassword , ' /url=' + strAppUrl , ' /op=A /log=' + strLogFileName , ' /infile=' + strActionScriptFileName , ' /delim=' + strDelimiter , ' /cver=' + strCurrentVersion , ' /pver=' + strCurrentVersion
  # print(cmdString)
 subprocess.call(['cmd', '/c', cmdString])
 SPC_UpdLogs(strLogFileName,strActionScriptFileName + "Action Script file completed successfully")

 # Log file update
def SPC_UpdLogs(strLogFileName,strLogText):
 logHandler=open(strLogFileName,"a")
 logHandler.write(strLogText)
 logHandler.close()
