Usage
=====

First export the environment variable with the database:connection value from your keystone.conf:

    $ export DB_CONNECTION="sqlite://keystone"

Now just execute the python module:

    $ python keystone-dbshell

Now try to list the roles:

    >> from keystone.assignment.backends import sql as sql_assign
    >> from keystone.common import driver_hints
    >> a = sql_assign.Assignment()
    >> hints = driver_hints.Hints()
    >> a.list_roles(hints)
