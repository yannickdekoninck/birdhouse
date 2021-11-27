# Birdhouse

## Objective

We're trying to build a bird house with an IR camera + light inside so we can look at the birds without disturbing them.

For this to work we need to:

- capture images/video/live feed from the camera
- control the intensity of the LED (automatically?)


## Setting up the pi

Flash an SD card with `buster`: https://downloads.raspberrypi.org/raspios_armhf/images/raspios_armhf-2021-05-28/2021-05-07-raspios-buster-armhf.zip

```
sudo apt update
sudo apt full-upgrade
sudo reboot
```

After the reboot

```
curl -sSL https://get.docker.com | sh
```

### setting up ssh

https://dev.to/s1ntaxe770r/how-to-setup-ssh-within-a-docker-container-i5i

https://www.cloudsavvyit.com/13937/how-to-ssh-into-a-docker-container/