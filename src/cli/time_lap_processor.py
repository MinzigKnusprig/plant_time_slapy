from src.external.google_cloud_i import Google_Cloud_Interface
from src.external.camera import Camera
from src.utils.days_counter import Day_Counter

class Time_Laps_Processor:
    gcli = None
    camera = None
    project_conf = None
    days_counter = None

    def __init__(self, project_conf):
        self.project_conf = project_conf
        self.gcli = Google_Cloud_Interface(project_conf.cred)
        self.camera = Camera()
        self.days_counter = Day_Counter(project_conf.start_date)

    def start_time_lap(self,project_conf):
        while(True):
            captured_img = self.camera.capture_image()
            self.gcli.add_object_to_bucket(project_conf, captured_img)