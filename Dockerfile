FROM python:3-stretch

WORKDIR /usr/src/cluster-lab-service

COPY cluster-lab-test-service/ ./

RUN make setup-tests

# TODO: avoid wraper script to properly manage PID1
ENTRYPOINT ["make"]
CMD ["run-dev"]
