from datetime import datetime
from typing import List
from uuid import uuid4, UUID
from dataclasses import dataclass, field


@dataclass
class Task:
    id: UUID = field(default_factory=uuid4)
    title: str = field(default='')
    descriptions: List[str] = field(default_factory=list)
    start_datetime: datetime = field(default_factory=datetime.now)
    end_datetime: datetime = field(default=None)
    sub_tasks: List['Task'] = field(default_factory=list)
