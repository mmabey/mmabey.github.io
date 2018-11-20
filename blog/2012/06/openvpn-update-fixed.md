```eval_rst
:heading: /var/log/mike
:subheading: Mike's Blog
:doc_type: blog

:orig_link: https://mikemabey.blogspot.com/2012/06/openvpn-update-fixed.html
:tags: Linux, Linux administration, networking, OpenVPN, Precise Pangolin, Ubuntu, Ubuntu 12.04, VPN
:day: 6
:month: 6
:year: 2012
:title: OpenVPN Update: Fixed!
:datePublished: 2012-06-06T00:00:00
:dateModified: 2012-06-06T00:00:00
```
# OpenVPN Update: Fixed!

I finally had time to really do some more troubleshooting on the [OpenVPN
problem](/blog/2012/05/troubles_with_openvpn.md) I recently posted about. After trying some of the same old things to
get the server to be able to access the Internet and have the VPN service running at the same time, I decided it was
time to purge the installation and start fresh:

```
sudo apt-get purge openvpn
```

No fun. It's always depressing when a configuration problem gets to the point where the only thing left you can think
to try is to start over from scratch. I did have the good sense to back up all the server's keys and configuration
files, which in the long run did end up being useful.

As I was once again going through the [OpenVPN tutorial](https://help.ubuntu.com/12.04/serverguide/openvpn.html)
provided by Ubuntu and scanning through the help comments in /etc/openvpn/server.conf, when I found the following:

> Use "dev tap0" if you are ethernet bridging and have precreated a tap0 virtual interface and bridged it with your
  ethernet interface.

For a while, I *mistakenly* thought that this might be the answer I was looking for, since it seemed like that was what I
was doing, but only because I didn't understand everything that was going on under the hood as well as I do now. You
see, when the tutorial has you add the line:

```
up "/etc/openvpn/up.sh br0 eth1"
```

this isn't exactly what is called to bring up the bridged interfaces. Taking another look at the `up.sh` script, there
are three network interface devices referenced, even though only two are explicitly given in the configuration line
above. OpenVPN adds the necessary `tap0` device to the system, and then adds its interface name as a parameter to the
end of the string you specify.

A minimum of three interfaces are needed to create a bridge of the sort that OpenVPN needs: 1) the physical interface
with access to the "real world" through which the VPN traffic will initially come in, 2) the destination interface which
is actually handled by OpenVPN, and 3) the bridging interface that connects the first two at the kernel level.

As I was figuring out all this, I thought to check the man page of `brctl` since I knew that the `up.sh` script called
by OpenVPN as it starts up uses `brctl` to do the kernel-level changes to bridge `eth1` and `tap0`. Once I really
started to understand how the various options worked, I tried refreshing the bridged interface by calling `brctl`
`dellbr` `br0` and then `brctl addbr br0`, followed by restarting the openvpn service.

Doing this had positive results, but none of them persisted through a reboot of the machine. Finally, after trying
several different things, I came up with hard-coding a refresh of the bridged interface in the `up.sh` script. This,
plus changing the network configuration of `eth0` from `static` to `dhcp` seems to have done the trick. The machine has
access to the Internet, and clients can connect just as they could before. I even copied over the old configuration,
certificate, and key files, which prevented me from having to re-issue all the client keys and re-distributing the
server's certificate.

The new contents of my `up.sh` script are below:

    #!/bin/sh
    
    BR=$1
    ETHDEV=$2
    TAPDEV=$3
    
    # Reset the bridge device first
    /sbin/ip link set "$BR" down
    /sbin/brctl delbr $BR
    /sbin/brctl addbr $BR
    /sbin/brctl addif $BR $ETHDEV
    
    /sbin/ip link set "$TAPDEV" up
    /sbin/ip link set "$ETHDEV" promisc on
    /sbin/brctl addif $BR $TAPDEV
