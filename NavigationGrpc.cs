// <auto-generated>
//     Generated by the protocol buffer compiler.  DO NOT EDIT!
//     source: navigation.proto
// </auto-generated>
#pragma warning disable 0414, 1591
#region Designer generated code

using grpc = global::Grpc.Core;

namespace Navigation {
  public static partial class Navigation
  {
    static readonly string __ServiceName = "navigation.Navigation";

    static readonly grpc::Marshaller<global::Navigation.NavigationRequest> __Marshaller_navigation_NavigationRequest = grpc::Marshallers.Create((arg) => global::Google.Protobuf.MessageExtensions.ToByteArray(arg), global::Navigation.NavigationRequest.Parser.ParseFrom);
    static readonly grpc::Marshaller<global::Navigation.NavigationResponse> __Marshaller_navigation_NavigationResponse = grpc::Marshallers.Create((arg) => global::Google.Protobuf.MessageExtensions.ToByteArray(arg), global::Navigation.NavigationResponse.Parser.ParseFrom);

    static readonly grpc::Method<global::Navigation.NavigationRequest, global::Navigation.NavigationResponse> __Method_SendNavigationMessage = new grpc::Method<global::Navigation.NavigationRequest, global::Navigation.NavigationResponse>(
        grpc::MethodType.Unary,
        __ServiceName,
        "SendNavigationMessage",
        __Marshaller_navigation_NavigationRequest,
        __Marshaller_navigation_NavigationResponse);

    /// <summary>Service descriptor</summary>
    public static global::Google.Protobuf.Reflection.ServiceDescriptor Descriptor
    {
      get { return global::Navigation.NavigationReflection.Descriptor.Services[0]; }
    }

    /// <summary>Base class for server-side implementations of Navigation</summary>
    public abstract partial class NavigationBase
    {
      public virtual global::System.Threading.Tasks.Task<global::Navigation.NavigationResponse> SendNavigationMessage(global::Navigation.NavigationRequest request, grpc::ServerCallContext context)
      {
        throw new grpc::RpcException(new grpc::Status(grpc::StatusCode.Unimplemented, ""));
      }

    }

    /// <summary>Client for Navigation</summary>
    public partial class NavigationClient : grpc::ClientBase<NavigationClient>
    {
      /// <summary>Creates a new client for Navigation</summary>
      /// <param name="channel">The channel to use to make remote calls.</param>
      public NavigationClient(grpc::Channel channel) : base(channel)
      {
      }
      /// <summary>Creates a new client for Navigation that uses a custom <c>CallInvoker</c>.</summary>
      /// <param name="callInvoker">The callInvoker to use to make remote calls.</param>
      public NavigationClient(grpc::CallInvoker callInvoker) : base(callInvoker)
      {
      }
      /// <summary>Protected parameterless constructor to allow creation of test doubles.</summary>
      protected NavigationClient() : base()
      {
      }
      /// <summary>Protected constructor to allow creation of configured clients.</summary>
      /// <param name="configuration">The client configuration.</param>
      protected NavigationClient(ClientBaseConfiguration configuration) : base(configuration)
      {
      }

      public virtual global::Navigation.NavigationResponse SendNavigationMessage(global::Navigation.NavigationRequest request, grpc::Metadata headers = null, global::System.DateTime? deadline = null, global::System.Threading.CancellationToken cancellationToken = default(global::System.Threading.CancellationToken))
      {
        return SendNavigationMessage(request, new grpc::CallOptions(headers, deadline, cancellationToken));
      }
      public virtual global::Navigation.NavigationResponse SendNavigationMessage(global::Navigation.NavigationRequest request, grpc::CallOptions options)
      {
        return CallInvoker.BlockingUnaryCall(__Method_SendNavigationMessage, null, options, request);
      }
      public virtual grpc::AsyncUnaryCall<global::Navigation.NavigationResponse> SendNavigationMessageAsync(global::Navigation.NavigationRequest request, grpc::Metadata headers = null, global::System.DateTime? deadline = null, global::System.Threading.CancellationToken cancellationToken = default(global::System.Threading.CancellationToken))
      {
        return SendNavigationMessageAsync(request, new grpc::CallOptions(headers, deadline, cancellationToken));
      }
      public virtual grpc::AsyncUnaryCall<global::Navigation.NavigationResponse> SendNavigationMessageAsync(global::Navigation.NavigationRequest request, grpc::CallOptions options)
      {
        return CallInvoker.AsyncUnaryCall(__Method_SendNavigationMessage, null, options, request);
      }
      /// <summary>Creates a new instance of client from given <c>ClientBaseConfiguration</c>.</summary>
      protected override NavigationClient NewInstance(ClientBaseConfiguration configuration)
      {
        return new NavigationClient(configuration);
      }
    }

    /// <summary>Creates service definition that can be registered with a server</summary>
    /// <param name="serviceImpl">An object implementing the server-side handling logic.</param>
    public static grpc::ServerServiceDefinition BindService(NavigationBase serviceImpl)
    {
      return grpc::ServerServiceDefinition.CreateBuilder()
          .AddMethod(__Method_SendNavigationMessage, serviceImpl.SendNavigationMessage).Build();
    }

  }
}
#endregion
