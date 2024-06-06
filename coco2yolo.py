from ultralytics.data.converter import convert_coco
import sys
convert_coco(sys.argv[1], use_segments=True, use_keypoints=False, cls91to80=True)
#convert_coco('../datasets/lvis/annotations/', use_segments=True, use_keypoints=False, cls91to80=False, lvis=True)
