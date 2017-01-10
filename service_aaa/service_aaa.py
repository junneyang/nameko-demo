from nameko.rpc import rpc, RpcProxy
from nameko.events import EventDispatcher, event_handler
from nameko.events import BROADCAST, event_handler

class ServiceAAA:
    name = "service_aaa"

    # we depend on the RPC interface of "another_service"
    # other_rpc = RpcProxy("another_service")

    @rpc  # `method` is exposed over RPC
    def method_a1(self, name, age):
        # application logic goes here
        #pass
        return {"name":name, "age":age, "method":"method_a1"}
    @rpc  # `method` is exposed over RPC
    def method_a2(self, params):
        # application logic goes here
        #pass
        return params['name'], params['age'], "method_a2"
    @event_handler("service_ccc", "event_type", handler_type=BROADCAST, reliable_delivery=False)
    def handle_event(self, payload):
        print("service_aaa received:", payload)
