#!/bin/sh

# exit on error
set -e
# -x debug mode to display line before its execution
set -x


USAGE="
Usage: $0
    -R SOURCE REPO -B SOURCE BRANCH
    -r TARGET REPO -b TARGET BRANCH [-h]
Post migrage while migrating volume from SOURCE to TARGET

Options:
    -R SOURCE REPO   Service repo source url from where volumes came from
    -B SOURCE BRANCH Service source branch from where volumes come from
    -r TARGET REPO   Service repo target url should be the current repo
                     where data are restored
    -b TARGET BRANCH Service target branch should be the current branch
                     where data are restored
    -h               Show this help.
"


while getopts "R:B:r:b:h" OPTION
do
    case $OPTION in
        R) SOURCE_REPO=$OPTARG;;
        B) SOURCE_BRANCH=$OPTARG;;
        r) REPO=$OPTARG;;
        b) BRANCH=$OPTARG;;
        h) echo "$USAGE";
           exit;;
        *) echo "Unknown parameter... ";
           echo "$USAGE";
           exit 1;;
    esac
done

echo "migrate data from $SOURCE_REPO branch: $SOURCE_BRANCH to $REPO branch: $BRANCH"
docker-compose up -d
docker-compose exec -T \
    anyblok sh -c \
    'echo "migrate data from '$SOURCE_REPO' branch: '$SOURCE_BRANCH' to '$REPO' branch: '$BRANCH'" > /var/test_service/migrate'

docker-compose run -T \
    --entrypoint "" \
    anyblok sh -c \
    'echo "migrate data from '$SOURCE_REPO' branch: '$SOURCE_BRANCH' to '$REPO' branch: '$BRANCH'"'
