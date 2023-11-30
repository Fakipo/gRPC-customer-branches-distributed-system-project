import grpc
import example_pb2_grpc
import example_pb2


class Branch(example_pb2_grpc.BranchServicer):
    def __init__(self, id, balance, branches):
        self.id = id
        self.balance = balance
        self.branches = branches
        self.stubList = list()
        self.recvMsg = list()

    # Setup gRPC channel & client stub for each branch
    def createStubs(self):
        self.stubList = [
            example_pb2_grpc.BranchStub(grpc.insecure_channel(f"localhost:{60000 + branchId}"))
            for branchId in self.branches if branchId != self.id
        ]

    def extendedMsgForProp(self, request, propagate):
        # print(request.branchId)
        result = "success"
        if request.money < 0:
            result = "fail"
        elif request.interface == "query":
            return example_pb2.MsgResponse(interface=request.interface, money=self.balance)
        elif request.interface == "deposit":
            self.balance += request.money
            if propagate == True:
                self.Propagate_Deposit(request)
        elif request.interface == "withdraw":
            if self.balance >= request.money:
                self.balance -= request.money
                if propagate == True:
                    self.Propagate_Withdraw(request)
            else:
                result = "fail"
        else:
            result = "fail"

        msg = {"interface": request.interface, "result": result, "branchId" : request.branchId}

        if request.interface != "query":
            msg["result"] = result
        else:
            msg["money"] = request.money
        self.recvMsg.append(msg)
        return example_pb2.MsgResponse(interface=request.interface, result=result, money=self.balance, branchId = request.branchId)

    def Propagate_Withdraw(self, request):
        for stub in self.stubList:
            stub.MsgPropagation(example_pb2.MsgRequest(id=request.id, interface="withdraw", branchId = request.branchId, money=request.money))

    def Propagate_Deposit(self, request):
        for stub in self.stubList:
            stub.MsgPropagation(example_pb2.MsgRequest(id=request.id, interface="deposit", branchId = request.branchId, money=request.money))

    def MsgDelivery(self, request, context):
        return self.extendedMsgForProp(request, True)

    def MsgPropagation(self, request, context):
        return self.extendedMsgForProp(request, False)
