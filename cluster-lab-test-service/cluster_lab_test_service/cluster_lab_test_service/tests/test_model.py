from anyblok.tests.testcase import BlokTestCase


class TestExample(BlokTestCase):
    """ Test python api on AnyBlok models"""

    def test_create_example(self):
        base = self.registry.Example.query().count()
        ex = self.registry.Example.insert(name="plop")
        self.assertEqual(self.registry.Example.query().count(), base + 1)
        self.assertEqual(ex.name, "plop")

    def test_create_example_with_content(self):
        base = self.registry.Example.query().count()
        ex = self.registry.Example.insert(name="plop2", content="plouf")
        self.assertEqual(self.registry.Example.query().count(), base + 1)
        self.assertEqual(ex.name, "plop2")
        self.assertEqual(ex.content, "plouf")
