from llama_cloud_services import LlamaParse
import getpass
import os


def parse_document(source_path, num_workers=4, language="en"):
    """Parse document using LlamaParse and return result"""
    def set_env(var: str):
        if not os.environ.get(var):
            os.environ[var] = getpass.getpass(f"{var}: ")

    set_env("LLAMA_API_KEY")

    parser = LlamaParse(
        api_key=os.environ.get("LLAMA_API_KEY"),
        num_workers=num_workers,
        result_type="markdown",
        verbose=True,
        language=language,
    )

    return parser.parse(source_path)
