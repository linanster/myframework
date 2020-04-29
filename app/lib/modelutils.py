from app.models.sqlite import Sysinfo

def get_running():
    record = Sysinfo.query.filter_by(key='r_running').first()
    return record.field1
