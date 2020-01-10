# STOCK-TRACK

Docker InfluxDb:

```docker run -p 8086:8086       -e INFLUXDB_DB=defaultdb       -e INFLUXDB_ADMIN_USER=admin       -e INFLUXDB_ADMIN_PASSWORD=adminpass       -e INFLUXDB_USER=user       -e INFLUXDB_USER_PASSWORD=userpass       -v influxdb:/var/lib/influxdb       influxdb:latest```

INFLUXDB CLI:
```docker ps```

```docker exec -it CONTAINER_ID /bin/bash```

Docker Grafana:
```docker run -d --name=grafana -p 3000:3000 grafana/grafana```