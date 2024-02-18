import subprocess

# Define commands to execute
commands = [
    "subscription-manager repos --enable codeready-builder-for-rhel-9-$(arch)-rpms",
    "dnf install -y https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm",
    "sudo dnf install -y prometheus-podman-exporter",
    "systemctl start prometheus-podman-exporter.service",
    "systemctl enable prometheus-podman-exporter.service",
    "netstat -tlpn | grep prometheus-po"
]

# Execute commands and print their outputs
for command in commands:
    print(f"Executing command: {command}")
    try:
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, text=True)
        print(output)
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")

