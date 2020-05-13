from flask_caching import Cache

import os

from app.myglobals import cachefolder

#cache = Cache(config={'CACHE_TYPE': 'simple'})



cache = Cache(config={
    'CACHE_TYPE': 'filesystem',
    'CACHE_DIR': cachefolder,
    'CACHE_THRESHOLD': 10000,
    'CACHE_DEFAULT_TIMEOUT': 600,
})
