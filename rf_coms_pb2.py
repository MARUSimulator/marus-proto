# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: rf_coms.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import std_pb2 as std__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='rf_coms.proto',
  package='rfcommunication',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\rrf_coms.proto\x12\x0frfcommunication\x1a\tstd.proto\"\'\n\x14ReceiveStreamRequest\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\"u\n\x0bRangeingMsg\x12\x1b\n\x06header\x18\x01 \x01(\x0b\x32\x0b.std.Header\x12\x0f\n\x07\x61\x64\x64ress\x18\x02 \x01(\t\x12\x10\n\x08masterId\x18\x03 \x01(\r\x12&\n\x06ranges\x18\x04 \x03(\x0b\x32\x16.rfcommunication.Range\"h\n\x07LoraMsg\x12\x1b\n\x06header\x18\x01 \x01(\x0b\x32\x0b.std.Header\x12\x0f\n\x07\x61\x64\x64ress\x18\x02 \x01(\t\x12\x10\n\x08sourceId\x18\x03 \x01(\r\x12\x10\n\x08targetId\x18\x04 \x01(\r\x12\x0b\n\x03msg\x18\x05 \x01(\x0c\"&\n\x0e\x41uvGotoCommand\x12\t\n\x01x\x18\x01 \x01(\x01\x12\t\n\x01y\x18\x02 \x01(\x01\"-\n\x1a\x41uvPossibleTargetDirection\x12\x0f\n\x07heading\x18\x01 \x01(\x01\":\n\x05Range\x12\x10\n\x08sourceId\x18\x01 \x01(\r\x12\x10\n\x08targetId\x18\x02 \x01(\r\x12\r\n\x05range\x18\x03 \x01(\x01\x32\xed\x01\n\x10LoraTransmission\x12\x42\n\x12StreamRangeingMsgs\x12\x1c.rfcommunication.RangeingMsg\x1a\n.std.Empty\"\x00(\x01\x12Z\n\x13ReceiveLoraMessages\x12%.rfcommunication.ReceiveStreamRequest\x1a\x18.rfcommunication.LoraMsg\"\x00\x30\x01\x12\x39\n\x0fSendLoraMessage\x12\x18.rfcommunication.LoraMsg\x1a\n.std.Empty\"\x00\x62\x06proto3')
  ,
  dependencies=[std__pb2.DESCRIPTOR,])




_RECEIVESTREAMREQUEST = _descriptor.Descriptor(
  name='ReceiveStreamRequest',
  full_name='rfcommunication.ReceiveStreamRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='address', full_name='rfcommunication.ReceiveStreamRequest.address', index=0,
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
  serialized_start=45,
  serialized_end=84,
)


_RANGEINGMSG = _descriptor.Descriptor(
  name='RangeingMsg',
  full_name='rfcommunication.RangeingMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='rfcommunication.RangeingMsg.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='address', full_name='rfcommunication.RangeingMsg.address', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='masterId', full_name='rfcommunication.RangeingMsg.masterId', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ranges', full_name='rfcommunication.RangeingMsg.ranges', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=86,
  serialized_end=203,
)


_LORAMSG = _descriptor.Descriptor(
  name='LoraMsg',
  full_name='rfcommunication.LoraMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='rfcommunication.LoraMsg.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='address', full_name='rfcommunication.LoraMsg.address', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sourceId', full_name='rfcommunication.LoraMsg.sourceId', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='targetId', full_name='rfcommunication.LoraMsg.targetId', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='msg', full_name='rfcommunication.LoraMsg.msg', index=4,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=205,
  serialized_end=309,
)


_AUVGOTOCOMMAND = _descriptor.Descriptor(
  name='AuvGotoCommand',
  full_name='rfcommunication.AuvGotoCommand',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='rfcommunication.AuvGotoCommand.x', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='y', full_name='rfcommunication.AuvGotoCommand.y', index=1,
      number=2, type=1, cpp_type=5, label=1,
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
  ],
  serialized_start=311,
  serialized_end=349,
)


_AUVPOSSIBLETARGETDIRECTION = _descriptor.Descriptor(
  name='AuvPossibleTargetDirection',
  full_name='rfcommunication.AuvPossibleTargetDirection',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='heading', full_name='rfcommunication.AuvPossibleTargetDirection.heading', index=0,
      number=1, type=1, cpp_type=5, label=1,
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
  ],
  serialized_start=351,
  serialized_end=396,
)


