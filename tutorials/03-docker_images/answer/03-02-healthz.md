
```shell
# Create the script on your VM, or copy it using scp, Winscp, etc.

# On the VM copy the healthz.py script inside the container
docker cp healthz.py new-container:.

# Check the script is available within the container
docker exec new-container ls
# bin
# boot
# dev
# etc
# healthz.py
# home
# ...

# If you try to run the command right now you will get an error because you need python3 and aiohttp package
docker exec new-container python3 /healthz.py
# OCI runtime exec failed: exec failed: container_linux.go:380: starting container process caused: exec: "python3": executable file not found in $PATH: unknown
```

Install needed dependencies on the container.

```shell
# Install dependencies
docker exec -ti new-container bash

apt-get update
# Install python3 basic dev env and curl
apt-get install python3 python3-pip curl

# Install aiohttp web server python package
pip3 install aiohttp

# Check the installation went well
python3 healthz.py 
#======== Running on http://0.0.0.0:8080 ========
#(Press CTRL+C to quit)

# Exit the container
exit
```

You can see that by default the web server is listening on port 8080, now run the
server through docker.

```shell
# Run the server within the container
docker exec -d new-container python3 healthz.py

# Check it is running
docker exec new-container ps 
#    PID TTY          TIME CMD
#      1 ?        00:00:00 bash
#   3924 ?        00:00:00 python3
#   3946 ?        00:00:00 ps

# Run a command to fetch the URL
docker exec new-container curl -v http://localhost:8080/healthz
#% Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
#                                 Dload  Upload   Total   Spent    Left  Speed
#  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0*   Trying 127.0.0.1:8080...
#* TCP_NODELAY set
#* Connected to localhost (127.0.0.1) port 8080 (#0)
#> GET /healthz HTTP/1.1
#> Host: localhost:8080
#> User-Agent: curl/7.68.0
#> Accept: */*
#> 
#* Mark bundle as not supporting multiuse
#< HTTP/1.1 200 OK
#< Content-Length: 0
#< Content-Type: application/octet-stream
#< Date: Mon, 14 Mar 2022 09:46:08 GMT
#< Server: Python/3.8 aiohttp/3.8.1
#< 
#  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
#* Connection #0 to host localhost left intact


# The HTTP/1.1 200 OK means the HTTP command worked
```










