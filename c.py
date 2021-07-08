import time
import os
import mysql.connector as mysql
import json
from obs import *

##### OBS Huawei
AK = 'MKS9H7VLE3B556QLIMDB'
SK = 'GUvX5vSrECTayt0IKQHWdYeU2DYFKWdeoDpFoLp9'
SERVER = 'https://obs.ap-southeast-3.myhuaweicloud.com'
BUCKET = 'smart-access'

obsClient = ObsClient(access_key_id = AK,
                      secret_access_key = SK,
                      server = SERVER)

MYDB = mysql.connect(
    host = '114.119.183.27',
    user = 'root',
    password = 'SmartAccess!',
    database = 'smart_access_db'
)

def generate_presigned_url(mydb, client_method, expires_in):
    # Constructs a obs client instance with your account for accessing OBS
    cursor = mydb.cursor(buffered=True)
    cursor.execute('SELECT doc_image_path FROM users')
    for path in cursor:
        url = obsClient.createSignedUrl( # ObsClient.createSignedUrl
            method=client_method, # Method = GET
            bucketName = BUCKET,
            objectKey = path[0],
            # BucketName = smart-access / ObjectKey = path[0] / expires = 2592000
            expires = expires_in
        )
        URL1.append(url.signedUrl)

    dict1={}
    for i in range(0,len(URL1)):
        dict1[i]=URL1[i]
    filePath1 = 'data.json'

    if os.path.exists(filePath1):
        os.remove(filePath1)

    myfile1 = open('data.json', 'w+')

    # create your dict
    json.dump(dict1, myfile1)
    myfile1.close()
    mydb.commit()

    ###### SELFIE IMAGE PART
    cursor1 = mydb.cursor(buffered=True)
    cursor1.execute('SELECT selfie_image_path FROM users')
    for path in cursor1:
        url3 = obsClient.createSignedUrl(
            method=client_method,
            bucketName = BUCKET,
            objectKey = path[0],
            expires = expires_in
        )
        URL2.append(url3.signedUrl)

    dict2 = {}
    for i in range(0, len(URL2)):
        dict2[i] = URL2[i]
    filePath = 'data1.json'

    if os.path.exists(filePath):
        os.remove(filePath)

    myfile = open('data1.json', 'w+')

    # create your dict

    json.dump(dict2, myfile)
    myfile.close()
    mydb.commit()
######## End

while True:

    URL1 = []
    URL2 = []
    # logger = logging.getLogger(__name__)
    METHOD = 'GET'
    EXPIRES_IN = 30
    generate_presigned_url(mydb = MYDB, client_method = METHOD, expires_in = EXPIRES_IN)
    time.sleep(EXPIRES_IN)
