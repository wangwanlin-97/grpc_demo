# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/messages.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14proto/messages.proto\x12\tgrpc_test\")\n\x0cHelloRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0b\n\x03\x61ge\x18\x02 \x01(\t\"\x1d\n\nHelloReply\x12\x0f\n\x07message\x18\x01 \x01(\t\",\n\x0b\x43hatRequest\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\"\x1f\n\x0c\x43hatResponse\x12\x0f\n\x07message\x18\x01 \x01(\t2C\n\x05Hello\x12:\n\x08sayHello\x12\x17.grpc_test.HelloRequest\x1a\x15.grpc_test.HelloReply2C\n\x04\x43hat\x12;\n\x04\x63hat\x12\x16.grpc_test.ChatRequest\x1a\x17.grpc_test.ChatResponse(\x01\x30\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proto.messages_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_HELLOREQUEST']._serialized_start=35
  _globals['_HELLOREQUEST']._serialized_end=76
  _globals['_HELLOREPLY']._serialized_start=78
  _globals['_HELLOREPLY']._serialized_end=107
  _globals['_CHATREQUEST']._serialized_start=109
  _globals['_CHATREQUEST']._serialized_end=153
  _globals['_CHATRESPONSE']._serialized_start=155
  _globals['_CHATRESPONSE']._serialized_end=186
  _globals['_HELLO']._serialized_start=188
  _globals['_HELLO']._serialized_end=255
  _globals['_CHAT']._serialized_start=257
  _globals['_CHAT']._serialized_end=324
# @@protoc_insertion_point(module_scope)
