"""MCP Tools - Modular tool definitions for NotebookLM MCP Server."""

# Import all tools from submodules for registration
from .downloads import download_artifact
from .auth import refresh_auth, save_auth_tokens
from .notebooks import (
    notebook_list,
    notebook_get,
    notebook_describe,
    notebook_create,
    notebook_rename,
    notebook_delete,
)
from .sources import (
    source_add,
    source_list_drive,
    source_sync_drive,
    source_delete,
    source_describe,
    source_get_content,
)
from .sharing import (
    notebook_share_status,
    notebook_share_public,
    notebook_share_invite,
    notebook_share_batch,
)
from .research import (
    research_start,
    research_status,
    research_import,
)
from .studio import (
    studio_create,
    studio_status,
    studio_delete,
    studio_revise,
)
from .chat import (
    notebook_query,
    chat_configure,
)
from .exports import (
    export_artifact,
)
from .notes import note
from .server import server_info
from .batch import (
    batch_query,
    batch_source_add,
    batch_studio_create,
    batch_notebook_list,
    batch_notebook_delete,
)
from .cross_notebook import cross_notebook_query
from .pipeline import pipeline_run, pipeline_list
from .smart_select import (
    smart_select_tag_add,
    smart_select_tag_remove,
    smart_select_tag_list,
    smart_select_query,
)
from .studio_advanced import studio_create_advanced

__all__ = [
    # Downloads (1 consolidated)
    "download_artifact",
    # Auth (2)
    "refresh_auth",
    "save_auth_tokens",
    # Notebooks (6)
    "notebook_list",
    "notebook_get",
    "notebook_describe",
    "notebook_create",
    "notebook_rename",
    "notebook_delete",
    # Sources (6)
    "source_add",
    "source_list_drive",
    "source_sync_drive",
    "source_delete",
    "source_describe",
    "source_get_content",
    # Sharing (4)
    "notebook_share_status",
    "notebook_share_public",
    "notebook_share_invite",
    "notebook_share_batch",
    # Research (3)
    "research_start",
    "research_status",
    "research_import",
    # Studio (4 - consolidated create + revise)
    "studio_create",
    "studio_status",
    "studio_delete",
    "studio_revise",
    # Chat (2)
    "notebook_query",
    "chat_configure",
    # Exports (1)
    "export_artifact",
    # Notes (1 consolidated)
    "note",
    # Server (1)
    "server_info",
    # Batch (5)
    "batch_query",
    "batch_source_add",
    "batch_studio_create",
    "batch_notebook_list",
    "batch_notebook_delete",
    # Cross-notebook (1)
    "cross_notebook_query",
    # Pipeline (2)
    "pipeline_run",
    "pipeline_list",
    # Smart select (4)
    "smart_select_tag_add",
    "smart_select_tag_remove",
    "smart_select_tag_list",
    "smart_select_query",
    # Studio advanced (1)
    "studio_create_advanced",
]
