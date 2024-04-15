class Worker:
    def __init__(self, worker_id, position, compensation):
        self.worker_id = worker_id
        self.position = position
        self.compensation = int(compensation)
        self.in_office = False
        self.last_entry = None
        self.total_time = 0
        self.pending_promotion = None

    def register_time(self, timestamp):
        timestamp = int(timestamp)
        if not self.in_office:
            self.in_office = True
            self.last_entry = timestamp
            # Check if there's a pending promotion and if the promotion starts now or later
            if self.pending_promotion and timestamp >= self.pending_promotion['timestamp']:
                self.position = self.pending_promotion['position']
                self.compensation = self.pending_promotion['compensation']
                self.pending_promotion = None
        else:
            self.in_office = False
            self.total_time += timestamp - self.last_entry

    def get_total_time(self):
        return self.total_time

    def promote(self, new_position, new_compensation, start_timestamp):
        if not self.pending_promotion:
            self.pending_promotion = {
                'position': new_position,
                'compensation': int(new_compensation),
                'timestamp': int(start_timestamp)
            }
            return "success"
        return "invalid_request"

def solution(queries):
    workers = {}
    positions = {}
    output = []

    for query in queries:
        op = query[0]

        if op == "ADD_WORKER":
            id_ = query[1]
            if id_ not in workers:
                workers[id_] = Worker(id_, query[2], query[3])
                pos = query[2].lower()
                if pos not in positions:
                    positions[pos] = []
                positions[pos].append(workers[id_])
                output.append("true")
            else:
                output.append("false")

        elif op == "REGISTER":
            id_ = query[1]
            if id_ in workers:
                workers[id_].register_time(query[2])
                output.append("registered")
            else:
                output.append("invalid_request")

        elif op == "TOP_N_WORKERS":
            n = int(query[1])
            pos = query[2].lower()
            if pos in positions:
                sorted_workers = sorted(positions[pos], key=lambda x: (-x.get_total_time(), x.worker_id))
                res = []
                for i in range(min(n, len(sorted_workers))):
                    worker = sorted_workers[i]
                    res.append(f"{worker.worker_id} ({worker.get_total_time()})")
                output.append(", ".join(res))
            else:
                output.append("")

        elif op == "PROMOTE":
            id_ = query[1]
            if id_ in workers:
                res = workers[id_].promote(query[2], query[3], query[4])
                output.append(res)
            else:
                output.append("invalid_request")

    return output

queries = [
    ["ADD_WORKER","John","Junior Developer","100"], 
    ["ADD_WORKER","John","Junior Developer","150"], 
    ["ADD_WORKER","Ashley","Junior Developer","100"], 
    ["PROMOTE","John","Middle Developer","250","10"], 
    ["PROMOTE","John","Middle Developer","200","15"], 
    ["PROMOTE","Bob","Middle Developer","200","15"], 
    ["PROMOTE","Ashley","Middle Developer","250","5"]
]

print(solution(queries))
