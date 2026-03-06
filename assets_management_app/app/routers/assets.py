import uuid
from datetime import datetime, timezone

from fastapi import APIRouter

from app.models import Asset, AssetCreate
from app.store import get_store

router = APIRouter(prefix="/assets", tags=["assets"])


@router.get("", response_model=list[Asset])
def list_assets():
    return list(get_store().values())


@router.post("", response_model=Asset, status_code=201)
def add_asset(payload: AssetCreate):
    now = datetime.now(timezone.utc)
    asset = Asset(
        id=str(uuid.uuid4()),
        created_at=now,
        updated_at=now,
        **payload.model_dump(),
    )
    get_store()[asset.id] = asset
    return asset
