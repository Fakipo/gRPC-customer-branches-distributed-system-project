# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: example.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rexample.proto\"L\n\nMsgRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x11\n\tinterface\x18\x02 \x01(\t\x12\r\n\x05money\x18\x03 \x01(\x05\x12\x10\n\x08\x62ranchId\x18\x04 \x01(\x05\"Q\n\x0bMsgResponse\x12\x11\n\tinterface\x18\x01 \x01(\t\x12\x0e\n\x06result\x18\x02 \x01(\t\x12\r\n\x05money\x18\x03 \x01(\x05\x12\x10\n\x08\x62ranchId\x18\x04 \x01(\x05\x32\x63\n\x06\x42ranch\x12*\n\x0bMsgDelivery\x12\x0b.MsgRequest\x1a\x0c.MsgResponse\"\x00\x12-\n\x0eMsgPropagation\x12\x0b.MsgRequest\x1a\x0c.MsgResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'example_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_MSGREQUEST']._serialized_start=17
  _globals['_MSGREQUEST']._serialized_end=93
  _globals['_MSGRESPONSE']._serialized_start=95
  _globals['_MSGRESPONSE']._serialized_end=176
  _globals['_BRANCH']._serialized_start=178
  _globals['_BRANCH']._serialized_end=277
# @@protoc_insertion_point(module_scope)
