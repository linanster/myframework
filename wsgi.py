# coding:utf8
#
from app import create_app
import sys

print('==sys.version==',sys.version)
print('==sys.executable==',sys.executable)

application_framework = create_app()

@application_framework.template_global('now')
def get_now_timestamp():
    import time
    return time.time()

@application_framework.template_filter('timeformat')
def timeformat(timestamp):
    import time
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timestamp))


if __name__ == '__main__':
    application_framework.run(host='0.0.0.0', port=5000, debug=True)
