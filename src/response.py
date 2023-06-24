from inc import *
import dataclasses

@dataclasses.dataclass
class Response:
    status: int
    log: str
    ext: list

    def as_json(self):
        return jsonify(
            dataclasses.asdict(self)
        )

