from fastapi import APIRouter, HTTPException

from fastapi import Body

from fastapi import status

from pydantic import UUID4

from sqlalchemy.future import select

from uuid import uuid4

from workout_api.categories.schemas import CategoriesIn, CategoriesOut

from workout_api.contrib.dependencies import DatabaseDependency

from workout_api.categories.models import CategoriesModel

router = APIRouter()

@router.post('/',summary='Create a new category',status_code=status.HTTP_201_CREATED,response_model=CategoriesOut)
async def post(db_session: DatabaseDependency, categories_in: CategoriesIn = Body(...)) -> CategoriesOut:
    
    categories_out = CategoriesOut(id=uuid4(), **categories_in.model_dump())
    categories_model = CategoriesModel(**categories_out.model_dump())
    
    db_session.add(categories_model)
    await db_session.commit()
    
    return categories_out


@router.get('/',summary='Browse all categories',status_code=status.HTTP_200_OK,response_model=list[CategoriesOut])
async def query(db_session: DatabaseDependency) -> list[CategoriesOut]:
    categories: list[CategoriesOut] = (await db_session.execute(select(CategoriesModel))).scalars().all()
    
    return categories


@router.get('/{id}',summary='Browse a category by id',status_code=status.HTTP_200_OK,response_model=CategoriesOut)
async def query(id: UUID4, db_session: DatabaseDependency) -> CategoriesOut:
    category: CategoriesOut = (await db_session.execute(select(CategoriesModel).filter_by(id=id))).scalars().first()
    
    if not category:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'No category was found with the given id: {id}')
    
    return category
