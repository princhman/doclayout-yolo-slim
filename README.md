# DocLayout-YOLO-Slim

This library is just a lightweight slim version of the original [doclayout-yolo library](https://github.com/opendatalab/DocLayout-YOLO) focued on inference of the models that were developed by OpenDataLab.

## Installation

### From PyPI (Coming Soon)
```bash
pip install doclayout-yolo-slim
```

### From Source
```bash
git clone https://github.com/princhman/doclayout-yolo-slim.git
cd doclayout-yolo-slim
pip install -e .
```

### Using uv
```bash
uv add doclayout-yolo-slim
```

## Quick Start

```python
from doclayout_yolo_slim.models import YOLOv10

# Load the model
model = YOLOv10(model="doclayout_yolo_docsynth300k_imgsz1600.pt")

# Run inference
results = model.predict("path/to/your/image.png")
print(results)
```


## Model Files

You'll need the pre-trained model file with original library. The example uses `doclayout_yolo_docsynth300k_imgsz1600.pt` which should be placed in your project directory or specify the full path.

## Requirements

- Python >= 3.11
- PyTorch >= 2.7.1
- OpenCV >= 4.11.0
- NumPy >= 2.3.1
- Other dependencies listed in `pyproject.toml`

## Performance

This slim implementation offers:
- Reduced memory usage
- Faster inference times
- Smaller package size
- Simplified codebase for easier maintenance

## License

This project is licensed under the AGPL-3.0 License - see the LICENSE file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Acknowledgments

- Based on the original ultralytics YOLO implementation
- Inspired by doclayout-yolo for document layout analysis
- Optimized for production use cases requiring speed and efficiency

## Changelog

### v0.1.0
- Initial release
- Simplified YOLOv10 implementation
