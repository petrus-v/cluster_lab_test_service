#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Setup script for cluster-lab-test-service"""

from setuptools import setup, find_packages
import os


here = os.path.abspath(os.path.dirname(__file__))

with open(
    os.path.join(here, 'README.rst'), 'r', encoding='utf-8'
) as readme_file:
    readme = readme_file.read()

with open(
    os.path.join(here, 'CHANGELOG.rst'), 'r', encoding='utf-8'
) as changelog_file:
    changelog = changelog_file.read()

with open(
    os.path.join(here, 'VERSION'), 'r', encoding='utf-8'
) as version_file:
    version = version_file.read().strip()

requirements = [
    'anyblok',
    'psycopg2',
    'anyblok_pyramid',
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='cluster_lab_test_service',
    version=version,
    description="A service to easly made integration test",
    long_description=readme + '\n\n' + changelog,
    author="Pierre Verkest",
    author_email='pverkest@anybox.fr',
    url='https://github.com/petrus-v/cluster-lab-test-service',
    packages=find_packages(),
    entry_points={
        'bloks': [
            'cluster_lab_test_service=cluster_lab_test_service.cluster_lab_test_service:Cluster_lab_test_service'
            ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='cluster-lab-test-service',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests',
    tests_require=test_requirements,
)
