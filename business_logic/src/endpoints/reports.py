from fastapi import APIRouter, Query, Security, status
from fastapi.security import APIKeyHeader
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
import requests
from datetime import datetime

from settings import DB_SERVER_URL, RPI_SERVER_URL
from src.utils.base_utils import raise_exception
from src.utils.report_utils import get_sensors_values

router = APIRouter()


@router.get("/realTimeValues",
            tags=["Reports"])
async def get_real_time_values(authorization=Security(APIKeyHeader(name="Authorization", auto_error=False))):
    try:
        response_db = requests.get(
            f"{DB_SERVER_URL}/devices",
            headers={"Authorization": authorization}
        )
        response_rpi = requests.get(
            f"{RPI_SERVER_URL}/sensors",
            headers={"Authorization": authorization}
        )
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=jsonable_encoder(
                get_sensors_values((response_rpi.json())['data'], (response_db.json())['data'])
            )
        )
    except Exception as e:
        raise_exception(e)


@router.get("/alerts",
            tags=["Reports"])
async def get_alerts(device_id: int = Query(None),
                     alert_date: datetime = Query(None),
                     authorization=Security(APIKeyHeader(name="Authorization", auto_error=False))):
    try:
        response = requests.get(
            f"{DB_SERVER_URL}/alerts",
            headers={"Authorization": authorization},
            params={
                'device_id': device_id,
                'alert_date': alert_date
            }
        )
        return JSONResponse(
            status_code=response.status_code,
            content=response.json()
        )
    except Exception as e:
        raise_exception(e)


@router.get("/reports",
            tags=["Reports"])
async def get_alerts(device_id: int = Query(None),
                     report_date: datetime = Query(None),
                     authorization=Security(APIKeyHeader(name="Authorization", auto_error=False))):
    try:
        response = requests.get(
            f"{DB_SERVER_URL}/reports",
            headers={"Authorization": authorization},
            params={
                'device_id': device_id,
                'report_date': report_date
            }
        )
        return JSONResponse(
            status_code=response.status_code,
            content=response.json()
        )
    except Exception as e:
        raise_exception(e)
