#!/usr/bin/python3
"""
Fabric script based on the file 1-pack_web_static.py that distributes an
archive to the web servers
"""

from fabric.api import env, run, put
from os.path import exists

env.hosts = ['52.90.22.66', '100.24.238.44']
env.user = 'ubuntu'
env.key_filename = '/root/.ssh/id_rsa'


def do_deploy(archive_path):
    if not exists(archive_path):
        return False

    try:
        put(archive_path, "/tmp/")
        archive_filename = archive_path.split('/')[-1]
        release_path = "/data/web_static/releases/{}".format(archive_filename[:-4])
        run("mkdir -p {}".format(release_path))
        run("tar -xzf /tmp/{} -C {}".format(archive_filename, release_path))
        run("rm /tmp/{}".format(archive_filename))
        run("rm -f /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(release_path))

        return True
    except Exception as e:
        print(e)
        return False


if __name__ == "__main__":
    do_deploy(archive_path="versions/web_static_20170315003959.tgz")
