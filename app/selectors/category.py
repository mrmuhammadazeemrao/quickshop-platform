from sqlalchemy.orm import Session, aliased

from app.models.product import Category
from app.serializers.category import CategorySerializer, SubCategorySerializer


def selector_get_categories_with_sub_categories(db: Session):
    sub_categories = aliased(Category, name="subcategory")

    queryset = (db.query(Category, sub_categories)
                .outerjoin(sub_categories, Category.id == sub_categories.parent_id)
                .filter(Category.parent_id == None).all())

    categories_with_sub_categories = []

    for category, subcategory in queryset:
        category_serializer = next((existing_category for existing_category in categories_with_sub_categories if
                                    existing_category.id == category.id), None)

        if not category_serializer:
            category_serializer = CategorySerializer(id=category.id, title=category.title, sub_categories=[])
            categories_with_sub_categories.append(category_serializer)

        if subcategory:
            subcategory_serializer = SubCategorySerializer(id=subcategory.id, title=subcategory.title)
            category_serializer.sub_categories.append(subcategory_serializer)

    return categories_with_sub_categories
