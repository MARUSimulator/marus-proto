# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: marine.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import std_pb2 as std__pb2
import geometry_pb2 as geometry__pb2
import geographic_pb2 as geographic__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='marine.proto',
  package='marine',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0cmarine.proto\x12\x06marine\x1a\tstd.proto\x1a\x0egeometry.proto\x1a\x10geographic.proto\"\x84\x02\n\x03\x44vl\x12\x1b\n\x06header\x18\x01 \x01(\x0b\x32\x0b.std.Header\x12#\n\x08velocity\x18\x02 \x01(\x0b\x32\x11.geometry.Vector3\x12\x1a\n\x12velocityCovariance\x18\x03 \x03(\x01\x12\x10\n\x08\x61ltitude\x18\x04 \x01(\x01\x12\x1a\n\x12\x61ltitudeCovariance\x18\x05 \x01(\x01\x12\x38\n\x11velocityReference\x18\x07 \x01(\x0e\x32\x1d.marine.Dvl.VelocityReference\"7\n\x11VelocityReference\x12\x0b\n\x07UNKNOWN\x10\x00\x12\t\n\x05WATER\x10\x01\x12\n\n\x06\x42OTTOM\x10\x02\"\xae\x01\n\x11\x41ISPositionReport\x12\x0c\n\x04type\x18\x01 \x01(\r\x12\x0c\n\x04mmsi\x18\x02 \x01(\r\x12\x0f\n\x07heading\x18\x03 \x01(\x02\x12\x18\n\x10\x63ourseOverGround\x18\x04 \x01(\x02\x12\x17\n\x0fspeedOverGround\x18\x05 \x01(\x02\x12\x11\n\ttimestamp\x18\x06 \x01(\r\x12&\n\x08geopoint\x18\x07 \x01(\x0b\x32\x14.geographic.GeoPointb\x06proto3'
  ,
  dependencies=[std__pb2.DESCRIPTOR,geometry__pb2.DESCRIPTOR,geographic__pb2.DESCRIPTOR,])



_DVL_VELOCITYREFERENCE = _descriptor.EnumDescriptor(
  name='VelocityReference',
  full_name='marine.Dvl.VelocityReference',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='WATER', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='BOTTOM', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=275,
  serialized_end=330,
)
_sym_db.RegisterEnumDescriptor(_DVL_VELOCITYREFERENCE)


_DVL = _descriptor.Descriptor(
  name='Dvl',
  full_name='marine.Dvl',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='marine.Dvl.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='velocity', full_name='marine.Dvl.velocity', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='velocityCovariance', full_name='marine.Dvl.velocityCovariance', index=2,
      number=3, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='altitude', full_name='marine.Dvl.altitude', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='altitudeCovariance', full_name='marine.Dvl.altitudeCovariance', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='velocityReference', full_name='marine.Dvl.velocityReference', index=5,
      number=7, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _DVL_VELOCITYREFERENCE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=70,
  serialized_end=330,
)


_AISPOSITIONREPORT = _descriptor.Descriptor(
  name='AISPositionReport',
  full_name='marine.AISPositionReport',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='marine.AISPositionReport.type', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mmsi', full_name='marine.AISPositionReport.mmsi', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='heading', full_name='marine.AISPositionReport.heading', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='courseOverGround', full_name='marine.AISPositionReport.courseOverGround', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='speedOverGround', full_name='marine.AISPositionReport.speedOverGround', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='marine.AISPositionReport.timestamp', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='geopoint', full_name='marine.AISPositionReport.geopoint', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=333,
  serialized_end=507,
)

_DVL.fields_by_name['header'].message_type = std__pb2._HEADER
_DVL.fields_by_name['velocity'].message_type = geometry__pb2._VECTOR3
_DVL.fields_by_name['velocityReference'].enum_type = _DVL_VELOCITYREFERENCE
_DVL_VELOCITYREFERENCE.containing_type = _DVL
_AISPOSITIONREPORT.fields_by_name['geopoint'].message_type = geographic__pb2._GEOPOINT
DESCRIPTOR.message_types_by_name['Dvl'] = _DVL
DESCRIPTOR.message_types_by_name['AISPositionReport'] = _AISPOSITIONREPORT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Dvl = _reflection.GeneratedProtocolMessageType('Dvl', (_message.Message,), {
  'DESCRIPTOR' : _DVL,
  '__module__' : 'marine_pb2'
  # @@protoc_insertion_point(class_scope:marine.Dvl)
  })
_sym_db.RegisterMessage(Dvl)

AISPositionReport = _reflection.GeneratedProtocolMessageType('AISPositionReport', (_message.Message,), {
  'DESCRIPTOR' : _AISPOSITIONREPORT,
  '__module__' : 'marine_pb2'
  # @@protoc_insertion_point(class_scope:marine.AISPositionReport)
  })
_sym_db.RegisterMessage(AISPositionReport)


# @@protoc_insertion_point(module_scope)
