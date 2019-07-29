#! /usr/bin/env python3

import os
import webbrowser

import pexpect

docker_cmd = pexpect.spawn(
    'docker',
    [
        'run',
        '-p', '8888:8888',
        '-e', 'JUPYTER_ENABLE_LAB=yes',
        '-v', '{}:/home/jovyan/'.format(os.getcwd()),
        '--user', str(os.getuid()),
        '--group-add', 'users',
        'zillow_docker',
    ]
)

docker_cmd.expect([r'http://\(.*\):8888/\?token=([0-9a-f]+)'])
token = docker_cmd.match.group(1).decode('utf_8')

webbrowser.open_new_tab(f'http://localhost:8888/?token={token}')

docker_cmd.interact()
