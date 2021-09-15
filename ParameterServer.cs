// <auto-generated>
//     Generated by the protocol buffer compiler.  DO NOT EDIT!
//     source: parameter_server.proto
// </auto-generated>
#pragma warning disable 1591, 0612, 3021
#region Designer generated code

using pb = global::Google.Protobuf;
using pbc = global::Google.Protobuf.Collections;
using pbr = global::Google.Protobuf.Reflection;
using scg = global::System.Collections.Generic;
namespace Parameterserver {

  /// <summary>Holder for reflection information generated from parameter_server.proto</summary>
  public static partial class ParameterServerReflection {

    #region Descriptor
    /// <summary>File descriptor for parameter_server.proto</summary>
    public static pbr::FileDescriptor Descriptor {
      get { return descriptor; }
    }
    private static pbr::FileDescriptor descriptor;

    static ParameterServerReflection() {
      byte[] descriptorData = global::System.Convert.FromBase64String(
          string.Concat(
            "ChZwYXJhbWV0ZXJfc2VydmVyLnByb3RvEg9wYXJhbWV0ZXJzZXJ2ZXIaCXN0",
            "ZC5wcm90byIfCg9HZXRQYXJhbVJlcXVlc3QSDAoEbmFtZRgBIAEoCSJLCg9T",
            "ZXRQYXJhbVJlcXVlc3QSDAoEbmFtZRgBIAEoCRIqCgV2YWx1ZRgCIAEoCzIb",
            "LnBhcmFtZXRlcnNlcnZlci5QYXJhbVZhbHVlInIKClBhcmFtVmFsdWUSEgoI",
            "dmFsdWVTdHIYASABKAlIABISCgh2YWx1ZUludBgCIAEoBUgAEhMKCXZhbHVl",
            "Qm9vbBgDIAEoCEgAEhUKC3ZhbHVlRG91YmxlGAQgASgBSABCEAoOcGFyYW1l",
            "dGVyVmFsdWUyogEKD1BhcmFtZXRlclNlcnZlchJPCgxHZXRQYXJhbWV0ZXIS",
            "IC5wYXJhbWV0ZXJzZXJ2ZXIuR2V0UGFyYW1SZXF1ZXN0GhsucGFyYW1ldGVy",
            "c2VydmVyLlBhcmFtVmFsdWUiABI+CgxTZXRQYXJhbWV0ZXISIC5wYXJhbWV0",
            "ZXJzZXJ2ZXIuU2V0UGFyYW1SZXF1ZXN0Ggouc3RkLkVtcHR5IgBiBnByb3Rv",
            "Mw=="));
      descriptor = pbr::FileDescriptor.FromGeneratedCode(descriptorData,
          new pbr::FileDescriptor[] { global::Std.StdReflection.Descriptor, },
          new pbr::GeneratedClrTypeInfo(null, new pbr::GeneratedClrTypeInfo[] {
            new pbr::GeneratedClrTypeInfo(typeof(global::Parameterserver.GetParamRequest), global::Parameterserver.GetParamRequest.Parser, new[]{ "Name" }, null, null, null),
            new pbr::GeneratedClrTypeInfo(typeof(global::Parameterserver.SetParamRequest), global::Parameterserver.SetParamRequest.Parser, new[]{ "Name", "Value" }, null, null, null),
            new pbr::GeneratedClrTypeInfo(typeof(global::Parameterserver.ParamValue), global::Parameterserver.ParamValue.Parser, new[]{ "ValueStr", "ValueInt", "ValueBool", "ValueDouble" }, new[]{ "ParameterValue" }, null, null)
          }));
    }
    #endregion

  }
  #region Messages
  public sealed partial class GetParamRequest : pb::IMessage<GetParamRequest> {
    private static readonly pb::MessageParser<GetParamRequest> _parser = new pb::MessageParser<GetParamRequest>(() => new GetParamRequest());
    private pb::UnknownFieldSet _unknownFields;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public static pb::MessageParser<GetParamRequest> Parser { get { return _parser; } }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public static pbr::MessageDescriptor Descriptor {
      get { return global::Parameterserver.ParameterServerReflection.Descriptor.MessageTypes[0]; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    pbr::MessageDescriptor pb::IMessage.Descriptor {
      get { return Descriptor; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public GetParamRequest() {
      OnConstruction();
    }

    partial void OnConstruction();

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public GetParamRequest(GetParamRequest other) : this() {
      name_ = other.name_;
      _unknownFields = pb::UnknownFieldSet.Clone(other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public GetParamRequest Clone() {
      return new GetParamRequest(this);
    }

    /// <summary>Field number for the "name" field.</summary>
    public const int NameFieldNumber = 1;
    private string name_ = "";
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public string Name {
      get { return name_; }
      set {
        name_ = pb::ProtoPreconditions.CheckNotNull(value, "value");
      }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override bool Equals(object other) {
      return Equals(other as GetParamRequest);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public bool Equals(GetParamRequest other) {
      if (ReferenceEquals(other, null)) {
        return false;
      }
      if (ReferenceEquals(other, this)) {
        return true;
      }
      if (Name != other.Name) return false;
      return Equals(_unknownFields, other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override int GetHashCode() {
      int hash = 1;
      if (Name.Length != 0) hash ^= Name.GetHashCode();
      if (_unknownFields != null) {
        hash ^= _unknownFields.GetHashCode();
      }
      return hash;
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override string ToString() {
      return pb::JsonFormatter.ToDiagnosticString(this);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public void WriteTo(pb::CodedOutputStream output) {
      if (Name.Length != 0) {
        output.WriteRawTag(10);
        output.WriteString(Name);
      }
      if (_unknownFields != null) {
        _unknownFields.WriteTo(output);
      }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public int CalculateSize() {
      int size = 0;
      if (Name.Length != 0) {
        size += 1 + pb::CodedOutputStream.ComputeStringSize(Name);
      }
      if (_unknownFields != null) {
        size += _unknownFields.CalculateSize();
      }
      return size;
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public void MergeFrom(GetParamRequest other) {
      if (other == null) {
        return;
      }
      if (other.Name.Length != 0) {
        Name = other.Name;
      }
      _unknownFields = pb::UnknownFieldSet.MergeFrom(_unknownFields, other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public void MergeFrom(pb::CodedInputStream input) {
      uint tag;
      while ((tag = input.ReadTag()) != 0) {
        switch(tag) {
          default:
            _unknownFields = pb::UnknownFieldSet.MergeFieldFrom(_unknownFields, input);
            break;
          case 10: {
            Name = input.ReadString();
            break;
          }
        }
      }
    }

  }

  public sealed partial class SetParamRequest : pb::IMessage<SetParamRequest> {
    private static readonly pb::MessageParser<SetParamRequest> _parser = new pb::MessageParser<SetParamRequest>(() => new SetParamRequest());
    private pb::UnknownFieldSet _unknownFields;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public static pb::MessageParser<SetParamRequest> Parser { get { return _parser; } }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public static pbr::MessageDescriptor Descriptor {
      get { return global::Parameterserver.ParameterServerReflection.Descriptor.MessageTypes[1]; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    pbr::MessageDescriptor pb::IMessage.Descriptor {
      get { return Descriptor; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public SetParamRequest() {
      OnConstruction();
    }

    partial void OnConstruction();

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public SetParamRequest(SetParamRequest other) : this() {
      name_ = other.name_;
      value_ = other.value_ != null ? other.value_.Clone() : null;
      _unknownFields = pb::UnknownFieldSet.Clone(other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public SetParamRequest Clone() {
      return new SetParamRequest(this);
    }

    /// <summary>Field number for the "name" field.</summary>
    public const int NameFieldNumber = 1;
    private string name_ = "";
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public string Name {
      get { return name_; }
      set {
        name_ = pb::ProtoPreconditions.CheckNotNull(value, "value");
      }
    }

    /// <summary>Field number for the "value" field.</summary>
    public const int ValueFieldNumber = 2;
    private global::Parameterserver.ParamValue value_;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public global::Parameterserver.ParamValue Value {
      get { return value_; }
      set {
        value_ = value;
      }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override bool Equals(object other) {
      return Equals(other as SetParamRequest);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public bool Equals(SetParamRequest other) {
      if (ReferenceEquals(other, null)) {
        return false;
      }
      if (ReferenceEquals(other, this)) {
        return true;
      }
      if (Name != other.Name) return false;
      if (!object.Equals(Value, other.Value)) return false;
      return Equals(_unknownFields, other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override int GetHashCode() {
      int hash = 1;
      if (Name.Length != 0) hash ^= Name.GetHashCode();
      if (value_ != null) hash ^= Value.GetHashCode();
      if (_unknownFields != null) {
        hash ^= _unknownFields.GetHashCode();
      }
      return hash;
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override string ToString() {
      return pb::JsonFormatter.ToDiagnosticString(this);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public void WriteTo(pb::CodedOutputStream output) {
      if (Name.Length != 0) {
        output.WriteRawTag(10);
        output.WriteString(Name);
      }
      if (value_ != null) {
        output.WriteRawTag(18);
        output.WriteMessage(Value);
      }
      if (_unknownFields != null) {
        _unknownFields.WriteTo(output);
      }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public int CalculateSize() {
      int size = 0;
      if (Name.Length != 0) {
        size += 1 + pb::CodedOutputStream.ComputeStringSize(Name);
      }
      if (value_ != null) {
        size += 1 + pb::CodedOutputStream.ComputeMessageSize(Value);
      }
      if (_unknownFields != null) {
        size += _unknownFields.CalculateSize();
      }
      return size;
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public void MergeFrom(SetParamRequest other) {
      if (other == null) {
        return;
      }
      if (other.Name.Length != 0) {
        Name = other.Name;
      }
      if (other.value_ != null) {
        if (value_ == null) {
          value_ = new global::Parameterserver.ParamValue();
        }
        Value.MergeFrom(other.Value);
      }
      _unknownFields = pb::UnknownFieldSet.MergeFrom(_unknownFields, other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public void MergeFrom(pb::CodedInputStream input) {
      uint tag;
      while ((tag = input.ReadTag()) != 0) {
        switch(tag) {
          default:
            _unknownFields = pb::UnknownFieldSet.MergeFieldFrom(_unknownFields, input);
            break;
          case 10: {
            Name = input.ReadString();
            break;
          }
          case 18: {
            if (value_ == null) {
              value_ = new global::Parameterserver.ParamValue();
            }
            input.ReadMessage(value_);
            break;
          }
        }
      }
    }

  }

  public sealed partial class ParamValue : pb::IMessage<ParamValue> {
    private static readonly pb::MessageParser<ParamValue> _parser = new pb::MessageParser<ParamValue>(() => new ParamValue());
    private pb::UnknownFieldSet _unknownFields;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public static pb::MessageParser<ParamValue> Parser { get { return _parser; } }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public static pbr::MessageDescriptor Descriptor {
      get { return global::Parameterserver.ParameterServerReflection.Descriptor.MessageTypes[2]; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    pbr::MessageDescriptor pb::IMessage.Descriptor {
      get { return Descriptor; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public ParamValue() {
      OnConstruction();
    }

    partial void OnConstruction();

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public ParamValue(ParamValue other) : this() {
      switch (other.ParameterValueCase) {
        case ParameterValueOneofCase.ValueStr:
          ValueStr = other.ValueStr;
          break;
        case ParameterValueOneofCase.ValueInt:
          ValueInt = other.ValueInt;
          break;
        case ParameterValueOneofCase.ValueBool:
          ValueBool = other.ValueBool;
          break;
        case ParameterValueOneofCase.ValueDouble:
          ValueDouble = other.ValueDouble;
          break;
      }

      _unknownFields = pb::UnknownFieldSet.Clone(other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public ParamValue Clone() {
      return new ParamValue(this);
    }

    /// <summary>Field number for the "valueStr" field.</summary>
    public const int ValueStrFieldNumber = 1;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public string ValueStr {
      get { return parameterValueCase_ == ParameterValueOneofCase.ValueStr ? (string) parameterValue_ : ""; }
      set {
        parameterValue_ = pb::ProtoPreconditions.CheckNotNull(value, "value");
        parameterValueCase_ = ParameterValueOneofCase.ValueStr;
      }
    }

    /// <summary>Field number for the "valueInt" field.</summary>
    public const int ValueIntFieldNumber = 2;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public int ValueInt {
      get { return parameterValueCase_ == ParameterValueOneofCase.ValueInt ? (int) parameterValue_ : 0; }
      set {
        parameterValue_ = value;
        parameterValueCase_ = ParameterValueOneofCase.ValueInt;
      }
    }

    /// <summary>Field number for the "valueBool" field.</summary>
    public const int ValueBoolFieldNumber = 3;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public bool ValueBool {
      get { return parameterValueCase_ == ParameterValueOneofCase.ValueBool ? (bool) parameterValue_ : false; }
      set {
        parameterValue_ = value;
        parameterValueCase_ = ParameterValueOneofCase.ValueBool;
      }
    }

    /// <summary>Field number for the "valueDouble" field.</summary>
    public const int ValueDoubleFieldNumber = 4;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public double ValueDouble {
      get { return parameterValueCase_ == ParameterValueOneofCase.ValueDouble ? (double) parameterValue_ : 0D; }
      set {
        parameterValue_ = value;
        parameterValueCase_ = ParameterValueOneofCase.ValueDouble;
      }
    }

    private object parameterValue_;
    /// <summary>Enum of possible cases for the "parameterValue" oneof.</summary>
    public enum ParameterValueOneofCase {
      None = 0,
      ValueStr = 1,
      ValueInt = 2,
      ValueBool = 3,
      ValueDouble = 4,
    }
    private ParameterValueOneofCase parameterValueCase_ = ParameterValueOneofCase.None;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public ParameterValueOneofCase ParameterValueCase {
      get { return parameterValueCase_; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public void ClearParameterValue() {
      parameterValueCase_ = ParameterValueOneofCase.None;
      parameterValue_ = null;
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override bool Equals(object other) {
      return Equals(other as ParamValue);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public bool Equals(ParamValue other) {
      if (ReferenceEquals(other, null)) {
        return false;
      }
      if (ReferenceEquals(other, this)) {
        return true;
      }
      if (ValueStr != other.ValueStr) return false;
      if (ValueInt != other.ValueInt) return false;
      if (ValueBool != other.ValueBool) return false;
      if (!pbc::ProtobufEqualityComparers.BitwiseDoubleEqualityComparer.Equals(ValueDouble, other.ValueDouble)) return false;
      if (ParameterValueCase != other.ParameterValueCase) return false;
      return Equals(_unknownFields, other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override int GetHashCode() {
      int hash = 1;
      if (parameterValueCase_ == ParameterValueOneofCase.ValueStr) hash ^= ValueStr.GetHashCode();
      if (parameterValueCase_ == ParameterValueOneofCase.ValueInt) hash ^= ValueInt.GetHashCode();
      if (parameterValueCase_ == ParameterValueOneofCase.ValueBool) hash ^= ValueBool.GetHashCode();
      if (parameterValueCase_ == ParameterValueOneofCase.ValueDouble) hash ^= pbc::ProtobufEqualityComparers.BitwiseDoubleEqualityComparer.GetHashCode(ValueDouble);
      hash ^= (int) parameterValueCase_;
      if (_unknownFields != null) {
        hash ^= _unknownFields.GetHashCode();
      }
      return hash;
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override string ToString() {
      return pb::JsonFormatter.ToDiagnosticString(this);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public void WriteTo(pb::CodedOutputStream output) {
      if (parameterValueCase_ == ParameterValueOneofCase.ValueStr) {
        output.WriteRawTag(10);
        output.WriteString(ValueStr);
      }
      if (parameterValueCase_ == ParameterValueOneofCase.ValueInt) {
        output.WriteRawTag(16);
        output.WriteInt32(ValueInt);
      }
      if (parameterValueCase_ == ParameterValueOneofCase.ValueBool) {
        output.WriteRawTag(24);
        output.WriteBool(ValueBool);
      }
      if (parameterValueCase_ == ParameterValueOneofCase.ValueDouble) {
        output.WriteRawTag(33);
        output.WriteDouble(ValueDouble);
      }
      if (_unknownFields != null) {
        _unknownFields.WriteTo(output);
      }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public int CalculateSize() {
      int size = 0;
      if (parameterValueCase_ == ParameterValueOneofCase.ValueStr) {
        size += 1 + pb::CodedOutputStream.ComputeStringSize(ValueStr);
      }
      if (parameterValueCase_ == ParameterValueOneofCase.ValueInt) {
        size += 1 + pb::CodedOutputStream.ComputeInt32Size(ValueInt);
      }
      if (parameterValueCase_ == ParameterValueOneofCase.ValueBool) {
        size += 1 + 1;
      }
      if (parameterValueCase_ == ParameterValueOneofCase.ValueDouble) {
        size += 1 + 8;
      }
      if (_unknownFields != null) {
        size += _unknownFields.CalculateSize();
      }
      return size;
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public void MergeFrom(ParamValue other) {
      if (other == null) {
        return;
      }
      switch (other.ParameterValueCase) {
        case ParameterValueOneofCase.ValueStr:
          ValueStr = other.ValueStr;
          break;
        case ParameterValueOneofCase.ValueInt:
          ValueInt = other.ValueInt;
          break;
        case ParameterValueOneofCase.ValueBool:
          ValueBool = other.ValueBool;
          break;
        case ParameterValueOneofCase.ValueDouble:
          ValueDouble = other.ValueDouble;
          break;
      }

      _unknownFields = pb::UnknownFieldSet.MergeFrom(_unknownFields, other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public void MergeFrom(pb::CodedInputStream input) {
      uint tag;
      while ((tag = input.ReadTag()) != 0) {
        switch(tag) {
          default:
            _unknownFields = pb::UnknownFieldSet.MergeFieldFrom(_unknownFields, input);
            break;
          case 10: {
            ValueStr = input.ReadString();
            break;
          }
          case 16: {
            ValueInt = input.ReadInt32();
            break;
          }
          case 24: {
            ValueBool = input.ReadBool();
            break;
          }
          case 33: {
            ValueDouble = input.ReadDouble();
            break;
          }
        }
      }
    }

  }

  #endregion

}

#endregion Designer generated code
