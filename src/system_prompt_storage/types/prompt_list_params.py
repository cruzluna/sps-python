# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["PromptListParams"]


class PromptListParams(TypedDict, total=False):
    category: str
    """The category of the prompts to return"""

    from_: Annotated[int, PropertyInfo(alias="from")]
    """The pagination offset to start from (0-based)"""

    size: int
    """The number of prompts to return"""

    to: int
    """The pagination offset to end at (exclusive)"""
