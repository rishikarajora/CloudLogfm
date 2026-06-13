import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))

from ml.data_pipeline.ingestion.bgl_loader import BGLLoader

loader = BGLLoader()

print(loader.get_dataset_path())
print(loader.list_files())