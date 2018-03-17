import os

from pyramid.view import view_defaults, view_config
from anyblok_pyramid import current_blok
from pyramid.response import Response

PERSISTENT_PATH = "/var/test_service/"
CACHE_PATH = "/var/cache/"


@view_defaults(installed_blok=current_blok())
class ExampleView:
    def __init__(self, request):
        self.request = request
        self.registry = request.anyblok.registry

    @view_config(route_name='root')
    def route_root(self):
        return Response(
            """
            <a href="./example">List all availaible examples</a><br/>
            <a href="./example/1">Get example id=1</a>
            """
        )

    @view_config(route_name='example', request_method='GET')
    def route_example(self):
        example = self.registry.Example.query().get(
            self.request.matchdict['id']
        )
        return Response(example.name)

    @view_config(
        route_name='example_list', renderer='json', request_method='POST'
    )
    def route_create(self):
        name = self.request.params.getone('name')
        content = self.request.params.get('content')
        record = self.registry.Example.insert(name=name, content=content)
        if content:
            with open(os.path.join(PERSISTENT_PATH, name), 'w') as f:
                f.write(content)
            with open(os.path.join(CACHE_PATH, name), 'w') as f:
                f.write(content)

        return Response(
            json_body=record.to_dict(),
            status=201,
            headers=dict(Location="example/{}".format(record.id))
        )

    @view_config(
        route_name='example_list', renderer='json', request_method='GET'
    )
    def route_examples(self):
        """view all examples.
        """
        return self.registry.Example.query().all().to_dict()
