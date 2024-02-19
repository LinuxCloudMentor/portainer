import subprocess

def start_portainer(version, container_tool):
    command = f"{container_tool} pull portainer/portainer-ce:{version}"
    subprocess.run(command, shell=True)
    
    if container_tool == "podman":
        command = f"{container_tool} run -d -p 9443:9443 --restart=always --name portainer --privileged -v /run/podman/podman.sock:/var/run/docker.sock:Z docker.io/portainer/portainer-ce:{version}"
    elif container_tool == "docker":
        command = f"{container_tool} run -d -p 9443:9443 --restart=always --name portainer --privileged -v /var/run/docker.sock:/var/run/docker.sock portainer/portainer-ce:{version}"
    else:
        print("Invalid container tool. Please choose either 'podman' or 'docker'.")
        return
    
    print(f"Starting Portainer container ({container_tool}) with version {version}...")
    subprocess.run(command, shell=True)

def start_prometheus(version, container_tool):
    command = f"{container_tool} pull bitnami/prometheus:{version}"
    subprocess.run(command, shell=True)
    
    if container_tool == "podman":
        volume_command = f"{container_tool} volume create prometheus-data && {container_tool} volume create prometheus-data-file"
        run_command = f"{container_tool} run -d -p 9090:9090 --restart=always --name prometheus -v prometheus-data-file:/opt/bitnami/prometheus -v prometheus-data:/prometheus bitnami/prometheus:{version}"
    elif container_tool == "docker":
        volume_command = f"{container_tool} volume create prometheus-data && {container_tool} volume create prometheus-data-file"
        run_command = f"{container_tool} run -d -p 9090:9090 --restart=always --name prometheus -v prometheus-data-file:/opt/bitnami/prometheus -v prometheus-data:/prometheus bitnami/prometheus:{version}"
    else:
        print("Invalid container tool. Please choose either 'podman' or 'docker'.")
        return
    
    print(f"Creating volumes for Prometheus container ({container_tool})...")
    subprocess.run(volume_command, shell=True)
    
    print(f"Starting Prometheus container ({container_tool}) with version {version}...")
    subprocess.run(run_command, shell=True)

def start_grafana(version, container_tool):
    command = f"{container_tool} pull grafana/grafana:{version}"
    subprocess.run(command, shell=True)
    
    if container_tool == "podman":
        volume_command = f"{container_tool} volume create grafana-storage"
        run_command = f"{container_tool} run -d -p 3000:3000 --restart=always --name grafana -v grafana-storage:/var/lib/grafana grafana/grafana:{version}"
    elif container_tool == "docker":
        volume_command = f"{container_tool} volume create grafana-storage"
        run_command = f"{container_tool} run -d -p 3000:3000 --restart=always --name grafana -v grafana-storage:/var/lib/grafana grafana/grafana:{version}"
    else:
        print("Invalid container tool. Please choose either 'podman' or 'docker'.")
        return
    
    print(f"Creating volume for Grafana container ({container_tool})...")
    subprocess.run(volume_command, shell=True)
    
    print(f"Starting Grafana container ({container_tool}) with version {version}...")
    subprocess.run(run_command, shell=True)

def main():
    portainer_version = input("Enter the version for Portainer container (e.g., 2.19.4): ")
    prometheus_version = input("Enter the version for Prometheus container (e.g., 2.49.1): ")
    grafana_version = input("Enter the version for Grafana container (e.g., 10.2.4): ")
    container_tool = input("Which container tool to use (podman/docker): ").lower()
    
    start_portainer(portainer_version, container_tool)
    start_prometheus(prometheus_version, container_tool)
    start_grafana(grafana_version, container_tool)

if __name__ == "__main__":
    main()

