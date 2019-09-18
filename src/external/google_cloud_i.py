from os import environ
from google.cloud import storage


class Google_Cloud_Interface:
    client_access = None
    bucket_access = None
    project_conf = None

    def __init__(self,project_conf):
        self.project_conf = project_conf
        self.init_credential_environ(self.project_conf.cred)

    def init_credential_environ(self,credential_path):
        environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

    def add_object_to_bucket(self,project_conf,img_file):
        self.init_bucket_access(project_conf.bucket_name)

        blob = self.bucket_access.blob('img2.jpg')

        blob.upload_from_filename(img_file)

    def init_bucket_access(self,bucket_name):
        self.client = storage.Client()
        self.bucket = self.client.get_bucket(bucket_name)


'''
credential_path = '/home/vizhan/Documents/private/PiKalle/Paprika and Cucumber Project-859993cce3b3.json'





'''
