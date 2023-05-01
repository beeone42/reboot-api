# reboot-api

Reboot service to be called by uptime-kuma webhook notification, filters to reboot only on monitor failure

Installation:

```
sudo apt install python3-pip
pip3 install -r requirements.txt
python3 app.py
```

Run with supervisord:

```
sudo apt install -y supervisor
sudo cp supervisord/reboot-api.conf /etc/supervisor/conf.d/
sudo supervisorctl reload
sudo supervisorctl status
```
