Provisioning a new site
=======================

## Using ansible

    ansible-playbook -i ansible.inventory provision.ansible.yaml --limit=staging

## Folder structure:
Assume we have a user account at /home/username

/home/username
└── sites
    └── SITENAME
         ├── database
         ├── source
         ├── static
         └── virtualenv
