import json
from worker.handlers import handle_logistics
from worker.queue import Job, Worker


def main() -> None:
    jobs = [
        Job("ok-1", {"id": "a"}),
        Job("ok-2", {"id": "b"}),
        Job("bad", {"fail": True}),
    ]
    worker = Worker()
    worker.run(jobs, handle_logistics)
    print(json.dumps({
        "processed": worker.processed,
        "dead_letter": [job.name for job in worker.dead_letter],
        "domain": "logistica / tracking",
    }, indent=2))


if __name__ == "__main__":
    main()
