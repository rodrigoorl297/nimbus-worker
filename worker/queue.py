from __future__ import annotations

from dataclasses import dataclass, field
from typing import Callable


@dataclass
class Job:
    name: str
    payload: dict
    attempts: int = 0


@dataclass
class Worker:
    max_attempts: int = 3
    processed: list[str] = field(default_factory=list)
    dead_letter: list[Job] = field(default_factory=list)

    def run(self, jobs: list[Job], handler: Callable[[Job], None]) -> None:
        for job in jobs:
            while job.attempts < self.max_attempts:
                job.attempts += 1
                try:
                    handler(job)
                    self.processed.append(job.name)
                    break
                except Exception:
                    if job.attempts >= self.max_attempts:
                        self.dead_letter.append(job)
