from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = ROOT_DIR / "data"

RAW_DIR = DATA_DIR / "raw"
PARSED_DIR = DATA_DIR / "parsed"
PROCESSED_DIR = DATA_DIR / "processed"
SEQUENCE_DIR = DATA_DIR / "sequences"
EMBEDDING_DIR = DATA_DIR / "embeddings"

BGL_DIR = RAW_DIR / "BGL"
OPENSTACK_DIR = RAW_DIR / "OpenStack"
HDFS_DIR = RAW_DIR / "HDFS"