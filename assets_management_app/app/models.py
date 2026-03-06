from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class OsInfo(BaseModel):
    name: str
    version: str


class AssetCreate(BaseModel):
    name: str
    asset_type: str
    description: str = ""
    os_info: Optional[OsInfo] = None


class Asset(AssetCreate):
    id: str
    created_at: datetime
    updated_at: datetime
