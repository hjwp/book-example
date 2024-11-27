#!/bin/bash
set -ex

ansible-playbook --user=elspeth -i staging.ottg.co.uk, infra/deploy-playbook.yaml -vv
