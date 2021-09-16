# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sensor.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import std_pb2 as std__pb2
import geometry_pb2 as geometry__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='sensor.proto',
  package='sensor',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0csensor.proto\x12\x06sensor\x1a\tstd.proto\x1a\x0egeometry.proto\"\x90\x02\n\x03Imu\x12\x1b\n\x06header\x18\x01 \x01(\x0b\x32\x0b.std.Header\x12)\n\x0borientation\x18\x02 \x01(\x0b\x32\x14.geometry.Quaternion\x12\x1d\n\x15orientationCovariance\x18\x03 \x03(\x01\x12*\n\x0f\x61ngularVelocity\x18\x04 \x01(\x0b\x32\x11.geometry.Vector3\x12!\n\x19\x61ngularVelocityCovariance\x18\x05 \x03(\x01\x12-\n\x12linearAcceleration\x18\x06 \x01(\x0b\x32\x11.geometry.Vector3\x12$\n\x1clinearAccelerationCovariance\x18\x07 \x03(\x01\"\xf3\x01\n\x0cNavSatStatus\x12+\n\x06status\x18\x01 \x01(\x0e\x32\x1b.sensor.NavSatStatus.Status\x12-\n\x07service\x18\x02 \x01(\x0e\x32\x1c.sensor.NavSatStatus.Service\"B\n\x06Status\x12\x07\n\x03\x46IX\x10\x00\x12\x0c\n\x08SBAS_FIX\x10\x01\x12\x0c\n\x08GBAS_FIX\x10\x02\x12\x13\n\x06NO_FIX\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\"C\n\x07Service\x12\x08\n\x04NONE\x10\x00\x12\x07\n\x03GPS\x10\x01\x12\x0b\n\x07GLONASS\x10\x02\x12\x0b\n\x07\x43OMPASS\x10\x04\x12\x0b\n\x07GALILEO\x10\x08\"\xa2\x01\n\tNavSatFix\x12\x1b\n\x06header\x18\x01 \x01(\x0b\x32\x0b.std.Header\x12$\n\x06status\x18\x02 \x01(\x0b\x32\x14.sensor.NavSatStatus\x12\x10\n\x08latitude\x18\x03 \x01(\x01\x12\x11\n\tlongitude\x18\x04 \x01(\x01\x12\x10\n\x08\x61ltitude\x18\x05 \x01(\x01\x12\x1b\n\x13position_covariance\x18\x06 \x03(\x01\x62\x06proto3')
  ,
  dependencies=[std__pb2.DESCRIPTOR,geometry__pb2.DESCRIPTOR,])



_NAVSATSTATUS_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='sensor.NavSatStatus.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='FIX', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SBAS_FIX', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GBAS_FIX', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NO_FIX', index=3, number=-1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=435,
  serialized_end=501,
)
_sym_db.RegisterEnumDescriptor(_NAVSATSTATUS_STATUS)

_NAVSATSTATUS_SERVICE = _descriptor.EnumDescriptor(
  name='Service',
  full_name='sensor.NavSatStatus.Service',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NONE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GPS', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GLONASS', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COMPASS', index=3, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GALILEO', index=4, number=8,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=503,
  serialized_end=570,
)
_sym_db.RegisterEnumDescriptor(_NAVSATSTATUS_SERVICE)


_IMU = _descriptor.Descriptor(
  name='Imu',
  full_name='sensor.Imu',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='sensor.Imu.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='orientation', full_name='sensor.Imu.orientation', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='orientationCovariance', full_name='sensor.Imu.orientationCovariance', index=2,
      number=3, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='angularVelocity', full_name='sensor.Imu.angularVelocity', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='angularVelocityCovariance', full_name='sensor.Imu.angularVelocityCovariance', index=4,
      number=5, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='linearAcceleration', full_name='sensor.Imu.linearAcceleration', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='linearAccelerationCovariance', full_name='sensor.Imu.linearAccelerationCovariance', index=6,
      number=7, type=1, cpp_type=5, label=3,
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
  serialized_start=52,
  serialized_end=324,
)


_NAVSATSTATUS = _descriptor.Descriptor(
  name='NavSatStatus',
  full_name='sensor.NavSatStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='sensor.NavSatStatus.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='service', full_name='sensor.NavSatStatus.service', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _NAVSATSTATUS_STATUS,
    _NAVSATSTATUS_SERVICE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=327,
  serialized_end=570,
)


_NAVSATFIX = _descriptor.Descriptor(
  name='NavSatFix',
  full_name='sensor.NavSatFix',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='sensor.NavSatFix.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='sensor.NavSatFix.status', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='latitude', full_name='sensor.NavSatFix.latitude', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='longitude', full_name='sensor.NavSatFix.longitude', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='altitude', full_name='sensor.NavSatFix.altitude', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='position_covariance', full_name='sensor.NavSatFix.position_covariance', index=5,
      number=6, type=1, cpp_type=5, label=3,
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
  serialized_start=573,
  serialized_end=735,
)

_IMU.fields_by_name['header'].message_type = std__pb2._HEADER
_IMU.fields_by_name['orientation'].message_type = geometry__pb2._QUATERNION
_IMU.fields_by_name['angularVelocity'].message_type = geometry__pb2._VECTOR3
_IMU.fields_by_name['linearAcceleration'].message_type = geometry__pb2._VECTOR3
_NAVSATSTATUS.fields_by_name['status'].enum_type = _NAVSATSTATUS_STATUS
_NAVSATSTATUS.fields_by_name['service'].enum_type = _NAVSATSTATUS_SERVICE
_NAVSATSTATUS_STATUS.containing_type = _NAVSATSTATUS
_NAVSATSTATUS_SERVICE.containing_type = _NAVSATSTATUS
_NAVSATFIX.fields_by_name['header'].message_type = std__pb2._HEADER
_NAVSATFIX.fields_by_name['status'].message_type = _NAVSATSTATUS
DESCRIPTOR.message_types_by_name['Imu'] = _IMU
DESCRIPTOR.message_types_by_name['NavSatStatus'] = _NAVSATSTATUS
DESCRIPTOR.message_types_by_name['NavSatFix'] = _NAVSATFIX
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Imu = _reflection.GeneratedProtocolMessageType('Imu', (_message.Message,), dict(
  DESCRIPTOR = _IMU,
  __module__ = 'sensor_pb2'
  # @@protoc_insertion_point(class_scope:sensor.Imu)
  ))
_sym_db.RegisterMessage(Imu)

NavSatStatus = _reflection.GeneratedProtocolMessageType('NavSatStatus', (_message.Message,), dict(
  DESCRIPTOR = _NAVSATSTATUS,
  __module__ = 'sensor_pb2'
  # @@protoc_insertion_point(class_scope:sensor.NavSatStatus)
  ))
_sym_db.RegisterMessage(NavSatStatus)

NavSatFix = _reflection.GeneratedProtocolMessageType('NavSatFix', (_message.Message,), dict(
  DESCRIPTOR = _NAVSATFIX,
  __module__ = 'sensor_pb2'
  # @@protoc_insertion_point(class_scope:sensor.NavSatFix)
  ))
_sym_db.RegisterMessage(NavSatFix)


# @@protoc_insertion_point(module_scope)
