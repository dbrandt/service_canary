# service_canary

A simple (web) app that checks connectivity to other services. 

That admittedly sounds a bit useless, but is something I use when troubleshooting container deployments or to quickly see if I got the routing right... or messed those security groups in my AWS setup.

## Configuration
Configuration is done via environment variables or command line options. The environment variables looked for look like this:
```
CANARY_DB_<n>_TYPE
CANARY_DB_<n>_USER
CANARY_DB_<n>_PASS
CANARY_DB_<n>_DB_NAME
CANARY_DB_<n>_TEST_QUERY
CANARY_MEMCACHED_<n>
CANARY_RABBITMQ_<n>
```

The <n> denotes a number, this is so you can test several nodes or several different databases at once.
