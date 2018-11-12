# Installing Apache Unomi 1.3 on Ubuntu
Apache Unomi is a customer data platform built on top of Apache Karaf and ElasticSearch. Unomi provides a REST API and is extendible using Java.

:warning: This is not a production setup. Command executed in the tutorial were done as root.

## Install Java 8
```
apt install openjdk-8-jdk
```
Set you `JAVA_HOME` by editing `/etc/environment`:
```
vi /etc/environment
```
and add these two lines below what is already there:
```
JAVA_HOME="/usr/lib/jvm/java-8-openjdk-amd64/"
PATH=$JAVA_HOME/bin:$PATH
```
Reload environment:
```
source /etc/environment
```
:warning: Your `JAVA_HOME` may vary. You can review the output of the `apt install` command to see where Java was installed.

## Installing ElasticSearch 5.6.3
```
apt-get update && apt-get -y install apt-transport-https curl wget
wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-5.6.3.deb
dpkg -i elasticsearch-5.6.3.deb
```
Next, edit the ElasticSearch configuration:
```
vi /etc/elasticsearch/elasticsearch.yml
```
Add uncomment and edit the line with `cluster.name` to:
```
cluster.name: contextElasticSearch
```
Unomi expects the cluster name to be `contextElasticSearch`.

Now start and check the status of ElasticSearch to confirm it is running:
```
service elasticsearch start
service elasticsearch status
```

## Installing Unomi 1.3
You can install a binary distribution from any of [these](https://www.apache.org/dyn/closer.lua/incubator/unomi/1.3.0-incubating/unomi-1.3.0-incubating-bin.tar.gz) mirrors. Just download and extract the files, the run it using Karaf.

Download and extract Unomi from binary distribution:
```
wget http://apache.mirrors.pair.com/incubator/unomi/1.3.0-incubating/unomi-1.3.0-incubating-bin.tar.gz
tar -xzf unomi-1.3.0-incubating-bin.tar.gz
```
After it is extracted, I prefer to move it into `/opt/unomi`, just my preference to put installed software into `/opt`:
```
mkdir /opt/unomi
mv unomi-1.3.0-incubating/*
```

## Start Unomi
To start Unomi from the terminal:
```
/opt/unomi/bin/karaf
```
In the Karaf terminal, run `unomi:start`:
```
karaf@root()> unomi:start
```
After you run the command, Unomi will be available.

## Test Unomi
There are some Python programs in this project that demostrate how to interface with Unomi.

You can check some endpoints in a web browser, the default username and password is `karaf` and `karaf`:
```
https://localhost:9443/cxs/cluster
http://localhost:8181/context.js?sessionId=1234
```
:warning: You may need to change localhost if you installed this on a remote server.

### Create a New Profile
Run the Python file to create a new profile (use Python 3):
```
python new_profile.py
```
This creates a profile with ID 10. You can view this profile with a [GET /profile endpoint](https://unomi.incubator.apache.org/rest-api-doc/#-1185500428) in the browser:
```
http://localhost:8181/cxs/profile/10
```

### Create a New Profile and Session
Run the Python file to create a new profile (use Python 3):
```
python new_profile_and_session.py
```
This creates a session with ID 101 and profile with ID 10. You can view this profile with a [GET /profile/{profile_id}/sessions endpoint](https://unomi.incubator.apache.org/rest-api-doc/#1764110248) in the browser:
```
http://localhost:8181/cxs/profiles/10/sessions/
```

### Create a New Rule
Run the python file to create a new rule (use Python 3):
```
python new_rule.py
```
This creates a rule with ID eligibilityRule and a profile with ID 10. You can view this rule with a [GET /rule/{rule_id} endpoint](https://unomi.incubator.apache.org/rest-api-doc/#-1505954579) in the browser:
```
http://localhost:8181/cxs/rules/eligibilityRule/
```
and you can view the profile which has been marked as eligible = "yes":
```
http://localhost:8181/cxs/profile/10
```

## Installing Unomi as a Service
You can install Unomi as a service using Karaf's [Service Wrapper](http://karaf.apache.org/manual/latest/#_service_wrapper).

From the Karaf command line:
```
karaf@root()> feature:install wrapper
karaf@root()> wrapper:install
```
The output from the `wrapper:install` command will include instructions for finishing the installation and starting/stoping Karaf.
