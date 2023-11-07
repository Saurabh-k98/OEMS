# OEMS
This project uses Python with Django to create a Office Employee Management System

# Adding debug toolcar
- Install package
    - python -m pip install django-debug-toolbar
- Add debug app in installed app in settings.py file
    - "debug_toolbar",
- Import package in main urls.py file
    - import debug_toolbar
- Add URL in URL.PY file
    - path("__debug__/", include(debug_toolbar.urls)),
- In setting.py MIDDLEWARE add
    - "debug_toolbar.middleware.DebugToolbarMiddleware",
- In settings.py add
    - INTERNAL_IPS = ["127.0.0.1",]