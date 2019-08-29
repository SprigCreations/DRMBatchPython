# Sprig Creations - 8/9/2019
# Sample script calls to run exports, books and action script files
# import DRM batch client function definition
import sys
import drmBatch_Functions as drmBatchObj
import Batch_Params as batchParamsObj

#  Export By Name   - Standard Export
Export_Name_Std=batchParamsObj.DRM_Batch_Params.STANDARD_EXPORT_NAME.value
Exp_File_Std=batchParamsObj.DRM_Batch_Params.STANDARD_EXPORT_FILE_NAME.value
Exp_LogFile_Std=batchParamsObj.DRM_Batch_Params.STANDARD_EXP_LOG_FILE.value
    #  Call export by name function
drmBatchObj.SPC_RunExpByNameStd(Export_Name_Std,Exp_File_Std,Exp_LogFile_Std) 
 
#  Export By Name   - Access Group
Exp_Name_AccGrp=batchParamsObj.DRM_Batch_Params.ACCESSGRP_EXPORT_NAME.value
Exp_File_AccGrp=batchParamsObj.DRM_Batch_Params.ACCESSGRP_EXPORT_FILE_NAME.value
Exp_LogFile_AccGrp=batchParamsObj.DRM_Batch_Params.ACCESSGRP_EXP_LOG_FILE.value
AccessGrp_Name= batchParamsObj.DRM_Batch_Params.EXPORT_ACCESS_GRP.value
    #  Call export function
drmBatchObj.SPC_RunExpByNameAGrp(Exp_Name_AccGrp,Exp_File_AccGrp,Exp_LogFile_AccGrp,AccessGrp_Name)

 #  Book By Name   - Standard Export
Book_Name_Std=batchParamsObj.DRM_Batch_Params.STANDARD_BOOK_NAME.value
Book_File_Std=batchParamsObj.DRM_Batch_Params.STANDARD_BOOK_FILE_NAME.value
Book_LogFile_Std=batchParamsObj.DRM_Batch_Params.STANDARD_BOOK_LOG_FILE.value
    #  Call Book by name function
drmBatchObj.SPC_RunBookByNameStd(Book_Name_Std,Book_File_Std,Book_LogFile_Std)

#  Book By Name   - Access Group
Book_Name_AccGrp=batchParamsObj.DRM_Batch_Params.ACCESSGRP_BOOK_NAME.value
Book_File_AccGrp=batchParamsObj.DRM_Batch_Params.ACCESSGRP_BOOK_FILE_NAME.value
Book_LogFile_AccGrp=batchParamsObj.DRM_Batch_Params.ACCESSGRP_BOOK_LOG_FILE.value
Book_AccessGrp=batchParamsObj.DRM_Batch_Params.BOOK_ACCESS_GRP.value
    #  Call export by name function
drmBatchObj.SPC_RunBookByNameAGrp(Book_Name_AccGrp,Book_File_AccGrp,Book_LogFile_AccGrp,Book_AccessGrp)

#  Action Script - Pipe seperated file
ActionScript_File_Name=batchParamsObj.DRM_Batch_Params.ACTIONSCRIPT_FILE_NAME.value
ActionScript_LogFile=batchParamsObj.DRM_Batch_Params.STANDARD_EXP_LOG_FILE.value
strFileDelimiter=batchParamsObj.DRM_Batch_Params.FILE_DELIMITER.value
    #  Call action script
drmBatchObj.SPC_RunActionScript(ActionScript_File_Name,strFileDelimiter,ActionScript_LogFile)