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

docker-compose up -d

docker-compose exec -T \
    anyblok sh -c \
    'echo "run update data after migrate repo: '$REPO' branch: '$BRANCH'" > /var/test_service/update'
