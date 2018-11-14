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

# just put a test file to check it exists in CI (then we now we apply well post_up.sh script)
docker-compose exec anyblok sh -c "echo 'TEST POST UP' >> /tmp/post_up_test.txt"
