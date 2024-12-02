import json

from ord_schema.message_helpers import load_message, write_message
from ord_schema.proto import dataset_pb2
from google.protobuf.json_format import MessageToJson

input_fname = "/Users/zhaodongliu/Documents/GitHub/ord-data/data/0a/ord_dataset-0a66204fc43e49c2922e6f9107e6b62f.pb.gz"
dataset = load_message(
    input_fname,
    dataset_pb2.Dataset,
)

# take one reaction message from the dataset for example
rxn = dataset.reactions[0]
rxn_json = json.loads(
    MessageToJson(
        message=rxn,
        including_default_value_fields=False,
        preserving_proto_field_name=True,
        indent=2,
        sort_keys=False,
        use_integers_for_enums=False,
        descriptor_pool=None,
        float_precision=None,
        ensure_ascii=True,
    )
)

print(f"We have converted the {input_fname} to JSON format shown as below, \n{rxn_json}")