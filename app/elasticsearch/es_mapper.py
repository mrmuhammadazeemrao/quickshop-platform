from app.elasticsearch.es_dsl import ProductDocument, SubCategoryDocument


def subcategory_to_document(sub_category):
    return SubCategoryDocument(
        meta={"id": sub_category.id},
        title=sub_category.title,
        parent_id=sub_category.parent_id
    )


def product_to_document(product):
    return ProductDocument(
        meta={"id": product.id},
        title=product.title,
        description=product.description,
        price=product.price,
        image=product.image,
        sub_category=subcategory_to_document(product.category)
    )