_RANGE = _descriptor.Descriptor(
  name='Range',
  full_name='rfcommunication.Range',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sourceId', full_name='rfcommunication.Range.sourceId', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='targetId', full_name='rfcommunication.Range.targetId', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='range', full_name='rfcommunication.Range.range', index=2,
      number=3, type=1, cpp_type=5, label=1,
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
  ],
  serialized_start=398,
  serialized_end=456,
)

_RANGEINGMSG.fields_by_name['header'].message_type = std__pb2._HEADER
_RANGEINGMSG.fields_by_name['ranges'].message_type = _RANGE
_LORAMSG.fields_by_name['header'].message_type = std__pb2._HEADER
DESCRIPTOR.message_types_by_name['ReceiveStreamRequest'] = _RECEIVESTREAMREQUEST
DESCRIPTOR.message_types_by_name['RangeingMsg'] = _RANGEINGMSG
DESCRIPTOR.message_types_by_name['LoraMsg'] = _LORAMSG
DESCRIPTOR.message_types_by_name['AuvGotoCommand'] = _AUVGOTOCOMMAND
DESCRIPTOR.message_types_by_name['AuvPossibleTargetDirection'] = _AUVPOSSIBLETARGETDIRECTION
DESCRIPTOR.message_types_by_name['Range'] = _RANGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ReceiveStreamRequest = _reflection.GeneratedProtocolMessageType('ReceiveStreamRequest', (_message.Message,), dict(
  DESCRIPTOR = _RECEIVESTREAMREQUEST,
  __module__ = 'rf_coms_pb2'
  # @@protoc_insertion_point(class_scope:rfcommunication.ReceiveStreamRequest)
  ))
_sym_db.RegisterMessage(ReceiveStreamRequest)

RangeingMsg = _reflection.GeneratedProtocolMessageType('RangeingMsg', (_message.Message,), dict(
  DESCRIPTOR = _RANGEINGMSG,
  __module__ = 'rf_coms_pb2'
  # @@protoc_insertion_point(class_scope:rfcommunication.RangeingMsg)
  ))
_sym_db.RegisterMessage(RangeingMsg)

LoraMsg = _reflection.GeneratedProtocolMessageType('LoraMsg', (_message.Message,), dict(
  DESCRIPTOR = _LORAMSG,
  __module__ = 'rf_coms_pb2'
  # @@protoc_insertion_point(class_scope:rfcommunication.LoraMsg)
  ))
_sym_db.RegisterMessage(LoraMsg)

AuvGotoCommand = _reflection.GeneratedProtocolMessageType('AuvGotoCommand', (_message.Message,), dict(
  DESCRIPTOR = _AUVGOTOCOMMAND,
  __module__ = 'rf_coms_pb2'
  # @@protoc_insertion_point(class_scope:rfcommunication.AuvGotoCommand)
  ))
_sym_db.RegisterMessage(AuvGotoCommand)

AuvPossibleTargetDirection = _reflection.GeneratedProtocolMessageType('AuvPossibleTargetDirection', (_message.Message,), dict(
  DESCRIPTOR = _AUVPOSSIBLETARGETDIRECTION,
  __module__ = 'rf_coms_pb2'
  # @@protoc_insertion_point(class_scope:rfcommunication.AuvPossibleTargetDirection)
  ))
_sym_db.RegisterMessage(AuvPossibleTargetDirection)

Range = _reflection.GeneratedProtocolMessageType('Range', (_message.Message,), dict(
  DESCRIPTOR = _RANGE,
  __module__ = 'rf_coms_pb2'
  # @@protoc_insertion_point(class_scope:rfcommunication.Range)
  ))
_sym_db.RegisterMessage(Range)



_LORATRANSMISSION = _descriptor.ServiceDescriptor(
  name='LoraTransmission',
  full_name='rfcommunication.LoraTransmission',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=459,
  serialized_end=696,
  methods=[
  _descriptor.MethodDescriptor(
    name='StreamRangeingMsgs',
    full_name='rfcommunication.LoraTransmission.StreamRangeingMsgs',
    index=0,
    containing_service=None,
    input_type=_RANGEINGMSG,
    output_type=std__pb2._EMPTY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ReceiveLoraMessages',
    full_name='rfcommunication.LoraTransmission.ReceiveLoraMessages',
    index=1,
    containing_service=None,
    input_type=_RECEIVESTREAMREQUEST,
    output_type=_LORAMSG,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SendLoraMessage',
    full_name='rfcommunication.LoraTransmission.SendLoraMessage',
    index=2,
    containing_service=None,
    input_type=_LORAMSG,
    output_type=std__pb2._EMPTY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_LORATRANSMISSION)

DESCRIPTOR.services_by_name['LoraTransmission'] = _LORATRANSMISSION

# @@protoc_insertion_point(module_scope)