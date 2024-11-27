#!/bin/bash
set -ex

ansible-playbook --user=elspeth -i www.ottg.co.uk, infra/deploy-playbook.yaml -vv
