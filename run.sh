#!/usr/bin/env bash
    
source venv/bin/activate
if [ ! -f /tmp/surl.db ]
  then
    cd surls; python -c 'import app; app.init_db()'
fi
python surls/app.py
deactivate

