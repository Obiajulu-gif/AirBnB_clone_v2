#!/usr/bin/python3
"""
Fabric script to genereate tgz archive
"""


from fabric.api import local
from datetime import datetime


def do_pack():
    local("mkdir -p versions")
    time_format = "%Y%m%d%H%M%S"
    current_time = datetime.utcnow().strftime(time_format)
    archive_name = "versions/web_static_{}.tgz".format(current_time)
    result = local("tar -cvzf {} web_static".format(archive_name))
    if result.failed:
        return None
    else:
        return archive_name


if __name__ == "__main__":
    do_pack()
