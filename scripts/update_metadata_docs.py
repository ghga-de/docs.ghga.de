# Copyright 2021 - 2023 Universität Tübingen, DKFZ, EMBL, and Universität zu Köln
# for the German Human Genome-Phenome Archive (GHGA)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

"""Script to generate user-facing metadata schema documentation"""

from pathlib import Path
from typing import Callable

import requests
import yaml
from jinja2 import Environment, FileSystemLoader
from linkml_runtime.utils.schemaview import SchemaView  # type: ignore
from pydantic import BaseModel, Field

HERE = Path(__file__).parent.resolve()
ROOT = HERE.parent
DOCS_DIR = ROOT / "docs" / "metadata" / "worksheets"
CONFIG_PATH = ROOT / ".workbook_config.yaml"

TEMPLATE = ".sheet_documentation_template.md"

SCHEMA_URL = "https://raw.githubusercontent.com/ghga-de/ghga-metadata-schema/main/src/schema/submission.yaml"  # pylint: disable=line-too-long

MAIN_WORKBOOK = "ghga_submission_full.xlsx"


class WorkbookConfigurationNotFound(Exception):
    """custom error to raise if the workbook config file does not exits in the given path"""


class MainSheetNotIdentified(Exception):
    """custom error to raise if the config does not have 'ghga_submission_full.xlsx'"""


class SchemaNotLoaded(Exception):
    """custom error to raise if the schema request return any response code other than 200"""


def load_config(config_path=CONFIG_PATH) -> dict:
    """Loads config file"""

    try:
        with open(config_path, "r", encoding="utf8") as config_file:
            return yaml.safe_load(config_file)
    except FileNotFoundError as exc:
        raise WorkbookConfigurationNotFound(
            f"Workbook configuration not found at: {config_path}"
        ) from exc


def load_schema(schema_url=SCHEMA_URL):
    """Loads schema"""

    schema_config = requests.get(schema_url, timeout=3)
    if schema_config.status_code == 200:
        return SchemaView(schema_config.text)
    raise SchemaNotLoaded(f"Schema could not be loaded from {SCHEMA_URL}")


def extract_slots_from(schema: SchemaView, sheet_name: str) -> list[dict]:
    """Extracts slot information of a given class"""

    return [
        {
            "name": definition.name,
            "alias": definition.alias,
            "description": definition.description,
            "data_type": definition.range,
            "required": definition.required,
        }
        for definition in schema.class_induced_slots(sheet_name)
    ]


def generate_workbook(
    schema: SchemaView,
    sheets: list[str],
    get_slots: Callable[[SchemaView, str], list[dict]],
) -> list[dict]:
    """Assembles the content of classes and their slots"""
    return [
        {
            "name": sheet,
            "description": schema.get_class(sheet).description,
            "slots": get_slots(schema, sheet),
        }
        for sheet in sheets
    ]


class WorkbookConfig(BaseModel):
    """A workbook configuration"""

    worksheets: list[str] = Field(default_factory=list)
    file_name: str


class Config(BaseModel):
    """Configures multiple workbooks each having a different set of worksheets"""

    workbooks: list[WorkbookConfig]

    @property
    def main_workbook(self):
        """Extract a workbook configuration based on file_name"""
        for sheet in self.workbooks:
            if sheet.file_name == MAIN_WORKBOOK:
                return sheet
            raise MainSheetNotIdentified(
                f"No workbook configuration is found for {MAIN_WORKBOOK}"
            )


def generate_markdown(content: dict) -> str:
    """Generates the markdown text by rendering the content into the template"""

    env = Environment(loader=FileSystemLoader(ROOT))
    template = env.get_template(TEMPLATE)
    return template.render(content)


def create_doc_file(out_dir: Path, name: str, content: str) -> None:
    """Creates a markdown file for a given sheet and content"""

    with open(out_dir / (name + ".md"), mode="w", encoding="utf8") as file:
        file.write(content)


def main():
    """Patches things together"""

    config = Config.model_validate(load_config())
    if config.main_workbook is None:
        raise MainSheetNotIdentified
    worksheet_names = config.main_workbook.worksheets

    schema = load_schema()
    workbook = generate_workbook(schema, worksheet_names, extract_slots_from)

    for sheet in workbook:
        create_doc_file(DOCS_DIR, sheet["name"], generate_markdown(sheet))


if __name__ == "__main__":
    main()
