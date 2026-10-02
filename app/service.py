from time import perf_counter
class Service:
    def run(self,value):
        t=perf_counter(); output=value.upper(); latency=round((perf_counter()-t)*1000,3)
        return {"input":value,"output":output,"latency_ms":latency,"tokens_in":len(value.split()),"tokens_out":len(output.split()),"estimated_cost":0.00001}