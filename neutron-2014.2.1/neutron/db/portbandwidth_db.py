# Copyright 2015 Suning, Inc.  All rights reserved.
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

import sqlalchemy as sa
from sqlalchemy import orm
from sqlalchemy.orm import exc

from neutron.api.v2 import attributes as attrs
from neutron.db import db_base_plugin_v2
from neutron.db import model_base
from neutron.db import models_v2
from neutron.extensions import portsecurity as psec
from neutron.openstack.common import log as logging

LOG = logging.getLogger(__name__)


class PortBandwidth(model_base.BASEV2):
    port_id = sa.Column(sa.String(36),
                        sa.ForeignKey('ports.id', ondelete="CASCADE"),
                        primary_key=True)
    uplink = sa.Column(sa.BigInteger, nullable=True)
    downlink = sa.Column(sa.BigInteger, nullable=True)


    # Add a relationship to the Port model in order to be to able to
    # instruct SQLAlchemy to eagerly load port security binding
    port = orm.relationship(
        models_v2.Port,
        backref=orm.backref("port_bandwidth", uselist=False,
                            cascade='delete', lazy='joined'))


class PortBandwidthMixin(object):
    """ Mixin class to port bandwith methods to db_base_plugin_v2."""
    pass

