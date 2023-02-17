# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: visualization.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import std_pb2 as std__pb2
import geometry_pb2 as geometry__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='visualization.proto',
  package='visualization',
  syntax='proto3',
  serialized_options=b'\n\036io.grpc.examples.visualizationB\rVisualizationP\001\242\002\003HLW',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x13visualization.proto\x12\rvisualization\x1a\tstd.proto\x1a\x0egeometry.proto\" \n\rMarkerRequest\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\"\x9b\x05\n\x06Marker\x12\x1b\n\x06header\x18\x01 \x01(\x0b\x32\x0b.std.Header\x12\n\n\x02ns\x18\x02 \x01(\t\x12\n\n\x02id\x18\x03 \x01(\x05\x12(\n\x04type\x18\x04 \x01(\x0e\x32\x1a.visualization.Marker.Type\x12,\n\x06\x61\x63tion\x18\x05 \x01(\x0e\x32\x1c.visualization.Marker.Action\x12\x1c\n\x04pose\x18\x06 \x01(\x0b\x32\x0e.geometry.Pose\x12 \n\x05scale\x18\x07 \x01(\x0b\x32\x11.geometry.Vector3\x12\x1d\n\x05\x63olor\x18\x08 \x01(\x0b\x32\x0e.std.ColorRGBA\x12\x10\n\x08lifetime\x18\t \x01(\x02\x12\x13\n\x0b\x66rameLocked\x18\n \x01(\x08\x12\x1f\n\x06points\x18\x0b \x03(\x0b\x32\x0f.geometry.Point\x12\x1e\n\x06\x63olors\x18\x0c \x03(\x0b\x32\x0e.std.ColorRGBA\x12\x0c\n\x04text\x18\r \x01(\t\x12\x14\n\x0cmeshResource\x18\x0e \x01(\t\x12 \n\x18meshUseEmbeddedMaterials\x18\x0f \x01(\x08\"\xbc\x01\n\x04Type\x12\t\n\x05\x41RROW\x10\x00\x12\x08\n\x04\x43UBE\x10\x01\x12\n\n\x06SPHERE\x10\x02\x12\x0c\n\x08\x43YLINDER\x10\x03\x12\x0e\n\nLINE_STRIP\x10\x04\x12\r\n\tLINE_LIST\x10\x05\x12\r\n\tCUBE_LIST\x10\x06\x12\x0f\n\x0bSPHERE_LIST\x10\x07\x12\n\n\x06POINTS\x10\x08\x12\x14\n\x10TEXT_VIEW_FACING\x10\t\x12\x11\n\rMESH_RESOURCE\x10\n\x12\x11\n\rTRIANGLE_LIST\x10\x0b\"8\n\x06\x41\x63tion\x12\x07\n\x03\x41\x44\x44\x10\x00\x12\n\n\x06MODIFY\x10\x01\x12\n\n\x06\x44\x45LETE\x10\x02\x12\r\n\tDELETEALL\x10\x03\"R\n\x0bMarkerArray\x12\x1b\n\x06header\x18\x01 \x01(\x0b\x32\x0b.std.Header\x12&\n\x07markers\x18\x02 \x03(\x0b\x32\x15.visualization.Marker2\xa5\x01\n\rVisualization\x12\x44\n\tSetMarker\x12\x1c.visualization.MarkerRequest\x1a\x15.visualization.Marker\"\x00\x30\x01\x12N\n\x0eSetMarkerArray\x12\x1c.visualization.MarkerRequest\x1a\x1a.visualization.MarkerArray\"\x00\x30\x01\x42\x37\n\x1eio.grpc.examples.visualizationB\rVisualizationP\x01\xa2\x02\x03HLWb\x06proto3'
  ,
  dependencies=[std__pb2.DESCRIPTOR,geometry__pb2.DESCRIPTOR,])



_MARKER_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='visualization.Marker.Type',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ARROW', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CUBE', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SPHERE', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CYLINDER', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LINE_STRIP', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LINE_LIST', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CUBE_LIST', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SPHERE_LIST', index=7, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='POINTS', index=8, number=8,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TEXT_VIEW_FACING', index=9, number=9,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MESH_RESOURCE', index=10, number=10,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TRIANGLE_LIST', index=11, number=11,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=521,
  serialized_end=709,
)
_sym_db.RegisterEnumDescriptor(_MARKER_TYPE)

_MARKER_ACTION = _descriptor.EnumDescriptor(
  name='Action',
  full_name='visualization.Marker.Action',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ADD', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MODIFY', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DELETE', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DELETEALL', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=711,
  serialized_end=767,
)
_sym_db.RegisterEnumDescriptor(_MARKER_ACTION)


