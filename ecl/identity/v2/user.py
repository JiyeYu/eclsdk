# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from ecl.identity import identity_service
from ecl import resource


class User(resource.Resource):
    resource_key = 'user'
    resources_key = 'users'
    base_path = '/users'
    service = identity_service.AdminService()

    # capabilities
    allow_create = True
    allow_retrieve = True
    allow_update = True
    allow_delete = True
    allow_list = True

    # Properties
    #: The email of this user. *Type: string*
    email = resource.prop('email')
    #: Setting this value to ``False`` prevents the user from authenticating or
    #: receiving authorization. Additionally, all pre-existing tokens held by
    #: the user are immediately invalidated. Re-enabling a user does not
    #: re-enable pre-existing tokens. *Type: bool*
    is_enabled = resource.prop('enabled', type=bool)
    #: The name of this user. *Type: string*
    name = resource.prop('name')
