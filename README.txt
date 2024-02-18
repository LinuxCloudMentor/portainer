# Start Portainer container
podman pull portainer/portainer-ce:2.19.4
podman run  -d -p 9443:9443 --restart=always --name portainer --privileged -v /run/podman/podman.sock:/var/run/docker.sock:Z docker.io/portainer/portainer-ce:2.19.4



# Start Prometheus container
podman pull bitnami/prometheus:2.49.1
podman volume create prometheus-data && podman volume create prometheus-data-file
podman run -d -p 9090:9090 --restart=always --name prometheus -v prometheus-data-file:/opt/bitnami/prometheus -v prometheus-data:/prometheus bitnami/prometheus:2.49.1

# start grafana
podman pull grafana/grafana:10.2.4
podman volume create grafana-storage
podman run -d -p 3000:3000 --restart=always --name grafana -v grafana-storage:/var/lib/grafana grafana/grafana:10.2.4