from pydantic import BaseModel
from typing import Optional

class Source(BaseModel):
    title: str
    excerpt: Optional[str] = None
    url: Optional[str] = None