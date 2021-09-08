# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: parameter_server.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import common_pb2 as common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='parameter_server.proto',
  package='parameterserver',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x16parameter_server.proto\x12\x0fparameterserver\x1a\x0c\x63ommon.proto\"\x1f\n\x0fGetParamRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"K\n\x0fSetParamRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12*\n\x05value\x18\x02 \x01(\x0b\x32\x1b.parameterserver.ParamValue\"r\n\nParamValue\x12\x12\n\x08valueStr\x18\x01 \x01(\tH\x00\x12\x12\n\x08valueInt\x18\x02 \x01(\x05H\x00\x12\x13\n\tvalueBool\x18\x03 \x01(\x08H\x00\x12\x15\n\x0bvalueDouble\x18\x04 \x01(\x01H\x00\x42\x10\n\x0eparameterValue2\xa5\x01\n\x0fParameterServer\x12O\n\x0cGetParameter\x12 .parameterserver.GetParamRequest\x1a\x1b.parameterserver.ParamValue\"\x00\x12\x41\n\x0cSetParameter\x12 .parameterserver.SetParamRequest\x1a\r.common.Empty\"\x00\x62\x06proto3')
  ,
  dependencies=[common__pb2.DESCRIPTOR,])




_GETPARAMREQUEST = _descriptor.Descriptor(
  name='GetParamRequest',
  full_name='parameterserver.GetParamRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='parameterserver.GetParamRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=57,
  serialized_end=88,
)


_SETPARAMREQUEST = _descriptor.Descriptor(
  name='SetParamRequest',
  full_name='parameterserver.SetParamRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='parameterserver.SetParamRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='parameterserver.SetParamRequest.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=90,
  serialized_end=165,
)


_PARAMVALUE = _descriptor.Descriptor(
  name='ParamValue',
  full_name='parameterserver.ParamValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='valueStr', full_name='parameterserver.ParamValue.valueStr', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='valueInt', full_name='parameterserver.ParamValue.valueInt', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='valueBool', full_name='parameterserver.ParamValue.valueBool', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='valueDouble', full_name='parameterserver.ParamValue.valueDouble', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='parameterValue', full_name='parameterserver.ParamValue.parameterValue',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=167,
  serialized_end=281,
)

_SETPARAMREQUEST.fields_by_name['value'].message_type = _PARAMVALUE
_PARAMVALUE.oneofs_by_name['parameterValue'].fields.append(
  _PARAMVALUE.fields_by_name['valueStr'])
_PARAMVALUE.fields_by_name['valueStr'].containing_oneof = _PARAMVALUE.oneofs_by_name['parameterValue']
_PARAMVALUE.oneofs_by_name['parameterValue'].fields.append(
  _PARAMVALUE.fields_by_name['valueInt'])
_PARAMVALUE.fields_by_name['valueInt'].containing_oneof = _PARAMVALUE.oneofs_by_name['parameterValue']
_PARAMVALUE.oneofs_by_name['parameterValue'].fields.append(
  _PARAMVALUE.fields_by_name['valueBool'])
_PARAMVALUE.fields_by_name['valueBool'].containing_oneof = _PARAMVALUE.oneofs_by_name['parameterValue']
_PARAMVALUE.oneofs_by_name['parameterValue'].fields.append(
  _PARAMVALUE.fields_by_name['valueDouble'])
_PARAMVALUE.fields_by_name['valueDouble'].containing_oneof = _PARAMVALUE.oneofs_by_name['parameterValue']
DESCRIPTOR.message_types_by_name['GetParamRequest'] = _GETPARAMREQUEST
DESCRIPTOR.message_types_by_name['SetParamRequest'] = _SETPARAMREQUEST
DESCRIPTOR.message_types_by_name['ParamValue'] = _PARAMVALUE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetParamRequest = _reflection.GeneratedProtocolMessageType('GetParamRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETPARAMREQUEST,
  __module__ = 'parameter_server_pb2'
  # @@protoc_insertion_point(class_scope:parameterserver.GetParamRequest)
  ))
_sym_db.RegisterMessage(GetParamRequest)

SetParamRequest = _reflection.GeneratedProtocolMessageType('SetParamRequest', (_message.Message,), dict(
  DESCRIPTOR = _SETPARAMREQUEST,
  __module__ = 'parameter_server_pb2'
  # @@protoc_insertion_point(class_scope:parameterserver.SetParamRequest)
  ))
_sym_db.RegisterMessage(SetParamRequest)

ParamValue = _reflection.GeneratedProtocolMessageType('ParamValue', (_message.Message,), dict(
  DESCRIPTOR = _PARAMVALUE,
  __module__ = 'parameter_server_pb2'
  # @@protoc_insertion_point(class_scope:parameterserver.ParamValue)
  ))
_sym_db.RegisterMessage(ParamValue)



_PARAMETERSERVER = _descriptor.ServiceDescriptor(
  name='ParameterServer',
  full_name='parameterserver.ParameterServer',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=284,
  serialized_end=449,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetParameter',
    full_name='parameterserver.ParameterServer.GetParameter',
    index=0,
    containing_service=None,
    input_type=_GETPARAMREQUEST,
    output_type=_PARAMVALUE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SetParameter',
    full_name='parameterserver.ParameterServer.SetParameter',
    index=1,
    containing_service=None,
    input_type=_SETPARAMREQUEST,
    output_type=common__pb2._EMPTY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_PARAMETERSERVER)

DESCRIPTOR.services_by_name['ParameterServer'] = _PARAMETERSERVER

# @@protoc_insertion_point(module_scope)
