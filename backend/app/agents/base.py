from typing import Protocol, Any, Dict

class Agent(Protocol):
    name: str
    async def handle(self, payload: Dict[str, Any]) -> Dict[str, Any]: ...
