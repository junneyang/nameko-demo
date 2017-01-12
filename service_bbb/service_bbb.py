from nameko.rpc import rpc, RpcProxy
from nameko.standalone.rpc import ClusterRpcProxy
# config = {'AMQP_URI': 'pyamqp://guest:guest@10.20.0.112'}
import time
from nameko.events import EventDispatcher, event_handler
from nameko.events import BROADCAST, event_handler

class ServiceBBB:
    name = "service_bbb"

    #dispatch = EventDispatcher()

    # we depend on the RPC interface of "another_service"
    # other_rpc = RpcProxy("another_service")
    service_aaa = RpcProxy("service_aaa")
    # cluster_rpc = ClusterRpcProxy(config)

    @rpc  # `method` is exposed over RPC
    def method_b1(self, name, age):
        # application logic goes here
        #pass
        print("sleep 10")
        time.sleep(10)
        return {"name":name, "age":age, "method":"method_b1", "aaa":self.service_aaa.method_a1("AAA", 123)}
        # RpcTimeout: 3
        # with ClusterRpcProxy(config, timeout=3) as cluster_rpc:
            # return cluster_rpc.service_aaa.method_a1("BBB", 321)
    @rpc  # `method` is exposed over RPC
    def method_b2(self, params):
        # application logic goes here
        #pass
        return params['name'], params['age'], "method_b2"
    #@rpc
    #def dispatching_method(self, payload):
    #    self.dispatch("event_type001", payload)

    @event_handler("service_ccc", "event_type", handler_type=BROADCAST, reliable_delivery=False)
    def handle_event(self, payload):
        print("service_bbb received:", payload)
