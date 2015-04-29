#Interactive prompting of access credentials to DB.
#Note that from bash, this needs to be invoked by
#. ./this_script
#source ./this_script
#Otherwise the set environmen values will not stay.
read -p "MYSQL IP address, please." ip
export MYSQLIP=$ip
read -p "MYSQL username, please." id
export MYSQLID=$id
read -p "MYSQL password, please." pw
export MYSQLPW=$pw
