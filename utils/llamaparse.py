import os
from llama_cloud_services import LlamaParse


def parse_document(source_path, api_key=None, num_workers=4, language="en"):
    """Parse document using LlamaParse and return result"""
    if not api_key:
        api_key = os.environ.get("LLAMA_API_KEY")

    parser = LlamaParse(
        api_key=api_key,
        num_workers=num_workers,
        verbose=True,
        language=language,
    )

    return parser.parse(source_path)
