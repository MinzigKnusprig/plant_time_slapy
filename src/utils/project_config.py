class Project_Config:
    cred = None
    bucket_name = None
    bucket_folder_name = None
    img_type = None
    img_number = None
    start_date = None

    def __init__(self,cred,bucket_name,bucket_folder_name,img_file,img_type,start_date,img_number):
        self.cred = cred
        self.bucket_name = bucket_name
        self.bucket_folder_name = bucket_folder_name
        self.img_file = img_file
        self.img_number = img_number
        self.img_type = img_type
        self.start_date = start_date