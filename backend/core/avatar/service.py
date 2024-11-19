import random
import string
import os

from ..models.avatar_model import Avatar
from django.core.files.uploadedfile import UploadedFile
from django.core.exceptions import ObjectDoesNotExist
from django.core.exceptions import ValidationError
from minio import Minio, S3Error

minio_client = Minio(
    endpoint=os.getenv("MINIO_URL", "localhost:9000"),
    access_key=os.getenv("MINIO_ACCESS_KEY", "none"),
    secret_key=os.getenv("MINIO_SECRET_KEY", "none"),
    secure=False if os.getenv("DEBUG", "True") == "True" else True,
)

BUCKET_NAME = os.getenv("MINIO_BUCKET_NAME", "notset")
FOLDER_NAME = "avatars"

def generate_random_string(length=20) -> str:
    """_summary_

    Args:
        length (int, optional): _description_. Defaults to 20.

    Returns:
        _type_: _description_
    """
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def upload_avatar(file: UploadedFile) -> Avatar:
    """
    Upload a new avatar image to minio and create a new Avatar instance.
    
    Args:
        file (UploadedFile): The file to be saved in the Avatar instance.
    
    Returns:
        Avatar: The created Avatar instance.
    """
    # check if bucket exists
    if not minio_client.bucket_exists(BUCKET_NAME):
        raise ValidationError("Bucket does not exist.")
    
    # generate a random string name for the file: random_string that include both numbers and letters 20 characters long
    file.name = f"{generate_random_string()}_avatar_{file.name}"
    try:
        # Save the file to MinIO
        minio_client.put_object(
            bucket_name=BUCKET_NAME,
            object_name=f"{FOLDER_NAME}/{file.name}",
            content_type=file.content_type,
            data=file,
            length=file.size,
        )
    except S3Error as e:
        raise ValidationError(f"S3Error uploading file: {str(e)}")
    except Exception as e:
        raise ValidationError(f"Error uploading file: {str(e)}")
    
    avatar_url = f"{os.getenv('MINIO_URL', 'localhost:9000')}/{BUCKET_NAME}/{FOLDER_NAME}/{file.name}"
    avatar = Avatar(avatar_url=avatar_url)
    avatar.save()  # Save the instance to trigger any custom save logic if needed
    return avatar