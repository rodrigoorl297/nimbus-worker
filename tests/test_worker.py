from worker.handlers import handle_logistics
from worker.queue import Job, Worker


def test_retry_and_dead_letter():
    worker = Worker(max_attempts=2)
    worker.run([
        Job("ok", {"id": "1"}),
        Job("nope", {"fail": True}),
    ], handle_logistics)
    assert worker.processed == ["ok"]
    assert worker.dead_letter[0].name == "nope"
    assert worker.dead_letter[0].attempts == 2
