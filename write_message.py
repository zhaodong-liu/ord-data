# import requirements
from ord_schema.message_helpers import load_message, write_message
from ord_schema.proto import dataset_pb2

# load the binary ord file
dataset = load_message("/Users/zhaodongliu/Documents/GitHub/ord-data/data/0a/ord_dataset-0a66204fc43e49c2922e6f9107e6b62f.pb.gz", dataset_pb2.Dataset)
# save the ord file as human readable text
write_message(dataset, "output_fname.pbtxt")