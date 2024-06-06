from ultralytics import YOLO
import argparse
data_path='/home/yf/data2/yoloworkspace/coco_converted/data.yaml'
parser = argparse.ArgumentParser(description='yolo on coco Training')
parser.add_argument('--epochs', default=30, type=int, 
                    help='number of total epochs to run')
parser.add_argument('--batch', default=32, type=int, 
                    help='batch size of training data')
parser.add_argument('--data', default=data_path, type=str, 
                    help='data path of training data')
# Load a model
model = YOLO("yolov8n.yaml")  # build a new model from YAML


# Train the model
args = parser.parse_args()
epochs = int(args.epochs)
batch = int(args.batch)
data_path = args.data
print(f"training setting: epochs = {epochs}, batch = {batch}, data = {data_path}")
results = model.train(data=data_path, epochs=epochs, imgsz=640, batch=batch)