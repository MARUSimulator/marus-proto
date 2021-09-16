# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import sensor_streaming_pb2 as sensor__streaming__pb2


class SensorStreamingStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.StreamCameraSensor = channel.stream_unary(
        '/sensorstreaming.SensorStreaming/StreamCameraSensor',
        request_serializer=sensor__streaming__pb2.CameraStreamingRequest.SerializeToString,
        response_deserializer=sensor__streaming__pb2.StreamingResponse.FromString,
        )
    self.StreamLidarSensor = channel.stream_unary(
        '/sensorstreaming.SensorStreaming/StreamLidarSensor',
        request_serializer=sensor__streaming__pb2.LidarStreamingRequest.SerializeToString,
        response_deserializer=sensor__streaming__pb2.StreamingResponse.FromString,
        )
    self.StreamRadarSensor = channel.stream_unary(
        '/sensorstreaming.SensorStreaming/StreamRadarSensor',
        request_serializer=sensor__streaming__pb2.RadarStreamingRequest.SerializeToString,
        response_deserializer=sensor__streaming__pb2.StreamingResponse.FromString,
        )
    self.StreamDepthSensor = channel.stream_unary(
        '/sensorstreaming.SensorStreaming/StreamDepthSensor',
        request_serializer=sensor__streaming__pb2.DepthStreamingRequest.SerializeToString,
        response_deserializer=sensor__streaming__pb2.StreamingResponse.FromString,
        )
    self.StreamDvlSensor = channel.stream_unary(
        '/sensorstreaming.SensorStreaming/StreamDvlSensor',
        request_serializer=sensor__streaming__pb2.DvlStreamingRequest.SerializeToString,
        response_deserializer=sensor__streaming__pb2.StreamingResponse.FromString,
        )
    self.StreamGnssSensor = channel.stream_unary(
        '/sensorstreaming.SensorStreaming/StreamGnssSensor',
        request_serializer=sensor__streaming__pb2.GnssStreamingRequest.SerializeToString,
        response_deserializer=sensor__streaming__pb2.StreamingResponse.FromString,
        )
    self.StreamImuSensor = channel.stream_unary(
        '/sensorstreaming.SensorStreaming/StreamImuSensor',
        request_serializer=sensor__streaming__pb2.ImuStreamingRequest.SerializeToString,
        response_deserializer=sensor__streaming__pb2.StreamingResponse.FromString,
        )
    self.StreamPoseSensor = channel.stream_unary(
        '/sensorstreaming.SensorStreaming/StreamPoseSensor',
        request_serializer=sensor__streaming__pb2.PoseStreamingRequest.SerializeToString,
        response_deserializer=sensor__streaming__pb2.StreamingResponse.FromString,
        )
    self.StreamSonarSensor = channel.stream_unary(
        '/sensorstreaming.SensorStreaming/StreamSonarSensor',
        request_serializer=sensor__streaming__pb2.SonarStreamingRequest.SerializeToString,
        response_deserializer=sensor__streaming__pb2.StreamingResponse.FromString,
        )
    self.StreamAisSensor = channel.stream_unary(
        '/sensorstreaming.SensorStreaming/StreamAisSensor',
        request_serializer=sensor__streaming__pb2.AISStreamingRequest.SerializeToString,
        response_deserializer=sensor__streaming__pb2.StreamingResponse.FromString,
        )


class SensorStreamingServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def StreamCameraSensor(self, request_iterator, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def StreamLidarSensor(self, request_iterator, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def StreamRadarSensor(self, request_iterator, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def StreamDepthSensor(self, request_iterator, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def StreamDvlSensor(self, request_iterator, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def StreamGnssSensor(self, request_iterator, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def StreamImuSensor(self, request_iterator, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def StreamPoseSensor(self, request_iterator, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def StreamSonarSensor(self, request_iterator, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def StreamAisSensor(self, request_iterator, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_SensorStreamingServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'StreamCameraSensor': grpc.stream_unary_rpc_method_handler(
          servicer.StreamCameraSensor,
          request_deserializer=sensor__streaming__pb2.CameraStreamingRequest.FromString,
          response_serializer=sensor__streaming__pb2.StreamingResponse.SerializeToString,
      ),
      'StreamLidarSensor': grpc.stream_unary_rpc_method_handler(
          servicer.StreamLidarSensor,
          request_deserializer=sensor__streaming__pb2.LidarStreamingRequest.FromString,
          response_serializer=sensor__streaming__pb2.StreamingResponse.SerializeToString,
      ),
      'StreamRadarSensor': grpc.stream_unary_rpc_method_handler(
          servicer.StreamRadarSensor,
          request_deserializer=sensor__streaming__pb2.RadarStreamingRequest.FromString,
          response_serializer=sensor__streaming__pb2.StreamingResponse.SerializeToString,
      ),
      'StreamDepthSensor': grpc.stream_unary_rpc_method_handler(
          servicer.StreamDepthSensor,
          request_deserializer=sensor__streaming__pb2.DepthStreamingRequest.FromString,
          response_serializer=sensor__streaming__pb2.StreamingResponse.SerializeToString,
      ),
      'StreamDvlSensor': grpc.stream_unary_rpc_method_handler(
          servicer.StreamDvlSensor,
          request_deserializer=sensor__streaming__pb2.DvlStreamingRequest.FromString,
          response_serializer=sensor__streaming__pb2.StreamingResponse.SerializeToString,
      ),
      'StreamGnssSensor': grpc.stream_unary_rpc_method_handler(
          servicer.StreamGnssSensor,
          request_deserializer=sensor__streaming__pb2.GnssStreamingRequest.FromString,
          response_serializer=sensor__streaming__pb2.StreamingResponse.SerializeToString,
      ),
      'StreamImuSensor': grpc.stream_unary_rpc_method_handler(
          servicer.StreamImuSensor,
          request_deserializer=sensor__streaming__pb2.ImuStreamingRequest.FromString,
          response_serializer=sensor__streaming__pb2.StreamingResponse.SerializeToString,
      ),
      'StreamPoseSensor': grpc.stream_unary_rpc_method_handler(
          servicer.StreamPoseSensor,
          request_deserializer=sensor__streaming__pb2.PoseStreamingRequest.FromString,
          response_serializer=sensor__streaming__pb2.StreamingResponse.SerializeToString,
      ),
      'StreamSonarSensor': grpc.stream_unary_rpc_method_handler(
          servicer.StreamSonarSensor,
          request_deserializer=sensor__streaming__pb2.SonarStreamingRequest.FromString,
          response_serializer=sensor__streaming__pb2.StreamingResponse.SerializeToString,
      ),
      'StreamAisSensor': grpc.stream_unary_rpc_method_handler(
          servicer.StreamAisSensor,
          request_deserializer=sensor__streaming__pb2.AISStreamingRequest.FromString,
          response_serializer=sensor__streaming__pb2.StreamingResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'sensorstreaming.SensorStreaming', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))