_MARKERREQUEST = _descriptor.Descriptor(
  name='MarkerRequest',
  full_name='visualization.MarkerRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='address', full_name='visualization.MarkerRequest.address', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=65,
  serialized_end=97,
)


_MARKER = _descriptor.Descriptor(
  name='Marker',
  full_name='visualization.Marker',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='visualization.Marker.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ns', full_name='visualization.Marker.ns', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='id', full_name='visualization.Marker.id', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='visualization.Marker.type', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='action', full_name='visualization.Marker.action', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pose', full_name='visualization.Marker.pose', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='scale', full_name='visualization.Marker.scale', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='color', full_name='visualization.Marker.color', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='lifetime', full_name='visualization.Marker.lifetime', index=8,
      number=9, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='frameLocked', full_name='visualization.Marker.frameLocked', index=9,
      number=10, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='points', full_name='visualization.Marker.points', index=10,
      number=11, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='colors', full_name='visualization.Marker.colors', index=11,
      number=12, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='text', full_name='visualization.Marker.text', index=12,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='meshResource', full_name='visualization.Marker.meshResource', index=13,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='meshUseEmbeddedMaterials', full_name='visualization.Marker.meshUseEmbeddedMaterials', index=14,
      number=15, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _MARKER_TYPE,
    _MARKER_ACTION,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=100,
  serialized_end=767,
)


_MARKERARRAY = _descriptor.Descriptor(
  name='MarkerArray',
  full_name='visualization.MarkerArray',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='visualization.MarkerArray.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='markers', full_name='visualization.MarkerArray.markers', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=769,
  serialized_end=851,
)

_MARKER.fields_by_name['header'].message_type = std__pb2._HEADER
_MARKER.fields_by_name['type'].enum_type = _MARKER_TYPE
_MARKER.fields_by_name['action'].enum_type = _MARKER_ACTION
_MARKER.fields_by_name['pose'].message_type = geometry__pb2._POSE
_MARKER.fields_by_name['scale'].message_type = geometry__pb2._VECTOR3
_MARKER.fields_by_name['color'].message_type = std__pb2._COLORRGBA
_MARKER.fields_by_name['points'].message_type = geometry__pb2._POINT
_MARKER.fields_by_name['colors'].message_type = std__pb2._COLORRGBA
_MARKER_TYPE.containing_type = _MARKER
_MARKER_ACTION.containing_type = _MARKER
_MARKERARRAY.fields_by_name['header'].message_type = std__pb2._HEADER
_MARKERARRAY.fields_by_name['markers'].message_type = _MARKER
DESCRIPTOR.message_types_by_name['MarkerRequest'] = _MARKERREQUEST
DESCRIPTOR.message_types_by_name['Marker'] = _MARKER
DESCRIPTOR.message_types_by_name['MarkerArray'] = _MARKERARRAY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MarkerRequest = _reflection.GeneratedProtocolMessageType('MarkerRequest', (_message.Message,), {
  'DESCRIPTOR' : _MARKERREQUEST,
  '__module__' : 'visualization_pb2'
  # @@protoc_insertion_point(class_scope:visualization.MarkerRequest)
  })
_sym_db.RegisterMessage(MarkerRequest)

Marker = _reflection.GeneratedProtocolMessageType('Marker', (_message.Message,), {
  'DESCRIPTOR' : _MARKER,
  '__module__' : 'visualization_pb2'
  # @@protoc_insertion_point(class_scope:visualization.Marker)
  })
_sym_db.RegisterMessage(Marker)

MarkerArray = _reflection.GeneratedProtocolMessageType('MarkerArray', (_message.Message,), {
  'DESCRIPTOR' : _MARKERARRAY,
  '__module__' : 'visualization_pb2'
  # @@protoc_insertion_point(class_scope:visualization.MarkerArray)
  })
_sym_db.RegisterMessage(MarkerArray)


DESCRIPTOR._options = None

_VISUALIZATION = _descriptor.ServiceDescriptor(
  name='Visualization',
  full_name='visualization.Visualization',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=854,
  serialized_end=1019,
  methods=[
  _descriptor.MethodDescriptor(
    name='SetMarker',
    full_name='visualization.Visualization.SetMarker',
    index=0,
    containing_service=None,
    input_type=_MARKERREQUEST,
    output_type=_MARKER,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='SetMarkerArray',
    full_name='visualization.Visualization.SetMarkerArray',
    index=1,
    containing_service=None,
    input_type=_MARKERREQUEST,
    output_type=_MARKERARRAY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_VISUALIZATION)

DESCRIPTOR.services_by_name['Visualization'] = _VISUALIZATION

# @@protoc_insertion_point(module_scope)
