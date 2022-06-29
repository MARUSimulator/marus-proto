# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: auv.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import std_pb2 as std__pb2
import geographic_pb2 as geographic__pb2
import geometry_pb2 as geometry__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='auv.proto',
  package='auv',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\tauv.proto\x12\x03\x61uv\x1a\tstd.proto\x1a\x10geographic.proto\x1a\x0egeometry.proto\"1\n\x03NED\x12\r\n\x05north\x18\x01 \x01(\x01\x12\x0c\n\x04\x65\x61st\x18\x02 \x01(\x01\x12\r\n\x05\x64\x65pth\x18\x03 \x01(\x01\"\x9d\x03\n\x10NavigationStatus\x12\x1b\n\x06header\x18\x01 \x01(\x0b\x32\x0b.std.Header\x12,\n\x0eglobalPosition\x18\x02 \x01(\x0b\x32\x14.geographic.GeoPoint\x12$\n\x06origin\x18\x03 \x01(\x0b\x32\x14.geographic.GeoPoint\x12\x1a\n\x08position\x18\x04 \x01(\x0b\x32\x08.auv.NED\x12\'\n\x0c\x62odyVelocity\x18\x05 \x01(\x0b\x32\x11.geometry.Vector3\x12+\n\x10seafloorVelocity\x18\x06 \x01(\x0b\x32\x11.geometry.Vector3\x12&\n\x0borientation\x18\x07 \x01(\x0b\x32\x11.geometry.Vector3\x12*\n\x0forientationRate\x18\x08 \x01(\x0b\x32\x11.geometry.Vector3\x12\"\n\x10positionVariance\x18\t \x01(\x0b\x32\x08.auv.NED\x12.\n\x13orientationVariance\x18\n \x01(\x0b\x32\x11.geometry.Vector3b\x06proto3')
  ,
  dependencies=[std__pb2.DESCRIPTOR,geographic__pb2.DESCRIPTOR,geometry__pb2.DESCRIPTOR,])




_NED = _descriptor.Descriptor(
  name='NED',
  full_name='auv.NED',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='north', full_name='auv.NED.north', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='east', full_name='auv.NED.east', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='depth', full_name='auv.NED.depth', index=2,
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
  serialized_start=63,
  serialized_end=112,
)


_NAVIGATIONSTATUS = _descriptor.Descriptor(
  name='NavigationStatus',
  full_name='auv.NavigationStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='auv.NavigationStatus.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='globalPosition', full_name='auv.NavigationStatus.globalPosition', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='origin', full_name='auv.NavigationStatus.origin', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='position', full_name='auv.NavigationStatus.position', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bodyVelocity', full_name='auv.NavigationStatus.bodyVelocity', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='seafloorVelocity', full_name='auv.NavigationStatus.seafloorVelocity', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='orientation', full_name='auv.NavigationStatus.orientation', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='orientationRate', full_name='auv.NavigationStatus.orientationRate', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='positionVariance', full_name='auv.NavigationStatus.positionVariance', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='orientationVariance', full_name='auv.NavigationStatus.orientationVariance', index=9,
      number=10, type=11, cpp_type=10, label=1,
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
  serialized_start=115,
  serialized_end=528,
)

_NAVIGATIONSTATUS.fields_by_name['header'].message_type = std__pb2._HEADER
_NAVIGATIONSTATUS.fields_by_name['globalPosition'].message_type = geographic__pb2._GEOPOINT
_NAVIGATIONSTATUS.fields_by_name['origin'].message_type = geographic__pb2._GEOPOINT
_NAVIGATIONSTATUS.fields_by_name['position'].message_type = _NED
_NAVIGATIONSTATUS.fields_by_name['bodyVelocity'].message_type = geometry__pb2._VECTOR3
_NAVIGATIONSTATUS.fields_by_name['seafloorVelocity'].message_type = geometry__pb2._VECTOR3
_NAVIGATIONSTATUS.fields_by_name['orientation'].message_type = geometry__pb2._VECTOR3
_NAVIGATIONSTATUS.fields_by_name['orientationRate'].message_type = geometry__pb2._VECTOR3
_NAVIGATIONSTATUS.fields_by_name['positionVariance'].message_type = _NED
_NAVIGATIONSTATUS.fields_by_name['orientationVariance'].message_type = geometry__pb2._VECTOR3
DESCRIPTOR.message_types_by_name['NED'] = _NED
DESCRIPTOR.message_types_by_name['NavigationStatus'] = _NAVIGATIONSTATUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

NED = _reflection.GeneratedProtocolMessageType('NED', (_message.Message,), dict(
  DESCRIPTOR = _NED,
  __module__ = 'auv_pb2'
  # @@protoc_insertion_point(class_scope:auv.NED)
  ))
_sym_db.RegisterMessage(NED)

NavigationStatus = _reflection.GeneratedProtocolMessageType('NavigationStatus', (_message.Message,), dict(
  DESCRIPTOR = _NAVIGATIONSTATUS,
  __module__ = 'auv_pb2'
  # @@protoc_insertion_point(class_scope:auv.NavigationStatus)
  ))
_sym_db.RegisterMessage(NavigationStatus)


# @@protoc_insertion_point(module_scope)