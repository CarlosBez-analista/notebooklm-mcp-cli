"""Smart select tools — Tag management and intelligent notebook selection."""

from typing import Any

from ...services import smart_select as smart_select_service
from ...services.errors import ServiceError
from ._utils import logged_tool


@logged_tool()
def tag_add(
    notebook_id: str,
    tags: str,
    notebook_title: str = "",
) -> dict[str, Any]:
    """Add tags to a notebook for smart selection.

    Tags are stored locally and used by smart_select to find relevant notebooks.

    Args:
        notebook_id: Notebook UUID
        tags: Comma-separated tags (e.g. "ai,research,llm")
        notebook_title: Optional notebook title for display
    """
    try:
        tag_list = [t.strip() for t in tags.split(",") if t.strip()]
        result = smart_select_service.tag_add(notebook_id, tag_list, notebook_title)
        return {"status": "success", "notebook_id": notebook_id, "tags": result["tags"]}
    except ServiceError as e:
        return {"status": "error", "error": e.user_message}
    except Exception as e:
        return {"status": "error", "error": str(e)}


@logged_tool()
def tag_remove(
    notebook_id: str,
    tags: str,
) -> dict[str, Any]:
    """Remove tags from a notebook.

    Args:
        notebook_id: Notebook UUID
        tags: Comma-separated tags to remove (e.g. "ai,research")
    """
    try:
        tag_list = [t.strip() for t in tags.split(",") if t.strip()]
        result = smart_select_service.tag_remove(notebook_id, tag_list)
        return {"status": "success", "notebook_id": notebook_id, "tags": result["tags"]}
    except ServiceError as e:
        return {"status": "error", "error": e.user_message}
    except Exception as e:
        return {"status": "error", "error": str(e)}


@logged_tool()
def tag_list() -> dict[str, Any]:
    """List all tagged notebooks with their tags."""
    try:
        result = smart_select_service.tag_list()
        return {"status": "success", **result}
    except Exception as e:
        return {"status": "error", "error": str(e)}


@logged_tool()
def smart_select(query: str) -> dict[str, Any]:
    """Find notebooks relevant to a query using tags.

    Uses keyword matching against notebook tags to suggest which notebooks
    are most relevant for a given topic or question.

    Args:
        query: Natural language query or comma-separated tags (e.g. "ai mcp" or "ai,mcp")
    """
    try:
        result = smart_select_service.smart_select(query)
        return {"status": "success", **result}
    except ServiceError as e:
        return {"status": "error", "error": e.user_message}
    except Exception as e:
        return {"status": "error", "error": str(e)}
