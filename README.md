# Cluster lab test service

The intent of this repo is for acceptance test developed in [mlfmonde/cluster](
https://github.com/mlfmonde/cluster).

This repo as different branches for different use cases:

* [![Build Status](https://travis-ci.org/mlfmonde/cluster_lab_test_service.svg?branch=docker_image_builder)](https://travis-ci.org/mlfmonde/cluster_lab_test_service)
  [docker_image_builder](https://github.com/mlfmonde/cluster_lab_test_service/tree/docker_image_builder):
  is used to build the docker images used in those different uses cases in order
  to avoid to build the image on each nodes while deploying the service a save
  a bit of time.
* [master](https://github.com/mlfmonde/cluster_lab_test_service) (this branch):
  this branches is used in multiple uses cases:
    * [test_new_service.py]()
    * [test_reverse_service.py]()
    * [test_redeploy_service.py]()
    * [test_disable_hapx_config_while_maintenance_mode.py]()
* [bind_relative_path](https://github.com/mlfmonde/cluster_lab_test_service/tree/bind_relative_path):
    * [test_bind_relative_path.py]()
* [build_copy_symlink](https://github.com/mlfmonde/cluster_lab_test_service/tree/build_copy_symlink):
  That's normal this branch do not use the docker image and build the image
  as deploy time to test this features.
    * [test_docker_compose_version_consistency.py]()
* [missing_volume](https://github.com/mlfmonde/cluster_lab_test_service/tree/missing_volume):
    * [auth_required/test_change_master_same_slave.py]():
      this test require authentication to push tag on this cluster lab
      test service repo to simulate config change.
    * [auth_required/test_change_slave_same_master.py]():
      this test require authentication to push tag on this cluster lab
      test service repo to simulate config change.
* [qualif](https://github.com/mlfmonde/cluster_lab_test_service/tree/qualif):
    * [test_migrate.py]()
* [update_script](https://github.com/mlfmonde/cluster_lab_test_service/tree/update_script):
    * []()
* [without_caddyfile](https://github.com/mlfmonde/cluster_lab_test_service/tree/without_caddyfile):
    * [test_migrate.py]()
    * [auth_required/test_change_master_same_slave.py]():
      this test require authentication to push tag on this cluster lab
      test service repo to simulate config change.
    * [auth_required/test_change_slave_same_master.py]():
      this test require authentication to push tag on this cluster lab
      test service repo to simulate config change.
