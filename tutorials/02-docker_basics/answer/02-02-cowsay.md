
First open a shell on the currently running container and install cowsay.

```shell
# Go to the container
docker exec -ti my-container bash

# Now run the installation of cow say
sudo apt-get update
sudo apt-get install -y cowsay

# Try the command
/usr/games/cowsay hello
#root@150c130b8751:/# /usr/games/cowsay  hello
# _______
#< hello >
# -------
#        \   ^__^
#         \  (oo)\_______
#            (__)\       )\/\
#                ||----w |
#                ||     ||

# exit the container
exit
```

