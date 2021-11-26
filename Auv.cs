// <auto-generated>
//     Generated by the protocol buffer compiler.  DO NOT EDIT!
//     source: auv.proto
// </auto-generated>
#pragma warning disable 1591, 0612, 3021
#region Designer generated code

using pb = global::Google.Protobuf;
using pbc = global::Google.Protobuf.Collections;
using pbr = global::Google.Protobuf.Reflection;
using scg = global::System.Collections.Generic;
namespace Auv {

  /// <summary>Holder for reflection information generated from auv.proto</summary>
  public static partial class AuvReflection {

    #region Descriptor
    /// <summary>File descriptor for auv.proto</summary>
    public static pbr::FileDescriptor Descriptor {
      get { return descriptor; }
    }
    private static pbr::FileDescriptor descriptor;

    static AuvReflection() {
      byte[] descriptorData = global::System.Convert.FromBase64String(
          string.Concat(
            "CglhdXYucHJvdG8SA2F1dhoJc3RkLnByb3RvGhBnZW9ncmFwaGljLnByb3Rv",
            "Gg5nZW9tZXRyeS5wcm90byIxCgNORUQSDQoFbm9ydGgYASABKAESDAoEZWFz",
            "dBgCIAEoARINCgVkZXB0aBgDIAEoASKdAwoQTmF2aWdhdGlvblN0YXR1cxIb",
            "CgZoZWFkZXIYASABKAsyCy5zdGQuSGVhZGVyEiwKDmdsb2JhbFBvc2l0aW9u",
            "GAIgASgLMhQuZ2VvZ3JhcGhpYy5HZW9Qb2ludBIkCgZvcmlnaW4YAyABKAsy",
            "FC5nZW9ncmFwaGljLkdlb1BvaW50EhoKCHBvc2l0aW9uGAQgASgLMgguYXV2",
            "Lk5FRBInCgxib2R5VmVsb2NpdHkYBSABKAsyES5nZW9tZXRyeS5WZWN0b3Iz",
            "EisKEHNlYWZsb29yVmVsb2NpdHkYBiABKAsyES5nZW9tZXRyeS5WZWN0b3Iz",
            "EiYKC29yaWVudGF0aW9uGAcgASgLMhEuZ2VvbWV0cnkuVmVjdG9yMxIqCg9v",
            "cmllbnRhdGlvblJhdGUYCCABKAsyES5nZW9tZXRyeS5WZWN0b3IzEiIKEHBv",
            "c2l0aW9uVmFyaWFuY2UYCSABKAsyCC5hdXYuTkVEEi4KE29yaWVudGF0aW9u",
            "VmFyaWFuY2UYCiABKAsyES5nZW9tZXRyeS5WZWN0b3IzYgZwcm90bzM="));
      descriptor = pbr::FileDescriptor.FromGeneratedCode(descriptorData,
          new pbr::FileDescriptor[] { global::Std.StdReflection.Descriptor, global::Geographic.GeographicReflection.Descriptor, global::Geometry.GeometryReflection.Descriptor, },
          new pbr::GeneratedClrTypeInfo(null, new pbr::GeneratedClrTypeInfo[] {
            new pbr::GeneratedClrTypeInfo(typeof(global::Auv.NED), global::Auv.NED.Parser, new[]{ "North", "East", "Depth" }, null, null, null),
            new pbr::GeneratedClrTypeInfo(typeof(global::Auv.NavigationStatus), global::Auv.NavigationStatus.Parser, new[]{ "Header", "GlobalPosition", "Origin", "Position", "BodyVelocity", "SeafloorVelocity", "Orientation", "OrientationRate", "PositionVariance", "OrientationVariance" }, null, null, null)
          }));
    }
    #endregion

  }
  #region Messages
  public sealed partial class NED : pb::IMessage<NED> {
    private static readonly pb::MessageParser<NED> _parser = new pb::MessageParser<NED>(() => new NED());
    private pb::UnknownFieldSet _unknownFields;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public static pb::MessageParser<NED> Parser { get { return _parser; } }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public static pbr::MessageDescriptor Descriptor {
      get { return global::Auv.AuvReflection.Descriptor.MessageTypes[0]; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    pbr::MessageDescriptor pb::IMessage.Descriptor {
      get { return Descriptor; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public NED() {
      OnConstruction();
    }

    partial void OnConstruction();

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public NED(NED other) : this() {
      north_ = other.north_;
      east_ = other.east_;
      depth_ = other.depth_;
      _unknownFields = pb::UnknownFieldSet.Clone(other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public NED Clone() {
      return new NED(this);
    }

    /// <summary>Field number for the "north" field.</summary>
    public const int NorthFieldNumber = 1;
    private double north_;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public double North {
      get { return north_; }
      set {
        north_ = value;
      }
    }

    /// <summary>Field number for the "east" field.</summary>
    public const int EastFieldNumber = 2;
    private double east_;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public double East {
      get { return east_; }
      set {
        east_ = value;
      }
    }

    /// <summary>Field number for the "depth" field.</summary>
    public const int DepthFieldNumber = 3;
    private double depth_;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public double Depth {
      get { return depth_; }
      set {
        depth_ = value;
      }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override bool Equals(object other) {
      return Equals(other as NED);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public bool Equals(NED other) {
      if (ReferenceEquals(other, null)) {
        return false;
      }
      if (ReferenceEquals(other, this)) {
        return true;
      }
      if (!pbc::ProtobufEqualityComparers.BitwiseDoubleEqualityComparer.Equals(North, other.North)) return false;
      if (!pbc::ProtobufEqualityComparers.BitwiseDoubleEqualityComparer.Equals(East, other.East)) return false;
      if (!pbc::ProtobufEqualityComparers.BitwiseDoubleEqualityComparer.Equals(Depth, other.Depth)) return false;
      return Equals(_unknownFields, other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override int GetHashCode() {
      int hash = 1;
      if (North != 0D) hash ^= pbc::ProtobufEqualityComparers.BitwiseDoubleEqualityComparer.GetHashCode(North);
      if (East != 0D) hash ^= pbc::ProtobufEqualityComparers.BitwiseDoubleEqualityComparer.GetHashCode(East);
      if (Depth != 0D) hash ^= pbc::ProtobufEqualityComparers.BitwiseDoubleEqualityComparer.GetHashCode(Depth);
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
      if (North != 0D) {
        output.WriteRawTag(9);
        output.WriteDouble(North);
      }
      if (East != 0D) {
        output.WriteRawTag(17);
        output.WriteDouble(East);
      }
      if (Depth != 0D) {
        output.WriteRawTag(25);
        output.WriteDouble(Depth);
      }
      if (_unknownFields != null) {
        _unknownFields.WriteTo(output);
      }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public int CalculateSize() {
      int size = 0;
      if (North != 0D) {
        size += 1 + 8;
      }
      if (East != 0D) {
        size += 1 + 8;
      }
      if (Depth != 0D) {
        size += 1 + 8;
      }
      if (_unknownFields != null) {
        size += _unknownFields.CalculateSize();
      }
      return size;
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public void MergeFrom(NED other) {
      if (other == null) {
        return;
      }
      if (other.North != 0D) {
        North = other.North;
      }
      if (other.East != 0D) {
        East = other.East;
      }
      if (other.Depth != 0D) {
        Depth = other.Depth;
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
          case 9: {
            North = input.ReadDouble();
            break;
          }
          case 17: {
            East = input.ReadDouble();
            break;
          }
          case 25: {
            Depth = input.ReadDouble();
            break;
          }
        }
      }
    }

  }

  public sealed partial class NavigationStatus : pb::IMessage<NavigationStatus> {
    private static readonly pb::MessageParser<NavigationStatus> _parser = new pb::MessageParser<NavigationStatus>(() => new NavigationStatus());
    private pb::UnknownFieldSet _unknownFields;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public static pb::MessageParser<NavigationStatus> Parser { get { return _parser; } }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public static pbr::MessageDescriptor Descriptor {
      get { return global::Auv.AuvReflection.Descriptor.MessageTypes[1]; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    pbr::MessageDescriptor pb::IMessage.Descriptor {
      get { return Descriptor; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public NavigationStatus() {
      OnConstruction();
    }

    partial void OnConstruction();

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public NavigationStatus(NavigationStatus other) : this() {
      header_ = other.header_ != null ? other.header_.Clone() : null;
      globalPosition_ = other.globalPosition_ != null ? other.globalPosition_.Clone() : null;
      origin_ = other.origin_ != null ? other.origin_.Clone() : null;
      position_ = other.position_ != null ? other.position_.Clone() : null;
      bodyVelocity_ = other.bodyVelocity_ != null ? other.bodyVelocity_.Clone() : null;
      seafloorVelocity_ = other.seafloorVelocity_ != null ? other.seafloorVelocity_.Clone() : null;
      orientation_ = other.orientation_ != null ? other.orientation_.Clone() : null;
      orientationRate_ = other.orientationRate_ != null ? other.orientationRate_.Clone() : null;
      positionVariance_ = other.positionVariance_ != null ? other.positionVariance_.Clone() : null;
      orientationVariance_ = other.orientationVariance_ != null ? other.orientationVariance_.Clone() : null;
      _unknownFields = pb::UnknownFieldSet.Clone(other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public NavigationStatus Clone() {
      return new NavigationStatus(this);
    }

    /// <summary>Field number for the "header" field.</summary>
    public const int HeaderFieldNumber = 1;
    private global::Std.Header header_;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public global::Std.Header Header {
      get { return header_; }
      set {
        header_ = value;
      }
    }

    /// <summary>Field number for the "globalPosition" field.</summary>
    public const int GlobalPositionFieldNumber = 2;
    private global::Geographic.GeoPoint globalPosition_;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public global::Geographic.GeoPoint GlobalPosition {
      get { return globalPosition_; }
      set {
        globalPosition_ = value;
      }
    }

    /// <summary>Field number for the "origin" field.</summary>
    public const int OriginFieldNumber = 3;
    private global::Geographic.GeoPoint origin_;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public global::Geographic.GeoPoint Origin {
      get { return origin_; }
      set {
        origin_ = value;
      }
    }

    /// <summary>Field number for the "position" field.</summary>
    public const int PositionFieldNumber = 4;
    private global::Auv.NED position_;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public global::Auv.NED Position {
      get { return position_; }
      set {
        position_ = value;
      }
    }

    /// <summary>Field number for the "bodyVelocity" field.</summary>
    public const int BodyVelocityFieldNumber = 5;
    private global::Geometry.Vector3 bodyVelocity_;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public global::Geometry.Vector3 BodyVelocity {
      get { return bodyVelocity_; }
      set {
        bodyVelocity_ = value;
      }
    }

    /// <summary>Field number for the "seafloorVelocity" field.</summary>
    public const int SeafloorVelocityFieldNumber = 6;
    private global::Geometry.Vector3 seafloorVelocity_;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public global::Geometry.Vector3 SeafloorVelocity {
      get { return seafloorVelocity_; }
      set {
        seafloorVelocity_ = value;
      }
    }

    /// <summary>Field number for the "orientation" field.</summary>
    public const int OrientationFieldNumber = 7;
    private global::Geometry.Vector3 orientation_;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public global::Geometry.Vector3 Orientation {
      get { return orientation_; }
      set {
        orientation_ = value;
      }
    }

    /// <summary>Field number for the "orientationRate" field.</summary>
    public const int OrientationRateFieldNumber = 8;
    private global::Geometry.Vector3 orientationRate_;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public global::Geometry.Vector3 OrientationRate {
      get { return orientationRate_; }
      set {
        orientationRate_ = value;
      }
    }

    /// <summary>Field number for the "positionVariance" field.</summary>
    public const int PositionVarianceFieldNumber = 9;
    private global::Auv.NED positionVariance_;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public global::Auv.NED PositionVariance {
      get { return positionVariance_; }
      set {
        positionVariance_ = value;
      }
    }

    /// <summary>Field number for the "orientationVariance" field.</summary>
    public const int OrientationVarianceFieldNumber = 10;
    private global::Geometry.Vector3 orientationVariance_;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public global::Geometry.Vector3 OrientationVariance {
      get { return orientationVariance_; }
      set {
        orientationVariance_ = value;
      }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override bool Equals(object other) {
      return Equals(other as NavigationStatus);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public bool Equals(NavigationStatus other) {
      if (ReferenceEquals(other, null)) {
        return false;
      }
      if (ReferenceEquals(other, this)) {
        return true;
      }
      if (!object.Equals(Header, other.Header)) return false;
      if (!object.Equals(GlobalPosition, other.GlobalPosition)) return false;
      if (!object.Equals(Origin, other.Origin)) return false;
      if (!object.Equals(Position, other.Position)) return false;
      if (!object.Equals(BodyVelocity, other.BodyVelocity)) return false;
      if (!object.Equals(SeafloorVelocity, other.SeafloorVelocity)) return false;
      if (!object.Equals(Orientation, other.Orientation)) return false;
      if (!object.Equals(OrientationRate, other.OrientationRate)) return false;
      if (!object.Equals(PositionVariance, other.PositionVariance)) return false;
      if (!object.Equals(OrientationVariance, other.OrientationVariance)) return false;
      return Equals(_unknownFields, other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override int GetHashCode() {
      int hash = 1;
      if (header_ != null) hash ^= Header.GetHashCode();
      if (globalPosition_ != null) hash ^= GlobalPosition.GetHashCode();
      if (origin_ != null) hash ^= Origin.GetHashCode();
      if (position_ != null) hash ^= Position.GetHashCode();
      if (bodyVelocity_ != null) hash ^= BodyVelocity.GetHashCode();
      if (seafloorVelocity_ != null) hash ^= SeafloorVelocity.GetHashCode();
      if (orientation_ != null) hash ^= Orientation.GetHashCode();
      if (orientationRate_ != null) hash ^= OrientationRate.GetHashCode();
      if (positionVariance_ != null) hash ^= PositionVariance.GetHashCode();
      if (orientationVariance_ != null) hash ^= OrientationVariance.GetHashCode();
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
      if (header_ != null) {
        output.WriteRawTag(10);
        output.WriteMessage(Header);
      }
      if (globalPosition_ != null) {
        output.WriteRawTag(18);
        output.WriteMessage(GlobalPosition);
      }
      if (origin_ != null) {
        output.WriteRawTag(26);
        output.WriteMessage(Origin);
      }
      if (position_ != null) {
        output.WriteRawTag(34);
        output.WriteMessage(Position);
      }
      if (bodyVelocity_ != null) {
        output.WriteRawTag(42);
        output.WriteMessage(BodyVelocity);
      }
      if (seafloorVelocity_ != null) {
        output.WriteRawTag(50);
        output.WriteMessage(SeafloorVelocity);
      }
      if (orientation_ != null) {
        output.WriteRawTag(58);
        output.WriteMessage(Orientation);
      }
      if (orientationRate_ != null) {
        output.WriteRawTag(66);
        output.WriteMessage(OrientationRate);
      }
      if (positionVariance_ != null) {
        output.WriteRawTag(74);
        output.WriteMessage(PositionVariance);
      }
      if (orientationVariance_ != null) {
        output.WriteRawTag(82);
        output.WriteMessage(OrientationVariance);
      }
      if (_unknownFields != null) {
        _unknownFields.WriteTo(output);
      }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public int CalculateSize() {
      int size = 0;
      if (header_ != null) {
        size += 1 + pb::CodedOutputStream.ComputeMessageSize(Header);
      }
      if (globalPosition_ != null) {
        size += 1 + pb::CodedOutputStream.ComputeMessageSize(GlobalPosition);
      }
      if (origin_ != null) {
        size += 1 + pb::CodedOutputStream.ComputeMessageSize(Origin);
      }
      if (position_ != null) {
        size += 1 + pb::CodedOutputStream.ComputeMessageSize(Position);
      }
      if (bodyVelocity_ != null) {
        size += 1 + pb::CodedOutputStream.ComputeMessageSize(BodyVelocity);
      }
      if (seafloorVelocity_ != null) {
        size += 1 + pb::CodedOutputStream.ComputeMessageSize(SeafloorVelocity);
      }
      if (orientation_ != null) {
        size += 1 + pb::CodedOutputStream.ComputeMessageSize(Orientation);
      }
      if (orientationRate_ != null) {
        size += 1 + pb::CodedOutputStream.ComputeMessageSize(OrientationRate);
      }
      if (positionVariance_ != null) {
        size += 1 + pb::CodedOutputStream.ComputeMessageSize(PositionVariance);
      }
      if (orientationVariance_ != null) {
        size += 1 + pb::CodedOutputStream.ComputeMessageSize(OrientationVariance);
      }
      if (_unknownFields != null) {
        size += _unknownFields.CalculateSize();
      }
      return size;
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public void MergeFrom(NavigationStatus other) {
      if (other == null) {
        return;
      }
      if (other.header_ != null) {
        if (header_ == null) {
          header_ = new global::Std.Header();
        }
        Header.MergeFrom(other.Header);
      }
      if (other.globalPosition_ != null) {
        if (globalPosition_ == null) {
          globalPosition_ = new global::Geographic.GeoPoint();
        }
        GlobalPosition.MergeFrom(other.GlobalPosition);
      }
      if (other.origin_ != null) {
        if (origin_ == null) {
          origin_ = new global::Geographic.GeoPoint();
        }
        Origin.MergeFrom(other.Origin);
      }
      if (other.position_ != null) {
        if (position_ == null) {
          position_ = new global::Auv.NED();
        }
        Position.MergeFrom(other.Position);
      }
      if (other.bodyVelocity_ != null) {
        if (bodyVelocity_ == null) {
          bodyVelocity_ = new global::Geometry.Vector3();
        }
        BodyVelocity.MergeFrom(other.BodyVelocity);
      }
      if (other.seafloorVelocity_ != null) {
        if (seafloorVelocity_ == null) {
          seafloorVelocity_ = new global::Geometry.Vector3();
        }
        SeafloorVelocity.MergeFrom(other.SeafloorVelocity);
      }
      if (other.orientation_ != null) {
        if (orientation_ == null) {
          orientation_ = new global::Geometry.Vector3();
        }
        Orientation.MergeFrom(other.Orientation);
      }
      if (other.orientationRate_ != null) {
        if (orientationRate_ == null) {
          orientationRate_ = new global::Geometry.Vector3();
        }
        OrientationRate.MergeFrom(other.OrientationRate);
      }
      if (other.positionVariance_ != null) {
        if (positionVariance_ == null) {
          positionVariance_ = new global::Auv.NED();
        }
        PositionVariance.MergeFrom(other.PositionVariance);
      }
      if (other.orientationVariance_ != null) {
        if (orientationVariance_ == null) {
          orientationVariance_ = new global::Geometry.Vector3();
        }
        OrientationVariance.MergeFrom(other.OrientationVariance);
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
            if (header_ == null) {
              header_ = new global::Std.Header();
            }
            input.ReadMessage(header_);
            break;
          }
          case 18: {
            if (globalPosition_ == null) {
              globalPosition_ = new global::Geographic.GeoPoint();
            }
            input.ReadMessage(globalPosition_);
            break;
          }
          case 26: {
            if (origin_ == null) {
              origin_ = new global::Geographic.GeoPoint();
            }
            input.ReadMessage(origin_);
            break;
          }
          case 34: {
            if (position_ == null) {
              position_ = new global::Auv.NED();
            }
            input.ReadMessage(position_);
            break;
          }
          case 42: {
            if (bodyVelocity_ == null) {
              bodyVelocity_ = new global::Geometry.Vector3();
            }
            input.ReadMessage(bodyVelocity_);
            break;
          }
          case 50: {
            if (seafloorVelocity_ == null) {
              seafloorVelocity_ = new global::Geometry.Vector3();
            }
            input.ReadMessage(seafloorVelocity_);
            break;
          }
          case 58: {
            if (orientation_ == null) {
              orientation_ = new global::Geometry.Vector3();
            }
            input.ReadMessage(orientation_);
            break;
          }
          case 66: {
            if (orientationRate_ == null) {
              orientationRate_ = new global::Geometry.Vector3();
            }
            input.ReadMessage(orientationRate_);
            break;
          }
          case 74: {
            if (positionVariance_ == null) {
              positionVariance_ = new global::Auv.NED();
            }
            input.ReadMessage(positionVariance_);
            break;
          }
          case 82: {
            if (orientationVariance_ == null) {
              orientationVariance_ = new global::Geometry.Vector3();
            }
            input.ReadMessage(orientationVariance_);
            break;
          }
        }
      }
    }

  }

  #endregion

}

#endregion Designer generated code