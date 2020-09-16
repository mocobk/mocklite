#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File   : base.py
# @Author : mocobk
# @Email  : mailmzb@qq.com
# @Time   : 2020/1/8 15:50

from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow_sqlalchemy import SQLAlchemyAutoSchemaOpts
from sqlalchemy.ext.declarative import declared_attr

from app.extensions import db
from app.libs.flask_sqlalchemy import QueryType


class ModelBase(db.Model):
    """
    db.Column(*args, **kwargs)
    - name
    - type_
    - *args
    - autoincrement
    - default
    - doc
    - key
    - index
    - info
    - nullable
    - onupdate
    - primary_key
    - server_default 
    - server_onupdate   
    - quote
    - unique
    - system
    - comment
    """
    query: QueryType  # Just for Type Hint
    # 为了ORM子类能继承
    __abstract__ = True

    # 为了把 create_time update_time 放在子类属性后面，这里用 declared_attr 方法声明类属性
    # @declared_attr
    # def create_time(self):
    #     return db.Column(db.DateTime, server_default=func.current_timestamp())
    #
    # @declared_attr
    # def update_time(self):
    #     return db.Column(db.DateTime, server_default=func.current_timestamp(), onupdate=datetime.now)

    @declared_attr
    def __mapper_args__(self):
        if hasattr(self, 'create_time'):
            return {"order_by": self.create_time.desc()}
        return {}


# -> marshmallow_sqlalchemy::SQLAlchemyAutoSchemaOpts
# -> marshmallow_sqlalchemy::SQLAlchemySchemaOpts
# -> marshmallow::SchemaOpts
# "->" 表示继承于
class BaseOpts(SQLAlchemyAutoSchemaOpts):
    """
    **选项均使用 meta.<option> = value 方式来定义**

    SQLAlchemySchema 选项配置，即 Meta 类中的选项，可以设置默认选项
    这里继承了 marshmallow_sqlalchemy 和 marshmallow 库的所有选项

    **marshmallow_sqlalchemy:: SQLAlchemyAutoSchemaOpts**
    - include_fk: Whether to include foreign fields; defaults to `False`.
    - include_relationships: Whether to include relationships; defaults to `False`.


    **marshmallow_sqlalchemy:: SQLAlchemySchemaOpts**

    - model: The SQLAlchemy model to generate the `Schema` from (mutually exclusive with ``table``).
    - table: The SQLAlchemy table to generate the `Schema` from (mutually exclusive with ``model``).
    - load_instance: Whether to load model instances.
    - sqla_session: SQLAlchemy session to be used for deserialization.
        This is only needed when ``load_instance`` is `True`. You can also pass a session to the Schema's `load` method.
    - transient: Whether to load model instances in a transient state (effectively ignoring the session).
        Only relevant when ``load_instance`` is `True`.
    - model_converter: `ModelConverter` class to use for converting the SQLAlchemy model to marshmallow fields.
    fields: Tuple or list of fields to include in the serialized result.


    **marshmallow:: SchemaOpts**

    - additional: Tuple or list of fields to include in addition to the
        explicitly declared fields. additional and fields are mutually-exclusive options.
    - include: Dictionary of additional fields to include in the schema. It is
        usually better to define fields as class variables, but you may need to use this option, e.g., if your fields are Python keywords. May be an OrderedDict.
    - exclude: Tuple or list of fields to exclude in the serialized result.
        Nested fields can be represented with dot delimiters.
    - dateformat: Default format for Date fields.
    - datetimeformat: Default format for DateTime fields.
    - render_module: Module to use for loads and dumps.
        Defaults to json from the standard library.
    - ordered: If True, order serialization output according to the
        order in which fields were declared. Output of Schema.dump will be a collections.OrderedDict.
    - index_errors: If True, errors dictionaries will include the index
        of invalid items in a collection.
    - load_only: Tuple or list of fields to exclude from serialized results.
    - dump_only: Tuple or list of fields to exclude from deserialization
    - unknown: Whether to exclude, include, or raise an error for unknown
        fields in the data. Use EXCLUDE, INCLUDE or RAISE.
    - register: Whether to register the Schema with marshmallow’s internal
        class registry. Must be True if you intend to refer to this Schema by class name in Nested fields. Only set this to False when memory usage is critical. Defaults to True.
    """

    def __init__(self, meta, **kwargs):
        meta.load_instance = True
        meta.datetimeformat = '%Y-%m-%d %H:%M:%S'
        meta.sqla_session = db.session

        super().__init__(meta, **kwargs)


SQLAlchemyAutoSchema.OPTIONS_CLASS = BaseOpts
