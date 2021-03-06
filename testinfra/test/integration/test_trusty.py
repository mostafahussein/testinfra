# -*- coding: utf8 -*-
# Copyright © 2015 Philippe Pepiot
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import unicode_literals

import itertools

import pytest

pytestmark = pytest.mark.integration
testinfra_hosts = [
    "%s://ubuntu_trusty?sudo=%s" % (b_type, sudo)
    for b_type, sudo in itertools.product(
        ["ssh", "paramiko", "safe-ssh", "docker"],
        ["true", "false"],
    )
]


def test_ssh_package(Package):
    ssh = Package("openssh-server")
    assert ssh.is_installed
    assert ssh.version == "1:6.6p1-2ubuntu2"


def test_ssh_service(Service):
    ssh = Service("ssh")
    assert ssh.is_running
    assert ssh.is_enabled


def test_systeminfo(SystemInfo):
    assert SystemInfo.type == "linux"
    assert SystemInfo.release == "14.04"
    assert SystemInfo.distribution == "ubuntu"
    assert SystemInfo.codename == "trusty"
