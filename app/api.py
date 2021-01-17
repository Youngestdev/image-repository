import os
import shutil
from typing import List

from fastapi import FastAPI, Body, HTTPException, status, UploadFile, File, Depends

from app.auth.auth_bearer import JWTBearer
from app.auth.auth_handler import signJWT
from app.model import UserModel

app = FastAPI()

# Temporary in-app user database.
users = []
current_user = []


def check_user(data: UserModel):
    for user in users:
        if user.username == data.username and user.password == data.password:
            return True
    return False


@app.get("/", tags=["Root"])
async def get_root() -> dict:
    return {
        "message": "Welcome to the Shopify internship challenge."
    }


@app.post("/user/new", status_code=status.HTTP_201_CREATED, tags=["User"])
async def register(user: UserModel = Body(...)):
    users.append(user)
    return {
        "message": "User successfully created, log in to continue"
    }


@app.post("/user/login", status_code=status.HTTP_200_OK, tags=["User"])
async def login(user: UserModel = Body(...)):
    if check_user(user):
        current_user.append(user.username)
        return signJWT(user.username)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User doesn't exist.")


@app.post("/image", dependencies=[Depends(JWTBearer())], status_code=status.HTTP_200_OK, tags=["Image Upload"])
async def upload_single_image(image: UploadFile = File(...)):
    image_storage_path = "images/{}/".format(current_user[0])
    if not os.path.isdir(image_storage_path):
        os.mkdir(image_storage_path)
    with open(image_storage_path + image.filename, "wb") as new_image:
        shutil.copyfileobj(image.file, new_image)

    return {
        "message": "Image uploaded successfully."
    }


@app.post("/images/", dependencies=[Depends(JWTBearer())], status_code=status.HTTP_200_OK, tags=["Image Upload"])
async def upload_bulk_images(images: List[UploadFile] = File(...)):
    image_storage_path = "images/{}/".format(current_user[0])
    if not os.path.isdir(image_storage_path):
        os.mkdir(image_storage_path)
    for image in images:
        with open(image_storage_path + image.filename, "wb") as new_image:
            shutil.copyfileobj(image.file, new_image)

    return {
        "message": "Images uploaded successfully."
    }


@app.delete("/image", dependencies=[Depends(JWTBearer())], status_code=status.HTTP_200_OK, tags=["Image Deletion"])
async def delete_single_image(image_name: str = Body(...)):
    image_path = "images/{0}/{1}".format(current_user[0], image_name)
    if os.path.isfile(image_path):
        os.remove(image_path)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Image doesn't exist.")

    return {
        "message": "Image deleted successfully."
    }

@app.delete("/images/", dependencies=[Depends(JWTBearer())], status_code=status.HTTP_200_OK, tags=["Image Deletion"])
async def delete_bulk_images(image_names: List[str] = Body(...)):
    for image_name in image_names:
        image_path = "images/{0}/{1}".format(current_user[0], image_name)
        if os.path.isfile(image_path):
            os.remove(image_path)

    return {
        "message": "Images removed successfully."
    }