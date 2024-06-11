# python_meetup_ansible_demo

Demo code for "An Evening of Python Coding" event hosted by the Austin Python Meetup group on Jun 18, 2024.

Link to the presentation [here]().

The topic of this presentation is to demonstrate the use of [Ansible](https://docs.ansible.com/ansible/latest/index.html) 
to automate the deployment of distributed applications.

This demo code consist of two parts each contained in a folder:

1. `tutor_site`: Contains a simple Django Application resulting of following the Django tutorial.
2. `deployment`: Contains ansible files needed to deploy the application as well as Vagrant files.

--------------------------------------------------------------------

## The application to be deployed - tutor_site

This is a demo Django application created from following Django official tutorial.

This application should be as simple as possible while still introducing beginners to the most basic Django concepts.

Links to the tutorial sections we followed:

- Part 1: Requests and responses [https://docs.djangoproject.com/en/5.0/intro/tutorial01/](https://docs.djangoproject.com/en/5.0/intro/tutorial01/)
- Part 2: Models and the admin site [https://docs.djangoproject.com/en/5.0/intro/tutorial02/](https://docs.djangoproject.com/en/5.0/intro/tutorial02/)
- Part 3: Views and templates [https://docs.djangoproject.com/en/5.0/intro/tutorial03/](https://docs.djangoproject.com/en/5.0/intro/tutorial03/)
- Part 4: Forms and generic views [https://docs.djangoproject.com/en/5.0/intro/tutorial04/](https://docs.djangoproject.com/en/5.0/intro/tutorial04/)
- Part 5: Testing [https://docs.djangoproject.com/en/5.0/intro/tutorial05/](https://docs.djangoproject.com/en/5.0/intro/tutorial05/)
- Part 6: Static files [https://docs.djangoproject.com/en/5.0/intro/tutorial06/](https://docs.djangoproject.com/en/5.0/intro/tutorial06/)
- Part 7: Customizing the admin site [https://docs.djangoproject.com/en/5.0/intro/tutorial07/](https://docs.djangoproject.com/en/5.0/intro/tutorial07/)
- Part 8: Adding third-party packages [https://docs.djangoproject.com/en/5.0/intro/tutorial08/](https://docs.djangoproject.com/en/5.0/intro/tutorial08/)

### Running the app in local development mode (never use this in production):

Run the local development web server: `$ python manage.py runserver`

Then:

- If you go to `http://127.0.0.1:8000/` you will get a 404 because no url pattern matches the root url. This is a bit confusing, I know, but I'm following the official Django Tutorial steps.
- To access the Polls app navigate to: `http://127.0.0.1:8000/polls/` . This app demonstrates using functional views, has limited tests but does customize the admin interface.
- To access the admin interface: `http://127.0.0.1:8000/admin/` . The admin interface has been customized for the polls app. Admin customizations include the admin question list view: `http://localhost:8000/admin/polls/question/` and also the question detail view: `http://localhost:8000/admin/polls/question/2/change/`.


### Access the Django app deployed in Vagrant

- If you go to `http://orc-app1.test:8080/` you will get a 404 because no url pattern matches the root url. This is a bit confusing, I know, but I'm following the official Django Tutorial steps.
- To access the Polls app navigate to: `http://orc-app1.test:8080/polls/` . This app demonstrates using functional views, has limited tests but does customize the admin interface.
- To access the admin interface: `http://orc-app1.test:8080/admin/` . To log in use the credentials provided in the next section (they come from the original sql data dump file I included in the deployment scripts).


### Admin user

Part of this demo app customizes a view in Django's [admin interface](https://docs.djangoproject.com/en/5.0/ref/contrib/admin/).

In order to access the admin interface you need to create a user with administration rights:

```text
$ python manage.py createsuperuser

user: admin
email: admin@tutorsiteapp.net
pass: Gr3enM0nkeyL4tte%_
```

**Never commit your credentials to Github!**!!!
The password above is needed for us to demonstrate accessing the admin interface on our virtualized vagrant app server during the demo.
The app server will only be accessible from localhost. 
Please, change this password if you want to run this demo in your own machine.


--------------------------------------------------------------------

## The deployment folder

This folder contains everything related to our Ansible deployment logic. This is not part of the Django app logic.

For simplicity, in small projects it's ok to keep our ansible files in the same git repository than our application.
However, for real projects I would recommend having a separate repository for the deployment.

The deployment folder contains 2 folders:

1. `ansible_playbooks` - Ansible deployment files
2. `vagrant_ubuntu20.04` - Vagrant configuration to locally run a Virtualized Deployment environment for testing deployments.


### Using Vagrant 

Vagrant is a tool that allows you to quickly provision, run and destroy Virtual Machines in your local machine 
to aid in testing your deployment strategies for distributed applications.

In addition to Vagrant itself, you will need a virtualization solution that Vagrant can recognize, 
like VirtualBox, VMWare Fusion, or Docker (not full virtualization, but reported as useful for Apple Silicon).

#### Installing Vagrant and VirtualBox on Linux

```bash
# For Debian based systems 
apt install virtualbox
apt install vagrant
```

#### Installing Vagrant and VMWare Player on Apple Silicon (M1 and up)

Steps:

1. Install VMWare Fusion (and register to get a free license).
2. Install Vagrant (homebrew recommended).
3. Install Vagrant VMWare provider (homebrew recommended).

Follow the steps as detailed in the following gist: 
[Vagrant and VMWare Fusion 13 on Apple M1 Pro](https://gist.github.com/sbailliez/2305d831ebcf56094fd432a8717bed93)

**Note**: For me, the Rosetta installation step threw an error (I already had it installed), but that did not seem to matter.

**To Learn more about Vagrant**:

- Beginner's friendly intro to Vagrant in a presentation style: https://where.matsinet.codes/presentations/getting-started-with-vagrant/
- Example Vagrantfiles for different situations: https://www.thisprogrammingthing.com/2015/multiple-vagrant-vms-in-one-vagrantfile/
- Chapter of a Vagrant book that covers networking configuration in vagrant: https://www.oreilly.com/library/view/vagrant-up-and/9781449336103/ch04.html

#### Vagrant Basic Operations

For this demo we will only use the following vagrant commands:

- `vagrant up`: starts and provisions the vagrant environment
- `vagrant reload`: restarts vagrant machine, loads new Vagrantfile configuration
- `vagrant halt`: stops the vagrant machine
- `vagrant destroy`: stops and deletes all traces of the vagrant machine
- `vagrant ssh`: connects to machine via SSH

All these commands accept an optional last argument `[name|id]` to specify on which vm the operation will be conducted.
For example, to connect via ssh to db vm: `vagrant ssh db`

Run `vagrant --help` to see all available commands.

