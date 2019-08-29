# Sprig Creations - 8/9/2019
# Assign batch required details for exports, books and actionscripts
import sys
from enum import Enum
class DRM_Batch_Params(Enum):
# Standard Export
 STANDARD_EXPORT_NAME='Account_Hier_Exp'
 STANDARD_EXPORT_FILE_NAME=r'C:\DRM_Batch_Python\log_exp\Std_Account_hier_exp.txt'
 STANDARD_EXP_LOG_FILE=r'C:\DRM_Batch_Python\log_exp\drmBatch_run.log'

 # Access Group Export
 EXPORT_ACCESS_GRP='"Oracle General Ledger"'
 ACCESSGRP_EXPORT_NAME='ORCL_GL_Account_Hier_Exp'
 ACCESSGRP_EXPORT_FILE_NAME=r'C:\DRM_Batch_Python\log_exp\ORCL_GL_Account_Hier_exp.txt'
 ACCESSGRP_EXP_LOG_FILE=r'C:\DRM_Batch_Python\log_exp\drmBatch_run.log'

 # Standard Book
 STANDARD_BOOK_NAME='Account_Book_Std'
 STANDARD_BOOK_FILE_NAME=r'C:\DRM_Batch_Python\log_exp\Std_Account_hier_bk.txt'
 STANDARD_BOOK_LOG_FILE=r'C:\DRM_Batch_Python\log_exp\drmBatch_run.log'

 # Access Group Book
 BOOK_ACCESS_GRP='"Oracle General Ledger"'
 ACCESSGRP_BOOK_NAME='Account_Book_ORCL_GL'
 ACCESSGRP_BOOK_FILE_NAME=r'C:\DRM_Batch_Python\log_exp\ORCL_Account_Hier_bk.txt'
 ACCESSGRP_BOOK_LOG_FILE=r'C:\DRM_Batch_Python\log_exp\drmBatch_run.log'

 # Action Script
 ACTIONSCRIPT_FILE_NAME=r'C:\DRM_Batch_Python\update_accounts.txt'
 ACTIONSCRIPT_LOG_FILE=r'C:\DRM_Batch_Python\log_exp\drmBatch_run.log'
 FILE_DELIMITER='#124'