# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: huawei-devm.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'huawei-devm.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11huawei-devm.proto\x12\x0bhuawei_devm\"\xc6\n\n\x04\x44\x65vm\x12,\n\x08\x63puInfos\x18\x05 \x01(\x0b\x32\x1a.huawei_devm.Devm.CpuInfos\x12\x38\n\x0e\x65thPortStaStss\x18\x07 \x01(\x0b\x32 .huawei_devm.Devm.EthPortStaStss\x12\x32\n\x0bmemoryInfos\x18\x0f \x01(\x0b\x32\x1d.huawei_devm.Devm.MemoryInfos\x12&\n\x05ports\x18\x14 \x01(\x0b\x32\x17.huawei_devm.Devm.Ports\x1a\xcd\x01\n\x08\x43puInfos\x12\x33\n\x07\x63puInfo\x18\x01 \x03(\x0b\x32\".huawei_devm.Devm.CpuInfos.CpuInfo\x1a\x8b\x01\n\x07\x43puInfo\x12\x10\n\x08\x65ntIndex\x18\x01 \x01(\r\x12\x10\n\x08interval\x18\x02 \x01(\r\x12\x17\n\x0fovloadThreshold\x18\x03 \x01(\r\x12\x10\n\x08position\x18\x04 \x01(\t\x12\x16\n\x0esystemCpuUsage\x18\x05 \x01(\r\x12\x19\n\x11unovloadThreshold\x18\x06 \x01(\r\x1a\xca\x01\n\x0e\x45thPortStaStss\x12\x45\n\rethPortStaSts\x18\x01 \x03(\x0b\x32..huawei_devm.Devm.EthPortStaStss.EthPortStaSts\x1aq\n\rEthPortStaSts\x12\x0e\n\x06ifName\x18\x01 \x01(\r\x12\x13\n\x0breceiveByte\x18\x02 \x01(\x04\x12\x15\n\rreceivePacket\x18\x03 \x01(\x04\x12\x10\n\x08sendByte\x18\x04 \x01(\x04\x12\x12\n\nsendPacket\x18\x05 \x01(\x04\x1a\xcd\x03\n\x0bMemoryInfos\x12<\n\nmemoryInfo\x18\x01 \x03(\x0b\x32(.huawei_devm.Devm.MemoryInfos.MemoryInfo\x1a\xff\x02\n\nMemoryInfo\x12\x14\n\x0c\x64oMemoryFree\x18\x01 \x01(\r\x12\x15\n\rdoMemoryTotal\x18\x02 \x01(\r\x12\x15\n\rdoMemoryUsage\x18\x03 \x01(\r\x12\x13\n\x0b\x64oMemoryUse\x18\x04 \x01(\r\x12\x10\n\x08\x65ntIndex\x18\x05 \x01(\r\x12\x14\n\x0cosMemoryFree\x18\x06 \x01(\r\x12\x15\n\rosMemoryTotal\x18\x07 \x01(\r\x12\x15\n\rosMemoryUsage\x18\x08 \x01(\r\x12\x13\n\x0bosMemoryUse\x18\t \x01(\r\x12\x17\n\x0fovloadThreshold\x18\n \x01(\r\x12\x10\n\x08position\x18\x0b \x01(\t\x12\x18\n\x10simpleMemoryFree\x18\x0c \x01(\r\x12\x19\n\x11simpleMemoryTotal\x18\r \x01(\r\x12\x19\n\x11simpleMemoryUsage\x18\x0e \x01(\r\x12\x17\n\x0fsimpleMemoryUse\x18\x0f \x01(\r\x12\x19\n\x11unovloadThreshold\x18\x10 \x01(\r\x1a\x8c\x02\n\x05Ports\x12*\n\x04port\x18\x01 \x03(\x0b\x32\x1c.huawei_devm.Devm.Ports.Port\x1a\xd6\x01\n\x04Port\x12=\n\x0bopticalInfo\x18\x08 \x01(\x0b\x32(.huawei_devm.Devm.Ports.Port.OpticalInfo\x1a\x8e\x01\n\x0bOpticalInfo\x12\x13\n\x0b\x62iasCurrent\x18\x01 \x01(\t\x12\x10\n\x08manuDate\x18\x02 \x01(\t\x12\x10\n\x08position\x18\x0f \x01(\t\x12\x0f\n\x07rxPower\x18\x10 \x01(\t\x12\x13\n\x0btemperature\x18\x11 \x01(\t\x12\x0f\n\x07txPower\x18\x14 \x01(\t\x12\x0f\n\x07voltage\x18\x17 \x01(\tb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'huawei_devm_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_DEVM']._serialized_start=35
  _globals['_DEVM']._serialized_end=1385
  _globals['_DEVM_CPUINFOS']._serialized_start=240
  _globals['_DEVM_CPUINFOS']._serialized_end=445
  _globals['_DEVM_CPUINFOS_CPUINFO']._serialized_start=306
  _globals['_DEVM_CPUINFOS_CPUINFO']._serialized_end=445
  _globals['_DEVM_ETHPORTSTASTSS']._serialized_start=448
  _globals['_DEVM_ETHPORTSTASTSS']._serialized_end=650
  _globals['_DEVM_ETHPORTSTASTSS_ETHPORTSTASTS']._serialized_start=537
  _globals['_DEVM_ETHPORTSTASTSS_ETHPORTSTASTS']._serialized_end=650
  _globals['_DEVM_MEMORYINFOS']._serialized_start=653
  _globals['_DEVM_MEMORYINFOS']._serialized_end=1114
  _globals['_DEVM_MEMORYINFOS_MEMORYINFO']._serialized_start=731
  _globals['_DEVM_MEMORYINFOS_MEMORYINFO']._serialized_end=1114
  _globals['_DEVM_PORTS']._serialized_start=1117
  _globals['_DEVM_PORTS']._serialized_end=1385
  _globals['_DEVM_PORTS_PORT']._serialized_start=1171
  _globals['_DEVM_PORTS_PORT']._serialized_end=1385
  _globals['_DEVM_PORTS_PORT_OPTICALINFO']._serialized_start=1243
  _globals['_DEVM_PORTS_PORT_OPTICALINFO']._serialized_end=1385
# @@protoc_insertion_point(module_scope)
