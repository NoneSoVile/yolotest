from ultralytics import YOLO
import argparse
parser = argparse.ArgumentParser(description='yolo predict')
tasktype = 'detect'
modelsize = 'n'
parser.add_argument('--tasktype', default=tasktype, type=str, 
                    help='type of task')
parser.add_argument('--modelsize', default=modelsize, type=str, 
                    help='size type of model')
args = parser.parse_args()
tasktype = args.tasktype
modelsize = args.modelsize
print(f'tasktype: {tasktype} model size: {modelsize}')
if tasktype == 'detect':    
    # Create a new YOLO model from scratch
    model = YOLO(f"yolov8{modelsize}.pt")
    # Load a pretrained YOLO model (recommended for training)
    #model = YOLO("train15/weights/best.pt")
elif tasktype == 'classify':
    model = YOLO(f"yolov8{modelsize}-cls.pt")
elif tasktype == 'segment':
    model = YOLO(f"yolov8{modelsize}-seg.pt")
elif tasktype == 'pose':
    model = YOLO(f"yolov8{modelsize}-pose.pt")
elif tasktype == 'track':
    # Load an official or custom model
    model = YOLO(f"yolov8{modelsize}.pt")  # Load an official Detect model
    model = YOLO(f"yolov8{modelsize}-seg.pt")  # Load an official Segment model
    model = YOLO(f"yolov8{modelsize}-pose.pt")  # Load an official Pose model
    #model = YOLO(f"path/to/best.pt")  # Load a custom trained model

    # Perform tracking with the model
    results = model.track("video\ADHD Personified.mp4", show=True)  # Tracking with default tracker
    exit()
    #results = model.track("https://youtu.be/LNwODJXcvt4", show=True, tracker="bytetrack.yaml")  # with ByteTrack
else:
    print("input the correct type of task")
    exit()


# Evaluate the model's performance on the validation set
#results = model.val()

# Perform object detection on an image using the model
filelist = ["cat1.jpg", "cat2.jpg","view1.jpg", "yf1.jpg", "bus.jpg", "dance.jpg"]
results = model(filelist)
for result in results:
    name = result.path
    name = name.replace('.jpg', f'{tasktype}.jpg')
    result.save(filename=name)

# Export the model to ONNX format
#success = model.export(format="onnx")
