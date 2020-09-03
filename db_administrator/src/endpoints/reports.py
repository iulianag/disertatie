from fastapi import APIRouter, Depends, status, Query
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from datetime import datetime

from src.dependencies.user_permission import have_permission
from src.db_data_management.alerts_management import AlertsTableManager
from src.db_data_management.daily_reports_management import DailyReportsTableManager
from src.utils.reports_utils import (get_alert_list, get_daily_report_list)
from src.utils.base_utils import raise_exception
from src.validation_models.report_model import AlertModel
from src.validation_models.base_validation_model import BaseResponseModel, InfoModel

router = APIRouter()


@router.get("/alerts",
            tags=["Alerts"],
            dependencies=[Depends(have_permission)])
async def get_alerts(device_id: int = Query(None),
                     alert_date: datetime = Query(None)):
    try:
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=jsonable_encoder(
                get_alert_list(await AlertsTableManager.read_alerts(device_id, alert_date))
            )
        )
    except Exception as e:
        raise_exception(e)


@router.post("/alerts",
             tags=["Alerts"])
async def post_alert(item: AlertModel):
    try:
        item.alert_date = datetime.utcnow()
        await AlertsTableManager.create_alert(item)
        return JSONResponse(
            status_code=status.HTTP_201_CREATED,
            content=jsonable_encoder(
                BaseResponseModel(info=[InfoModel(type='success', message='Alert added')])
            )
        )
    except Exception as e:
        raise_exception(e)


@router.get("/reports",
            tags=["Reports"],
            dependencies=[Depends(have_permission)])
async def get_reports(device_id: int = Query(None),
                      report_date: datetime = Query(None)):
    try:
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=jsonable_encoder(
                get_daily_report_list(await DailyReportsTableManager.read_reports(device_id, report_date))
            )
        )
    except Exception as e:
        raise_exception(e)
