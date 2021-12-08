# Raspberry Pi - Services for Sensing and Actuation
---
## Setup
---
### Move the service to the system directory
```bash
sudo mv ~/pi-system-service/dht11.service /etc/systemd/system/dht11.service
```

### Reload the systemctl daemon
```bash
sudo systemctl daemon-reload
```

### Enable the service
```bash
sudo systemctl enable dht11.service
```

### Start the service
```bash
sudo systemctl start dht11.service
```

### Service status
```bash
sudo systemctl status dht11.service
```

### Service restart
```bash
sudo systemctl restart dht11.service
```
<br>

---
## Remove
---
### Stop the service
```bash
sudo systemctl stop dht11.service
```

### Remove the service
```bash
sudo rm /etc/systemd/system/dht11.service
```