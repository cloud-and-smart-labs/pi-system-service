# Background Services for Sensing and Actuation

## Table of Contents
- [Creating Service](#creating-service)
- [Check Service Status](#check-service-status)
- [Service Restart](#service-restart)
- [Delete Service](#delete-service)

## Creating Service
Move the service to the system directory
```bash
sudo mv ~/pi-system-service/service_name.service /etc/systemd/system/service_name.service
```

Reload the systemctl daemon
```bash
sudo systemctl daemon-reload
```

Enable the service
```bash
sudo systemctl enable service_name.service
```

Start the service
```bash
sudo systemctl start service_name.service
```


## Check Service Status
Service status
```bash
sudo systemctl status service_name.service
```


## Service Restart
Service restart
```bash
sudo systemctl restart dht11.service
```


## Delete Service
Stop the service
```bash
sudo systemctl stop dht11.service
```

Remove the service
```bash
sudo rm /etc/systemd/system/dht11.service
```