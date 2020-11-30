# Copyright 2020 Alibaba Group Holding Limited. All Rights Reserved.
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
# =============================================================================
"""local training script for unsupervised GraphSage"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import base64
import json
import sys
import graphlearn as gl
import time


def main():
  handle_str = sys.argv[1]
  s = base64.b64decode(handle_str).decode('utf-8')
  handle = json.loads(s)
  handle['pod_index'] = int(sys.argv[2])
  node_type = sys.argv[3]
  edge_type = sys.argv[4]
  for node_info in handle['node_schema']:
    if node_info.split(':')[0] == node_type:
      handle['node_schema'] = [node_info]
  for edge_info in handle['edge_schema']:
    if edge_info.split(':')[1] == edge_type:
      handle['edge_schema'] = [edge_info]
  handle['node_schema'] = ['paper:false:false:0:128:0']
  hosts = handle['hosts'].split(',')
  handle['server'] = ','.join(["{}:{}".format(pod_name, 8000 + index) for index, pod_name in enumerate(hosts[0:])])
  g = gl.init_graph_from_handle(handle, handle['pod_index'])
  print('servers', handle['server'])
  time.sleep(100000)

if __name__ == "__main__":
  main()
