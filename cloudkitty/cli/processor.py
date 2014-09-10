# -*- coding: utf-8 -*-
# Copyright 2014 Objectif Libre
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
#
# @author: Stéphane Albert
#
from oslo.config import cfg

from cloudkitty.common import rpc
from cloudkitty.openstack.common import log as logging
from cloudkitty import orchestrator
from cloudkitty import service

LOG = logging.getLogger(__name__)

CONF = cfg.CONF


def main():
    service.prepare_service()
    rpc.init()
    processor = orchestrator.Orchestrator()
    try:
        processor.process()
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()