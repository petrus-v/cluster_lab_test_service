import os

from anyblok_pyramid.tests.testcase import PyramidBlokTestCase
from cluster_lab_test_service.cluster_lab_test_service import views


class TestCanigooRestApi(PyramidBlokTestCase):
    """ Test pyramid routes with PyramidBlokTestCase"""

    def test_root(self):
        """Test pyramid Example get route /"""
        response = self.webserver.get('/')
        self.assertEqual(response.status, '200 OK')

    def test_examples(self):
        response = self.webserver.get('/example')
        self.assertEqual(response.status, '200 OK')
        self.assertEqual(
            response.json_body,
            [{'id': 1, 'name': "An example", 'content': None}]
        )

    def test_get_example(self):
        response = self.webserver.get('/example/1', status=200)
        self.assertEqual(response.body.decode('utf8'), "An example")

    def test_post_example(self):
        response = self.webserver.post(
            '/example', dict(name="test post", ), status=201
        )
        json_body = response.json_body
        id = json_body['id']
        self.assertEqual(
            json_body,
            {'id': id, 'name': "test post", 'content': None}
        )
        self.assertTrue(response.headers['Location'].endswith(
            "example/{}".format(id)))

    def test_post_example_with_content(self):
        name = "test_with_content"
        response = self.webserver.post(
            '/example', dict(name=name, content="hello"), status=201
        )
        json_body = response.json_body
        id = json_body['id']
        self.assertTrue(response.headers['Location'].endswith(
            "example/{}".format(id)))

        with open(os.path.join(views.PERSISTENT_PATH, name), 'r') as f:
            self.assertEqual(f.read(), "hello")
        with open(os.path.join(views.CACHE_PATH, name), 'r') as f:
            self.assertEqual(f.read(), "hello")
