# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Lemmatizer.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='Lemmatizer.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x10Lemmatizer.proto\"\x1d\n\nTestString\x12\x0f\n\x07message\x18\x01 \x01(\t\"\x1b\n\x08\x44ocument\x12\x0f\n\x07\x63ontent\x18\x01 \x01(\t\"8\n\x05Query\x12\x12\n\nsearchTerm\x18\x01 \x01(\t\x12\x1b\n\x08\x64ocument\x18\x02 \x01(\x0b\x32\t.Document\"[\n\tLocations\x12&\n\tlocations\x18\x01 \x03(\x0b\x32\x13.Locations.Location\x1a&\n\x08Location\x12\r\n\x05start\x18\x01 \x01(\x03\x12\x0b\n\x03\x65nd\x18\x02 \x01(\x03\"8\n\x14LemmasAndFrequencies\x12\r\n\x05lemma\x18\x01 \x03(\t\x12\x11\n\tfrequency\x18\x02 \x03(\x03\x32\xa4\x01\n\nLemmatizer\x12\x39\n!LemmaSentencesForUnionisedRequest\x12\x06.Query\x1a\n.Locations\"\x00\x12\x37\n\x11LemmasForDocument\x12\t.Document\x1a\x15.LemmasAndFrequencies\"\x00\x12\"\n\x04Test\x12\x0b.TestString\x1a\x0b.TestString\"\x00\x62\x06proto3')
)




_TESTSTRING = _descriptor.Descriptor(
  name='TestString',
  full_name='TestString',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='TestString.message', index=0,
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
  serialized_start=20,
  serialized_end=49,
)


_DOCUMENT = _descriptor.Descriptor(
  name='Document',
  full_name='Document',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='content', full_name='Document.content', index=0,
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
  serialized_start=51,
  serialized_end=78,
)


_QUERY = _descriptor.Descriptor(
  name='Query',
  full_name='Query',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='searchTerm', full_name='Query.searchTerm', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='document', full_name='Query.document', index=1,
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
  serialized_start=80,
  serialized_end=136,
)


_LOCATIONS_LOCATION = _descriptor.Descriptor(
  name='Location',
  full_name='Locations.Location',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='start', full_name='Locations.Location.start', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='end', full_name='Locations.Location.end', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=191,
  serialized_end=229,
)

_LOCATIONS = _descriptor.Descriptor(
  name='Locations',
  full_name='Locations',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='locations', full_name='Locations.locations', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_LOCATIONS_LOCATION, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=138,
  serialized_end=229,
)


_LEMMASANDFREQUENCIES = _descriptor.Descriptor(
  name='LemmasAndFrequencies',
  full_name='LemmasAndFrequencies',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='lemma', full_name='LemmasAndFrequencies.lemma', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='frequency', full_name='LemmasAndFrequencies.frequency', index=1,
      number=2, type=3, cpp_type=2, label=3,
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
  serialized_start=231,
  serialized_end=287,
)

_QUERY.fields_by_name['document'].message_type = _DOCUMENT
_LOCATIONS_LOCATION.containing_type = _LOCATIONS
_LOCATIONS.fields_by_name['locations'].message_type = _LOCATIONS_LOCATION
DESCRIPTOR.message_types_by_name['TestString'] = _TESTSTRING
DESCRIPTOR.message_types_by_name['Document'] = _DOCUMENT
DESCRIPTOR.message_types_by_name['Query'] = _QUERY
DESCRIPTOR.message_types_by_name['Locations'] = _LOCATIONS
DESCRIPTOR.message_types_by_name['LemmasAndFrequencies'] = _LEMMASANDFREQUENCIES
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TestString = _reflection.GeneratedProtocolMessageType('TestString', (_message.Message,), dict(
  DESCRIPTOR = _TESTSTRING,
  __module__ = 'Lemmatizer_pb2'
  # @@protoc_insertion_point(class_scope:TestString)
  ))
_sym_db.RegisterMessage(TestString)

Document = _reflection.GeneratedProtocolMessageType('Document', (_message.Message,), dict(
  DESCRIPTOR = _DOCUMENT,
  __module__ = 'Lemmatizer_pb2'
  # @@protoc_insertion_point(class_scope:Document)
  ))
_sym_db.RegisterMessage(Document)

Query = _reflection.GeneratedProtocolMessageType('Query', (_message.Message,), dict(
  DESCRIPTOR = _QUERY,
  __module__ = 'Lemmatizer_pb2'
  # @@protoc_insertion_point(class_scope:Query)
  ))
_sym_db.RegisterMessage(Query)

Locations = _reflection.GeneratedProtocolMessageType('Locations', (_message.Message,), dict(

  Location = _reflection.GeneratedProtocolMessageType('Location', (_message.Message,), dict(
    DESCRIPTOR = _LOCATIONS_LOCATION,
    __module__ = 'Lemmatizer_pb2'
    # @@protoc_insertion_point(class_scope:Locations.Location)
    ))
  ,
  DESCRIPTOR = _LOCATIONS,
  __module__ = 'Lemmatizer_pb2'
  # @@protoc_insertion_point(class_scope:Locations)
  ))
_sym_db.RegisterMessage(Locations)
_sym_db.RegisterMessage(Locations.Location)

LemmasAndFrequencies = _reflection.GeneratedProtocolMessageType('LemmasAndFrequencies', (_message.Message,), dict(
  DESCRIPTOR = _LEMMASANDFREQUENCIES,
  __module__ = 'Lemmatizer_pb2'
  # @@protoc_insertion_point(class_scope:LemmasAndFrequencies)
  ))
_sym_db.RegisterMessage(LemmasAndFrequencies)



_LEMMATIZER = _descriptor.ServiceDescriptor(
  name='Lemmatizer',
  full_name='Lemmatizer',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=290,
  serialized_end=454,
  methods=[
  _descriptor.MethodDescriptor(
    name='LemmaSentencesForUnionisedRequest',
    full_name='Lemmatizer.LemmaSentencesForUnionisedRequest',
    index=0,
    containing_service=None,
    input_type=_QUERY,
    output_type=_LOCATIONS,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='LemmasForDocument',
    full_name='Lemmatizer.LemmasForDocument',
    index=1,
    containing_service=None,
    input_type=_DOCUMENT,
    output_type=_LEMMASANDFREQUENCIES,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Test',
    full_name='Lemmatizer.Test',
    index=2,
    containing_service=None,
    input_type=_TESTSTRING,
    output_type=_TESTSTRING,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_LEMMATIZER)

DESCRIPTOR.services_by_name['Lemmatizer'] = _LEMMATIZER

# @@protoc_insertion_point(module_scope)
