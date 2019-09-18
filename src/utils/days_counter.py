from datetime import datetime

class Day_Counter:
    date_format = None
    start_day = None

    def __init__(self,start_date):
        self.init_start_date(start_date)

    def init_start_date(self,start_date):
        self.date_format = "%m/%d/%Y"
        self.start_day = datetime.strptime(start_date, self.date_format)

    def get_current_project_day(self):
        current_day = datetime.today()
        project_day = current_day - self.start_day

        return project_day
