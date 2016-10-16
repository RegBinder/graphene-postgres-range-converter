from __future__ import absolute_import

import json

import psycopg2 as psycopg2
from graphql.language import ast

from graphene.types.scalars import Scalar


class JSONRangeString(Scalar):
    '''JSON String'''

    @staticmethod
    def serialize(obj):
        if isinstance(obj, psycopg2.extras.Range):
            return json.dumps(dict(lower=obj.lower, upper=obj.upper))
        else:
            return json.dumps(obj)

    @staticmethod
    def parse_literal(node):
        if isinstance(node, ast.StringValue):
            return json.loads(node.value)

    @staticmethod
    def parse_value(value):
        return json.loads(value)
