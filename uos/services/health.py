"""
Universal Observatory Operating System
Health Service v0.1
"""

from uos.kernel.registry import list_objects
from uos.kernel.relationship import list_relationships
from uos.kernel.knowledge_graph import (
    graph_statistics,
    dangling_relationships,
)
from uos.kernel.manifest import (
    KERNEL_NAME,
    KERNEL_VERSION,
)


def kernel_health():

    stats = graph_statistics()
    dangling = dangling_relationships()

    return {

        "kernel": KERNEL_NAME,

        "version": KERNEL_VERSION,

        "objects": stats["objects"],

        "relationships": stats["relationships"],

        "average_degree": stats["average_degree"],

        "dangling_relationships": len(dangling),

        "status":

            "HEALTHY"

            if len(dangling) == 0

            else "WARNING"
    }