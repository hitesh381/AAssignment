Created server using python which consists in file server.py

Wrote client using bash api curl as it gave me flexibility in listening to log file and ssh-events which i was having trouble to do in python (could've been a bit more time consuming)

1) Run server first 
2) setup client script on host machines and keep them running - advisable to set it over crontab or systemd service file
3) whenever someone logs in to the client machine a ssh login event is greped by our tail -f cmd which in turn writes the same in another logfile and we're using the same as counter and whenever the script is executed we count the line of log file which is basically our counter here and we trigger curl api on every event received 


Created Dockerfile for the server
 
 
Wrote required yaml and helm charts for the same

Use "helm upgrade -f myvalues.yaml -f override.yaml assignment-helm ./assignment-helm" to upgrade the application after switching to dev



PS: This project/assignment has lot of room to improve and develop, thanks
