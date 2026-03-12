"""Pipeline tools — define and execute multi-step notebook workflows."""

from typing import Any

from ...services import pipeline as pipeline_service
from ...services.errors import ServiceError
from ._utils import get_client, logged_tool


@logged_tool()
def pipeline_run(
    notebook_id: str,
    pipeline_name: str,
    input_url: str = "",
) -> dict[str, Any]:
    """Execute a pipeline on a notebook.

    Pipelines are sequences of actions (source_add, notebook_query, studio_create, etc.)
    executed in order. Use pipeline_list to see available pipelines.

    Args:
        notebook_id: Target notebook UUID
        pipeline_name: Pipeline name (e.g. "ingest-and-podcast", "research-and-report")
        input_url: URL variable for pipelines that need it (replaces $INPUT_URL)
    """
    try:
        client = get_client()
        variables = {}
        if input_url:
            variables["INPUT_URL"] = input_url

        result = pipeline_service.pipeline_run(client, notebook_id, pipeline_name, variables)
        return {"status": "success", **result}
    except ServiceError as e:
        return {"status": "error", "error": e.user_message}
    except Exception as e:
        return {"status": "error", "error": str(e)}


@logged_tool()
def pipeline_list() -> dict[str, Any]:
    """List all available pipelines (builtin and user-defined).

    Returns pipeline names, descriptions, and step counts.
    """
    try:
        pipelines = pipeline_service.pipeline_list()
        return {
            "status": "success",
            "pipelines": pipelines,
            "count": len(pipelines),
        }
    except Exception as e:
        return {"status": "error", "error": str(e)}
