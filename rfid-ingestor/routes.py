from fastapi import Request, APIRouter


router = APIRouter(prefix='/rfid/')


@router.get('/info/{rfid_tag_id}/')
async def get_rfid_info(request: Request, rfid_tag_id: str):
    pass


@router.post('/register/{rfid_tag_id}/')
async def register_rfid_tag(request: Request, rfid_tag_id: str):
    pass
