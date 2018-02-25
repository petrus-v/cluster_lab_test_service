FROM python:3-stretch

WORKDIR /usr/src/cluster-lab-service

COPY cluster-lab-test-service/ ./

RUN make setup-dev

ENTRYPOINT ["make"]
CMD ["run-dev"]