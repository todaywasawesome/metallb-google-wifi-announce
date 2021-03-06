# The effects are only temporary 
Unfortunately the effects only work temporarily, eventually Google Wifi starts rerouting traffic based on the MAC address to the wrong ip. The workaround for now is to use an ingress with NodePort then forward to any node. Unfortunately this breaks failover but at least nodes can have static ips. 

# metallb-google-wifi-announce

[![Codefresh build status]( https://g.codefresh.io/api/badges/pipeline/todaywasawesome/Atomic%20Cluster%2Fmetallb-google-wifi-announce?type=cf-1)]( https://g.codefresh.io/public/accounts/todaywasawesome/pipelines/new/608845638eccddd62359b672)

Google Wifi doesn't obey normal ARP announcements made form metallb or other Kubernetes services. This creates a problem when trying to create port forwarding rules in Google Wifi because ingress and services never show up in the UI. 

This project creates a loop that basically spoofs a packet from the ingress ip you want to advertise. Unfourtunately it's not enough to do this once, you must do it constantly or Google Wifi will try to change the forwarding rule to whatever MAC address it has. It may also help to direct inbound traffic to keep the route alive. 

## Usage

### As a python script
```
export HOST_IP=[IP ADDRESS TO ADVERTISE]
export DEST_IP=8.8.8.8
python advertise.py
```

### As a Docker image
`docker run -e HOST_IP=[IP ADDRESS TO ADVERTISE] DEST_IP=[DESTINATION ip, maybe use 8.8.8.8] todaywasawesome/metallb-google-wifi-announce`

### In Kubernetes, K3s etc
Modify the [daemonset yaml](deploy/kubernetes/metallb-google-wifi-announce-daemonset.yaml) with the ip address you want to advertise then apply if with `kubectl apply -f metallb-google-wifi-announce-daemonset.yaml`

## Credits
Special thanks to Etienne Champetier for showing me how to use Scapy. And to Redditor [u/jaygrok for having thread](https://www.reddit.com/r/GoogleWiFi/comments/id5qt9/port_forwarding_metallb/) that was easy to follow and documented the issue. I hope you found a resolution :) 