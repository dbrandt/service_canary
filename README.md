# service_canary

A simple (web) app that checks connectivity to other services. 

That admittedly sounds a bit useless, but is something I use when troubleshooting container deployments or to quickly see if I got the routing right... or messed those security groups in my AWS setup.

## Prerequisites
The only real requirement is `requests`. Of course, then you can only test API connectivity.

Beyond API testing you might want to install: 
* if you want to test RabbitMQ
* `psycopg2` if you want to test PostgreSQL
* `riak` if you want to test Riak/RiakTS
* `python-memcache` if you wan to test `memcached`

## Configuration
Configuration is done via environment variables or command line options. The environment variables looked for look like this:
```
CANARY_DB_<n>_TYPE
CANARY_DB_<n>_HOST
CANARY_DB_<n>_PORT
CANARY_DB_<n>_USER
CANARY_DB_<n>_PASS
CANARY_DB_<n>_DB_NAME
CANARY_DB_<n>_TEST_QUERY
CANARY_API_<n>_URL
CANARY_API_<n>_TOKEN
CANARY_API_<n>_ENDPOINT
CANARY_MEMCACHED_HOST
CANARY_MEMCACHED_PORT
CANARY_RABBITMQ_HOST
CANARY_RABBITMQ_PORT
```

The <n> denotes a number, this is so you can test several nodes or several databases at once. You translate this to command line arguments by stripping the `CANARY_` prefix and making it lowercase: `CANARY_DB_1_TYPE` becomes `--db-1-type` and so on.

### Databases
Valid values for database type at this point:
* `postgres` (PostgreSQL)
* `riak` (Riak/RiakTS)

The test query and db name setting is optional. If you leave them out, the code will connect and issue a `SELECT 1` for SQL-databases or a `ping` for Riak.
