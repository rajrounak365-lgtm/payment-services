from fastapi import APIRouter

router = APIRouter()

@router.get("/payments")
def get_payments():
    return {
        "payments": [
            {"id": 1, "amount": 499},
            {"id": 2, "amount": 799}
        ]
    }
