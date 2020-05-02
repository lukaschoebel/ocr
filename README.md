# OCR

The objective of this repository is to understand common techniques for extracting text from handwritten documents. In general, the goal is to obtain the text from transcribed German letters from the beginning of the 20th century.

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->


- [Learnings](#learnings)
- [Virtual Environment HowTo](#virtual-environment-howto)
- [Requirements](#requirements)
- [Acknowledgements](#acknowledgements)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Learnings

In the beginning, the use of `tesseract` was evaluated but it was found out that the library only performs reasonably well when the data is not too noisy and machine written. The script `tesseract_ocr.py` takes images in `.png` format, preprocesses them and prints the detected string to the console. In the current version, it is neither possible to detect special characters like *ü*, *ä* or *ß*, nor possible to execute the script on other image file formats.

## Virtual Environment HowTo

- Install [Conda](https://docs.conda.io/en/latest/miniconda.html)
- Create Virtual environment with `conda create -n <ENV_NAME> python=3.6`
- Activate venv with `conda activate <ENV_NAME>`
- Install requirements with `pip install -r requirements.txt` and openCV with `conda install -c menpo opencv`
- Removing venv by first deactivataing and then `conda env remove -n <ENV_NAME>`

## Requirements

- conda[`tesseract`](https://github.com/tesseract-ocr/tesseract)
- `openCV`

## Acknowledgements

- Kudos to Adrian Rosebrocks and his [OCR Tutorial](https://www.pyimagesearch.com/2017/07/10/using-tesseract-ocr-python/)
