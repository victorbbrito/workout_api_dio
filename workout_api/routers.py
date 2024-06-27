from fastapi import APIRouter

from workout_api.athlete.controller import router as athlete_router
from workout_api.categories.controller import router as categories_router
from workout_api.training_center.controller import router as training_center_router

api_router = APIRouter()
api_router.include_router(athlete_router, prefix='/athlete', tags=['athlete'])
api_router.include_router(categories_router, prefix='/categories', tags=['categories'])
api_router.include_router(training_center_router, prefix='/training_center', tags=['training_center'])

