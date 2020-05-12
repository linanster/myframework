from app.models.sqlite import db_sqlite, Sysinfo

def get_running():
    record = Sysinfo.query.filter_by(key='r_running').first()
    return record.field1

def get_visitcount():
    record = Sysinfo.query.filter_by(key='r_visitcount').first()
    return record.field2

def add_visitcount():
    record = Sysinfo.query.filter_by(key='r_visitcount').first()
    record.field2 += 1
    db_sqlite.session.commit()
    return record.field2
