from fastapi import FastAPI, Query
from pydantic import BaseModel
from typing import Annotated
from enum import Enum


class FoodCategory(str, Enum):
    food = 'food'
    drink = 'drink'
    dessert = 'dessert'


class Food(BaseModel):
    name: str
    price: float
    category: FoodCategory
    promotion: bool = False
    description: str | None = None


app = FastAPI()

@app.get("/foods")
async def getFood(sort: bool | None = False):
    return {
        'success': True,
        'is_sorted': sort,
    }

@app.get('/foody')
async def getFoody(search: Annotated[str, Query(alias='item-query', title='The query to sesssarch for', description='The query to search for', min_length=3, max_length=50, deprecated=True)]):
    return {
        'success': True,
        'search': search,
    }

@app.post('/foods')
async def createFood(food: Food):
    return {
        'success': True,
        'food': food,
    }