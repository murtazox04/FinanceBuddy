from typing import Optional, List
from asgiref.sync import sync_to_async
from django.db import IntegrityError, models

from apps.finance.models import ExpenseCategory


async def get_categories(
    _id: Optional[int] = None,
    user_id: Optional[int] = None,
    parent_id: Optional[int] = None,
) -> List[ExpenseCategory]:
    query = models.Q(is_active=True, user_id=None)
    if _id:
        query &= models.Q(id=_id)
    if user_id:
        query |= models.Q(user_id=user_id)
    if parent_id:
        query &= models.Q(parent_id=parent_id)
    data = await sync_to_async(list)(ExpenseCategory.objects.filter(query))
    return await sync_to_async(list)(ExpenseCategory.objects.filter(query))


async def create_category(
    name: str,
    user_id: Optional[int] = None,
    parent_id: Optional[int] = None,
) -> ExpenseCategory:
    if parent_id:
        parent_category = await sync_to_async(ExpenseCategory.objects.filter(id=parent_id).first)()
        if not parent_category:
            raise ValueError("Parent category does not exist.")
        if parent_category.user_id and parent_category.user_id != user_id:
            raise ValueError("Cannot create a subcategory under another user's category.")
    try:
        return await sync_to_async(ExpenseCategory.objects.create)(
            name=name,
            user_id=user_id,
            parent_id=parent_id,
        )
    except IntegrityError:
        error_message = f"Category with name '{name}' already exists for this user."
        raise ValueError(error_message)
