from pydantic import (
    BaseModel,
    Field,
    validator
)


class PagesModel(BaseModel):
    fb: int = Field(...)
    ig: int = Field(...)
    tw: int = Field(...)
    ga: int = Field(...)

class PostsModel(BaseModel):
    scheduled: int = Field(...)
    now: int = Field(...)
    drafts: int = Field(...)

class BasePackageModel(BaseModel):
    user_profiles: int = Field(...)
    pages: PagesModel = Field(...)
    posts: PostsModel = Field(...)

