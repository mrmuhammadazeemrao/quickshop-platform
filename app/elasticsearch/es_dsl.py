from elasticsearch_dsl import Document, Text, Integer, Float, Nested


class SubCategoryDocument(Document):
    title = Text()
    parent_id = Integer()

    class Index:
        name = "subcategory_index"


class ProductDocument(Document):
    title = Text()
    description = Text()
    price = Float()
    image = Text()

    sub_category = Nested(SubCategoryDocument)

    class Index:
        name = "products_index"
