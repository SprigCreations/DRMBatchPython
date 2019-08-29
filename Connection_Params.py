# Sprig Creations - 8/9/2019
# Assign connection required details
import sys
from enum import Enum
class DRM_Conn_Params(Enum):
 USER_NAME='drm_batch'
 PASSWORD='*****'
 DRM_CLIENT_PATH=r'C:\Oracle\Middleware\EPMSystem11R1\products\DataRelationshipManagement\client\batch-client\drm-batch-client.exe'
 DRM_APP_URL='net.tcp://localhost:5210/Oracle/Drm/Engine'
 VERSION_NAME='CurrentVersion'