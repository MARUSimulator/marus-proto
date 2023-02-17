# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import bellhop_pb2 as bellhop__pb2


class BellhopStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.BellhopSim = channel.unary_unary(
                '/service.Bellhop/BellhopSim',
                request_serializer=bellhop__pb2.BellhopMsg.SerializeToString,
                response_deserializer=bellhop__pb2.BellhopRes.FromString,
                )


class BellhopServicer(object):
    """Missing associated documentation comment in .proto file."""

    def BellhopSim(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_BellhopServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'BellhopSim': grpc.unary_unary_rpc_method_handler(
                    servicer.BellhopSim,
                    request_deserializer=bellhop__pb2.BellhopMsg.FromString,
                    response_serializer=bellhop__pb2.BellhopRes.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'service.Bellhop', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Bellhop(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def BellhopSim(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/service.Bellhop/BellhopSim',
            bellhop__pb2.BellhopMsg.SerializeToString,
            bellhop__pb2.BellhopRes.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)