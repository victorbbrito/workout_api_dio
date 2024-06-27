from uuid import uuid4

from fastapi import APIRouter, HTTPException

from fastapi import Body

from fastapi import status

from pydantic import UUID4
from sqlalchemy.future import select

from workout_api.athlete.schemas import AthleteIn, AthleteUpdate

from workout_api.athlete.schemas import AthleteOut

from workout_api.athlete.models import AthleteModel

from workout_api.categories.models import CategoriesModel

from workout_api.contrib.dependencies import DatabaseDependency

from datetime import datetime, UTC

from workout_api.training_center.models import TrainingCenterModel

router = APIRouter()

@router.post('/',summary='Create new athlete',status_code=status.HTTP_201_CREATED, response_model= AthleteOut)
async def post(db_session: DatabaseDependency, athlete_in: AthleteIn = Body(...)) -> AthleteOut:
    category = (await db_session.execute(select(CategoriesModel).filter_by(name=athlete_in.category.name))).scalars().first()
    
    if not category:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=f"This category {athlete_in.category.name} was not found")
    
    training_center = (await db_session.execute(select(TrainingCenterModel).filter_by(name=athlete_in.training_center.name))).scalars().first()
    
    if not training_center:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=f"This training center {athlete_in.training_center.name} was not found")
    try:
        athlete_out = AthleteOut(id=uuid4(),created_at=datetime.now(UTC), **athlete_in.model_dump())
        
        athlete_model = AthleteModel(**athlete_out.model_dump(exclude={'category','training_center'}))
        
        athlete_model.training_center_id = training_center.pk_id
        
        athlete_model.category_id = category.pk_id
        
        db_session.add(athlete_model)
        
        await db_session.commit()
        
    except Exception:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail=f"An error occurred while inserting data into the database, the athlete already exists")
        
    return athlete_out


@router.get('/',summary='Browse all athletes',status_code=status.HTTP_200_OK,response_model=list[AthleteOut])
async def query(db_session: DatabaseDependency) -> list[AthleteOut]:
    athletes: list[AthleteOut] = (await db_session.execute(select(AthleteModel))).scalars().all()
    
    return [AthleteOut.model_validate(athlete) for athlete in athletes] 


@router.get('/{id}',summary='Browse a athlete by id',status_code=status.HTTP_200_OK,response_model=AthleteOut)
async def query(id: UUID4, db_session: DatabaseDependency) -> AthleteOut:
    athlete: AthleteOut = (await db_session.execute(select(AthleteModel).filter_by(id=id))).scalars().first()
    
    if not athlete:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'No athlete was found with the given id: {id}')
    
    return athlete


@router.patch('/{id}',summary='Edit a athlete by id',status_code=status.HTTP_200_OK,response_model=AthleteOut)
async def query(id: UUID4, db_session: DatabaseDependency, athlete_up: AthleteUpdate = Body(...)) -> AthleteOut:
    athlete: AthleteOut = (await db_session.execute(select(AthleteModel).filter_by(id=id))).scalars().first()
    
    if not athlete:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'No athlete was found with the given id: {id}')
    
    athlete_update = athlete_up.model_dump(exclude_unset=True)
    
    for key,value in athlete_update.items():
        setattr(athlete,key,value)
    
    await db_session.commit()
    
    await db_session.refresh(athlete)
    
    return athlete


@router.delete('/{id}',summary='Delete a athlete by id',status_code=status.HTTP_204_NO_CONTENT)
async def query(id: UUID4, db_session: DatabaseDependency) -> None:
    athlete: AthleteOut = (await db_session.execute(select(AthleteModel).filter_by(id=id))).scalars().first()
    
    if not athlete:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'No athlete was found with the given id: {id}')
    
    await db_session.delete(athlete)
    
    await db_session.commit()