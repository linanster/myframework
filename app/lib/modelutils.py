from app.models.sqlite import db_sqlite, Sysinfo, Student, User, StatsCount

def get_running():
    record = Sysinfo.query.filter_by(key='r_running').first()
    return record.field1

def get_visitcount():
    record = StatsCount.query.filter_by(metric='visitcount').first()
    return record.count

def add_visitcount():
    record = StatsCount.query.filter_by(metric='visitcount').first()
    record.count += 1
    db_sqlite.session.commit()
    return record.count

