from nameko.rpc import rpc, RpcProxy
from nameko.standalone.rpc import ClusterRpcProxy
from nameko.events import EventDispatcher, event_handler

class ServiceCCC:
    name = "service_ccc"
    dispatch = EventDispatcher()
    
    @rpc
    def dispatching_method(self, payload):
        self.dispatch("event_type", payload)

