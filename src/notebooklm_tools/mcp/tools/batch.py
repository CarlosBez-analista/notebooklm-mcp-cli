"""Batch tools — perform operations across multiple notebooks."""

from typing import Any

from ...services import batch as batch_service
from ...services.errors import ServiceError
from ._utils import get_client, logged_tool


@logged_tool()
def batch_query(
    query: str,
    notebook_names: str | None = None,
    tags: str | None = None,
    all: bool = False,
) -> dict[str, Any]:
    """Query multiple notebooks with the same question.

    Args:
        query: Question to ask across notebooks
        notebook_names: Comma-separated notebook names or IDs
        tags: Comma-separated tags to select notebooks
        all: Query ALL notebooks
    """
    try:
        client = get_client()
        names = [n.strip() for n in notebook_names.split(",") if n.strip()] if notebook_names else None
        tag_list = [t.strip() for t in tags.split(",") if t.strip()] if tags else None

        result = batch_service.batch_query(client, query, names, tag_list, all)
        return {"status": "success", **result}
    except ServiceError as e:
        return {"status": "error", "error": e.user_message}
    except Exception as e:
        return {"status": "error", "error": str(e)}


@logged_tool()
def batch_add_source(
    source_url: str,
    notebook_names: str | None = None,
    tags: str | None = None,
    all: bool = False,
) -> dict[str, Any]:
    """Add the same source URL to multiple notebooks.

    Args:
        source_url: URL to add as source to each notebook
        notebook_names: Comma-separated notebook names or IDs
        tags: Comma-separated tags to select notebooks
        all: Add to ALL notebooks
    """
    try:
        client = get_client()
        names = [n.strip() for n in notebook_names.split(",") if n.strip()] if notebook_names else None
        tag_list = [t.strip() for t in tags.split(",") if t.strip()] if tags else None

        result = batch_service.batch_add_source(client, source_url, names, tag_list, all)
        return {"status": "success", **result}
    except ServiceError as e:
        return {"status": "error", "error": e.user_message}
    except Exception as e:
        return {"status": "error", "error": str(e)}


@logged_tool()
def batch_create(titles: str) -> dict[str, Any]:
    """Create multiple notebooks at once.

    Args:
        titles: Comma-separated notebook titles (e.g. "Project A, Project B, Project C")
    """
    try:
        client = get_client()
        title_list = [t.strip() for t in titles.split(",") if t.strip()]
        result = batch_service.batch_create(client, title_list)
        return {"status": "success", **result}
    except ServiceError as e:
        return {"status": "error", "error": e.user_message}
    except Exception as e:
        return {"status": "error", "error": str(e)}


@logged_tool()
def batch_delete(
    notebook_names: str | None = None,
    tags: str | None = None,
    confirm: bool = False,
) -> dict[str, Any]:
    """Delete multiple notebooks. IRREVERSIBLE. Requires confirm=True.

    Args:
        notebook_names: Comma-separated notebook names or IDs
        tags: Comma-separated tags to select notebooks to delete
        confirm: Must be True after user approval
    """
    if not confirm:
        return {
            "status": "error",
            "error": "Batch delete not confirmed. Ask the user to confirm before setting confirm=True.",
            "warning": "This action is IRREVERSIBLE. Multiple notebooks will be permanently deleted.",
        }

    try:
        client = get_client()
        names = [n.strip() for n in notebook_names.split(",") if n.strip()] if notebook_names else None
        tag_list = [t.strip() for t in tags.split(",") if t.strip()] if tags else None

        result = batch_service.batch_delete(client, names, tag_list, confirm=True)
        return {"status": "success", **result}
    except ServiceError as e:
        return {"status": "error", "error": e.user_message}
    except Exception as e:
        return {"status": "error", "error": str(e)}


@logged_tool()
def batch_studio(
    artifact_type: str = "audio",
    notebook_names: str | None = None,
    tags: str | None = None,
    all: bool = False,
) -> dict[str, Any]:
    """Generate studio artifacts (audio, video, etc.) across multiple notebooks.

    Args:
        artifact_type: Type: audio, video, report, flashcards, infographic, mindmap, quiz, slides, data_table
        notebook_names: Comma-separated notebook names or IDs
        tags: Comma-separated tags to select notebooks
        all: Generate for ALL notebooks
    """
    try:
        client = get_client()
        names = [n.strip() for n in notebook_names.split(",") if n.strip()] if notebook_names else None
        tag_list = [t.strip() for t in tags.split(",") if t.strip()] if tags else None

        result = batch_service.batch_studio(client, artifact_type, names, tag_list, all)
        return {"status": "success", **result}
    except ServiceError as e:
        return {"status": "error", "error": e.user_message}
    except Exception as e:
        return {"status": "error", "error": str(e)}
