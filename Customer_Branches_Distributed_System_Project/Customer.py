import grpc
import example_pb2_grpc
import example_pb2


class Customer:
    def __init__(self, id, events):
        self.id = id
        self.events = events
        self.recvMsg = list()
        self.stub = None

    # Setup gRPC channel & client stub for branch
    def createStub(self):
        port = str(60000 + self.id)
        channel = grpc.insecure_channel("localhost:" + port)
        self.stub = example_pb2_grpc.BranchStub(channel)

    # Send gRPC request for each event
    def executeEvents(self):
        for event in self.events:
            if event["interface"] != "query":
                response = self.stub.MsgDelivery(
                    example_pb2.MsgRequest(id=event["id"], interface=event["interface"], money=event["money"])
                )
            else:
                response = self.stub.MsgDelivery(
                    example_pb2.MsgRequest(id=event["id"], interface=event["interface"])
                )
            if response.interface != "query":
                stringToAppend = {"interface": response.interface, "result": response.result}
            else:
                stringToAppend = {"interface": response.interface,  "balance": response.money}
            self.recvMsg.append(stringToAppend)

    def output(self):
        return {"id": self.id, "recv": self.recvMsg}
