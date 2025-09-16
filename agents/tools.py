from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field





class BlogInput(BaseModel):
    """Input schema for BlogUploadTool."""
    title: str = Field(..., description="Title of the blog.")
    content: str = Field(..., description="Contents of the blog of the blog.")

class BlogUploadTool(BaseTool):
    name: str = "blog_uploader"
    description: str = (
        "A tool for uploading a blog post to the website. It requires a title and the content of the blog."
    )
    args_schema: Type[BaseModel] = BlogInput

    def _run(self, title: str, content: str) -> str:
        from blog.models import Blog
        Blog.objects.create(title=title, content=content)
        return "Blog post uploaded successfully."
        

