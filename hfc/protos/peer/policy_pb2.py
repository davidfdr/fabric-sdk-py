# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: hfc/protos/peer/policy.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from hfc.protos.common import policies_pb2 as hfc_dot_protos_dot_common_dot_policies__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1chfc/protos/peer/policy.proto\x12\x06protos\x1a hfc/protos/common/policies.proto\"\x83\x01\n\x11\x41pplicationPolicy\x12;\n\x10signature_policy\x18\x01 \x01(\x0b\x32\x1f.common.SignaturePolicyEnvelopeH\x00\x12)\n\x1f\x63hannel_config_policy_reference\x18\x02 \x01(\tH\x00\x42\x06\n\x04TypeBR\n\"org.hyperledger.fabric.protos.peerZ,github.com/hyperledger/fabric-protos-go/peerb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'hfc.protos.peer.policy_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\"org.hyperledger.fabric.protos.peerZ,github.com/hyperledger/fabric-protos-go/peer'
  _globals['_APPLICATIONPOLICY']._serialized_start=75
  _globals['_APPLICATIONPOLICY']._serialized_end=206
# @@protoc_insertion_point(module_scope)
