#!/bin/sh

# exit on error
set -e
# -x debug mode to display line before its execution
set +x


USAGE="
Usage: $0
    -r REPO   Service repo: url should be the current service repo
    -b BRANCH Service branch: should be the current branch
Post up of -r repo of -b branch application
Options:
    -h               Show this help.
"


while getopts "r:b:h" OPTION
do
    case $OPTION in
        r) REPO=$OPTARG;;
        b) BRANCH=$OPTARG;;
        h) echo "$USAGE";
           exit;;
        *) echo "Unknown parameter... ";
           echo "$USAGE";
           exit 1;;
    esac
done

# if exists load optional post_up.env
if [ -f $BRANCH/post_up.env ]; then
    . $BRANCH/post_up.env
fi

# Reminder: at this stage containers are not up yet !

# sim here a real life UC: up of the db for an update
docker-compose up -d dbserver
#docker-compose exec -T -u postgres dbserver sh -c \
#    "while ! psql -d 'lab_db' -c 'select 1' ; do echo 'Waiting pgsql init...'; sleep 1; done;"

# sim here a fake update
# just put a test file to check it exists in CI (then we now we apply well update.sh script)
docker-compose run --rm test sh -c "echo 'TEST UPDATE' >> /tmp/update.txt"

# down services
docker-compose down
