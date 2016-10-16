import json

from ..postgres_range import JSONRangeString
from graphene.types.objecttype import ObjectType
from graphene.types.schema import Schema


class Query(ObjectType):
    json = JSONRangeString(input=JSONRangeString())

    def resolve_json(self, args, context, info):
        input = args.get('input')
        return input

schema = Schema(query=Query)


def test_jsonstring_query():
    json_value = '{"key": "value"}'

    json_value_quoted = json_value.replace('"', '\\"')
    result = schema.execute('''{ json(input: "%s") }'''%json_value_quoted)
    assert not result.errors
    assert result.data == {
        'json': json_value
    }


def test_jsonstring_query_variable():
    json_value = '{"key": "value"}'

    result = schema.execute(
        '''query Test($json: JSONString){ json(input: $json) }''',
        variable_values={'json': json_value}
    )
    assert not result.errors
    assert result.data == {
        'json': json_value
    }