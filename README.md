# SolarServers
How to test:
1. Download project to local system
2. Inside main folder, open terminal and run
# "uvicorn SolarServers_server:app --port 8000"
3. Inside frontend, open terminal and run
# "python -m http.server 8000"
4.Inside backend.py ,open terminal and run
# "uvicorn backend:app"
5.Backend runs on: # "http://127.0.0.1:8000/docs"
6. In browser, specifically go to
<br>
# "http://localhost:8000 or http://localhost:8000/"
7. DO NOT directly open index.html.

> On top left, a small green square will appear. It is the placeholder for HUD

# Changelog
1. Added planets to show connections to sites via browser
2. Added on-click shown tooltips for planets, showing connection details
