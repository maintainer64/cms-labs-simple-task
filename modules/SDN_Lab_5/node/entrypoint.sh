#!/usr/bin/env bash
set -euo pipefail

ssh-keygen -A
/usr/sbin/sshd
/usr/sbin/snmpd -C -c /etc/snmp/snmpd.conf -Lo

exec python3 /usr/local/bin/lab-agent
