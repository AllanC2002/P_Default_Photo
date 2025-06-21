from conections.mongo import conection_mongo
from bson import ObjectId

def assign_default_photo(user_id):
    
    db = conection_mongo()

    default_image = db.Images.find_one({"name": "Default photo"})

    if not default_image:
        return {"error": "Default image not found"}, 404

    db.UserPhotos.update_one(
        {"user_id": user_id},
        {"$set": {"image_id": default_image["_id"]}},
        upsert=True
    )

    return {"message": f"Default photo assigned to user {user_id}"}, 200
