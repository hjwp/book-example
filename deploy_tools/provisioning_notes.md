Provisioning a new site
=======================

## Using ansible

    ansible-playbook -i ansible.inventory provision.ansible.yaml --limit=staging

For localhost where sudo needs a password, add the flag `--ask-sudo-pass`

    ansible-playbook -i ansible.inventory provision.ansible.yaml --limit=local --ask-sudo-pass

## Folder structure:
Assume we have a user account at /home/username

/home/username
└── sites
    └── SITENAME
         ├── database
         ├── source
         ├── static
         └── virtualenv
